from googleapiclient.http import MediaFileUpload
from Google import Create_Service

SECRET = '<ADD CLENT SECRET FILE LOCATION>'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(SECRET, API_NAME, API_VERSION, SCOPE)

folder_id = '<FOLDER-NAME>'

file_names = <FILE-NAME>
mime_types = <MIME-TYPE>

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_name, mimetype=mime_type)
    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
