Folder Monitoring and File Upload Automation

This project automates the process of monitoring a folder for new pictures, uploading them to a specified server using the curl command, and moving the successfully uploaded pictures to an "uploaded" folder.

Features

Monitors a designated folder for new files.

Automatically uploads images using a curl POST request.

Moves successfully uploaded images to an "uploaded" folder to prevent redundancy.

Configurable upload interval and folder paths.

Prerequisites

Python 3.x installed on your system.

curl installed on your system (available by default on most Linux/Mac systems; for Windows, download it from curl website).

Configuration

Before running the script, update the following configuration variables in the script:

WATCH_FOLDER: Path to the folder where the camera saves images.

UPLOADED_FOLDER: Path to the folder where successfully uploaded images will be moved.

UPLOAD_URL: The server URL for uploading images.

UPLOAD_INTERVAL: Time interval (in seconds) to check for new images (default is 30 seconds).

Running the Script

Place the script file (e.g., folder_monitor_upload.py) in a directory.

Ensure you have proper read/write permissions for the specified folder paths.

Execute the script:

python folder_monitor_upload.py

Testing the Script

Set Up Test Folders:

Create a folder to simulate the camera's output (e.g., /path/to/camera/folder).

Create another folder to act as the "uploaded" folder (e.g., /path/to/uploaded/folder).

Add Test Files:

Add some test images to the camera folder.

Run the Script:

Start the script and observe its behavior.

Check for log outputs in the terminal for upload success/failure.

Verify that successfully uploaded files are moved to the uploaded folder.

Simulate Upload Failures:

Change the UPLOAD_URL to an invalid address and observe the error handling.

Example Output

Uploaded: /path/to/camera/folder/image1.jpg
Moved image1.jpg to uploaded folder.
Uploaded: /path/to/camera/folder/image2.jpg
Moved image2.jpg to uploaded folder.

Notes

Ensure network connectivity when testing the upload functionality.

Logs for errors will be printed to the console.

Make sure the curl command works independently before running the script.

Troubleshooting

If files are not being uploaded:

Check if curl is installed and working.

Verify the correctness of the UPLOAD_URL.

Ensure file paths and permissions are correct.

If files are not moved to the uploaded folder:

Check the UPLOADED_FOLDER path.

Verify folder permissions.

License

This script is provided as-is for educational purposes.