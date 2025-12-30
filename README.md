# Google Drive Uploader

A straightforward command-line tool for uploading files to a specific Google Drive folder.

## Setup

This project uses `uv` for dependency management.

1.  **Create and sync a virtual environment:**

    ```sh
    uv venv
    uv pip install -r requirements.txt
    ```

2.  **Configure your credentials:**

    -   Copy `config.json.example` to `config.json`.
    -   Update `config.json` with your Google Drive `folder_id` and the path to your `client_secret.json` file.

3.  **Authorize with Google:**

    The first time you run the script, it will open a browser window for you to authorize the application. This creates a local token so you only have to do it once.

## Usage

To upload a file, run `upload.py` with the file path as an argument.

```sh
python upload.py path/to/your/file.mp4
```

The script will show the upload progress and print the file ID when it's done.