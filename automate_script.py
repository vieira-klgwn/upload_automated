import os
import time
import subprocess
from shutil import move

# Configuration
MONITOR_DIR = "/home/klgwn/Documents/klgwn/studies/embedded/photo_uploaded/cameraFolder"  # Folder to monitor
UPLOADED_DIR = os.path.join(MONITOR_DIR, "uploaded")  # Folder for uploaded files
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9d39741a93ed0356c/iot_testing_202501/upload.php"

# Ensure the uploaded directory exists
os.makedirs(os.path.normpath(UPLOADED_DIR), exist_ok=True)

def upload_file(file_path):
    """
    Uploads a file to the specified URL using curl.
    :param file_path: Path to the file to upload
    :return: True if upload is successful, False otherwise
    """
    try:
        result = subprocess.run(
            ["curl", "--http1.1", "-X", "POST", "-F", f"imageFile=@{file_path}", UPLOAD_URL],
            capture_output=True,
            text=True
        )
        # Log curl's output for debugging
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")

        if result.returncode == 0 and "200" in result.stdout:
            print(f"Upload successful: {file_path}")
            return True
        else:
            print(f"Upload failed for {file_path}: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"Error during upload: {e}")
        return False

def monitor_folder():
    """
    Monitors a folder for new files and uploads them if they are not recently modified.
    """
    print(f"Monitoring folder: {MONITOR_DIR}")
    while True:
        try:
            # Get list of files in the directory (ignoring the 'uploaded' folder)
            files = [
                f for f in os.listdir(MONITOR_DIR)
                if os.path.isfile(os.path.join(MONITOR_DIR, f)) and f != "uploaded"
            ]
            for file_name in files:
                file_path = os.path.join(MONITOR_DIR, file_name)
                
                # Check if the file has been modified at least 30 seconds ago
                if time.time() - os.path.getmtime(file_path) >= 30:
                    print(f"Processing file: {file_path}")
                    if upload_file(file_path):
                        # Move to 'uploaded' folder if successful
                        destination = os.path.join(UPLOADED_DIR, file_name)
                        move(file_path, destination)
                        print(f"Moved {file_name} to {UPLOADED_DIR}")
                    else:
                        print(f"Skipping file {file_name} due to upload failure.")
            # Pause for a short interval before re-scanning the folder
            time.sleep(10)
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"Error while monitoring folder: {e}")

if __name__ == "__main__":
    monitor_folder()
