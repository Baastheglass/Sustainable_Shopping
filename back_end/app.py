from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {
        "message": "This is a placeholder response. Implement your scraping logic here."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)