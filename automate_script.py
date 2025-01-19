import os
import time
import subprocess
import shutil

# Configuration
WATCH_FOLDER = "/home/klgwn/Documents/klgwn/studies/embedded/photo_uploaded/cameraFolder" #path/to/camera/folder
UPLOADED_FOLDER = "/home/klgwn/Documents/klgwn/studies/embedded/photo_uploaded/uploadedFolder"
UPLOAD_URL = "https://projects.benax.rw/f/o/r/e/a/c/h/p/r/o/j/e/c/t/s/4e8d42b606f70fa9741a93ed0356c/iot_testing_202301/upload.php"
UPLOAD_INTERVAL = 30  # seconds

def monitor_folder():
    """Monitor the folder for new files and upload them."""
    while True:
        try:
            # Get list of files in the folder
            files = [f for f in os.listdir(WATCH_FOLDER) if os.path.isfile(os.path.join(WATCH_FOLDER, f))]

            for file_name in files:
                file_path = os.path.join(WATCH_FOLDER, file_name)

                # Upload the file
                success = upload_file(file_path)

                if success:
                    # Move the file to the uploaded folder
                    move_to_uploaded(file_name)

            # Wait before checking again
            time.sleep(UPLOAD_INTERVAL)

        except Exception as e:
            print(f"Error: {e}")

def upload_file(file_path):
    """Upload a file using curl."""
    try:
        command = [
            "curl",
            "-X", "POST",
            "-F", f"imageFile=@{file_path}",
            UPLOAD_URL
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"Uploaded: {file_path}")
            return True
        else:
            print(f"Failed to upload {file_path}. Error: {result.stderr.decode('utf-8')}")
            return False
    except Exception as e:
        print(f"Error while uploading {file_path}: {e}")
        return False

def move_to_uploaded(file_name):
    """Move the uploaded file to the uploaded folder."""
    try:
        source = os.path.join(WATCH_FOLDER, file_name)
        destination = os.path.join(UPLOADED_FOLDER, file_name)

        if not os.path.exists(UPLOADED_FOLDER):
            os.makedirs(UPLOADED_FOLDER)

        shutil.move(source, destination)
        print(f"Moved {file_name} to uploaded folder.")
    except Exception as e:
        print(f"Error moving {file_name}: {e}")

if __name__ == "__main__":
    monitor_folder()
