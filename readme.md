# Google Sheets API Integration using Flask

This is a simple Flask application that connects to a Google Sheet and returns the data in JSON format. The app downloads the credentials file from Google Drive and uses it to authorize the Google Sheets API.

## Requirements

- Flask
- Flask-CORS
- Pandas
- Numpy
- Gspread
- Oauth2client
- Requests

## Usage

To use this application, follow the steps below:

1. Create a new Google Sheet and share it with the service account email address provided in the credentials JSON file.
2. Copy the document key and the name of the sheet you want to access.
3. Upload the credentials JSON file to Google Drive and copy its file ID.
4. Edit the `app.py` file and replace the placeholders for `document_key`, `sheet` and `creds_id_google_drive` with the values obtained in steps 2 and 3.
5. Start the application by running `python app.py`.
6. Send a GET request to `http://localhost:5000/` to retrieve the data in JSON format.

## Code Overview

- The `download_google_drive_json_file` function downloads a JSON file from Google Drive given its ID.
- The `GoogleSheetDataFrame` class inherits from Pandas' DataFrame class and represents a Google Sheet.
- The Flask app is created and CORS is enabled.
- The `getData` function is the endpoint that retrieves the data from the Google Sheet and returns it in JSON format. It expects a JSON payload containing the document key, sheet name, and credentials file ID.

## Note

This application is meant for educational purposes only. It is not intended to be used in production environments. If you need to access Google Sheets from your application, it is recommended to use the Google Sheets API directly.

Here's an example of a cURL request to test the application:

```bash
curl --location --request GET 'http://localhost:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "doc_key": "your_document_key_here",
    "sheet": "your_sheet_name_here",
    "creds_id": "your_credentials_file_id_here"
}'
```

Replace the placeholders with your own values and run the command in your terminal to retrieve the data from the Google Sheet in JSON format.

Sure, here's a detailed explanation of where to get the variables needed to run the application:

- `doc_key`: This refers to the key of the Google Sheet document you want to access. You can find the document key in the URL of the Google Sheet. It is the part of the URL that comes after "/d/" and before "/edit". For example, if the URL of your Google Sheet is `https://docs.google.com/spreadsheets/d/abc123456789/edit#gid=0`, then the document key is `abc123456789`.

- `sheet`: This refers to the name of the sheet you want to access. If you have multiple sheets in your Google Sheet document, you need to specify the name of the sheet you want to access. The sheet name should be exact and match the name of the sheet as it appears in the Google Sheet document.

- `creds_id_google_drive`: This refers to the ID of the credentials JSON file that you uploaded to Google Drive. You can find the ID in the URL of the file. It is the part of the URL that comes after "/d/" and before "/view". For example, if the URL of your credentials JSON file is `https://drive.google.com/file/d/xyz987654321/view`, then the credentials ID is `xyz987654321`.

You need to ensure that the Google Sheet document and the credentials JSON file are shared with the service account email address provided in the credentials JSON file. You can find the service account email address in the "client_email" field of the JSON file.