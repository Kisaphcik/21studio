from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def main():
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }

    handle_dialog(response, request.json)
    return json.dumps(response)


def handle_dialog(res, req):
    if req["session"]["new"]:
        req["response"]["text"] = "Привет"
    else:
        if req["request"]["original_utterance"].lower() == "привет":
            req["response"]["text"] = "Как дела?"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)