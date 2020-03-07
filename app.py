from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('data.json') as f:
    d = json.load(f)

# A welcome message to test our server
@app.route('/')
def index():
    return d

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)