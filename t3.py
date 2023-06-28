from googleapiclient.http import MediaFileUpload
from Google import Create_Service

SECRET = 'client_secret_904522675884-3lbn4r8ofhol51juuoa8sis76di3fmm7.apps.googleusercontent.com.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = Create_Service(SECRET, API_NAME, API_VERSION, SCOPE)

folder_id = '1SvvHNcap4c0qbLcY5iUBoqwC42krlVon'

file_names = ['test-plastic.mp4']
mime_types = ['video/mp4']

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
