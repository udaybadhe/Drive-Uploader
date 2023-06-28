# Google Drive File Upload

This script allows you to upload files to Google Drive using the Google Drive API. It utilizes the `googleapiclient` library and requires authentication through a client secret file.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed on your system.
2. The required Python libraries: `pickle`, `os`, `google_auth_oauthlib`, `googleapiclient`, and `google.auth.transport.requests`. You can install them using pip:
   ```
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```
3. A Google Cloud project with the Google Drive API enabled.
4. OAuth 2.0 client credentials (client secret file) for your Google Cloud project. Make sure you download the JSON file and save it securely.

## Setup

1. Place the `Google.py` file in the same directory as your script (`t3.py`) or in a location accessible to your script.
2. In the `t3.py` file, replace the following placeholders with your own values:
   - `<ADD CLIENT SECRET FILE LOCATION>`: Path to your client secret file.
   - `<FOLDER-NAME>`: ID of the folder in Google Drive where you want to upload the files.
   - `<FILE-NAME>`: List of file names to upload (e.g., `['file1.txt', 'file2.jpg']`).
   - `<MIME-TYPE>`: List of MIME types corresponding to the file names (e.g., `['text/plain', 'image/jpeg']`).

## Usage

To run the script and upload files to Google Drive, execute the `t3.py` script using Python:
```
python t3.py
```

The script will authenticate using the client secret file, upload the specified files to the specified Google Drive folder, and print the ID of each uploaded file.

Note: The first time you run the script, it will prompt you to authorize access to your Google Drive account through a web browser. Follow the instructions in the console to complete the authorization process. The script will save the authentication token in a pickle file (`token_drive_v3.pickle`) for future use, so you won't need to reauthorize each time you run the script.