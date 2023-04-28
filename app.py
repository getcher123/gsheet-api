from flask import Flask, make_response, request, jsonify
from flask_cors import CORS


from GoogleSheetDataFrame import GoogleSheetDataFrame
from utils.downloadGD import download_google_drive_json_file

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run()
    
@app.route('/', methods=['GET'])
def getData():
        request_data = request.get_json()
        document_key = request_data["doc_key"]
        sheet = request_data["sheet"]
        creds_id_google_drive = request_data["creds_id"]
        json_data = download_google_drive_json_file(creds_id_google_drive)
        result = GoogleSheetDataFrame(json_data, document_key, sheet)
        result = result.to_json(orient='records')
        headers = {}
        headers['Content-Type'] = 'application/json'
        headers['Access-Control-Allow-Origin'] = '*'
        return result, 200, headers



