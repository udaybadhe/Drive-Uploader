import sys
import os
import json
from googleapiclient.http import MediaFileUpload
from Google import Create_Service
import mimetypes

def upload_file(file_path, folder_id):
    """
    Uploads a file to a specific Google Drive folder.
    """
    service = Create_Service()
    if not service:
        return

    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return

    file_name = os.path.basename(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream' # Default MIME type

    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    try:
        media = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
        request = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        )
        
        response = None
        print(f"Uploading '{file_name}'...")
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%")
        
        print(f"File '{file_name}' uploaded successfully. File ID: {response.get('id')}")

    except Exception as e:
        print(f"An error occurred during upload: {e}")

def main():
    """
    Main function to handle command-line arguments and start the upload process.
    """
    if len(sys.argv) != 2:
        print("Usage: python upload.py <file_path>")
        return

    file_path = sys.argv[1]

    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: 'config.json' not found. Please create it from 'config.json.example'.")
        return

    folder_id = config.get('folder_id')
    if not folder_id or folder_id == 'YOUR_FOLDER_ID':
        print("Error: 'folder_id' not set in 'config.json'. Please update it with your Google Drive folder ID.")
        return

    upload_file(file_path, folder_id)

if __name__ == '__main__':
    main()