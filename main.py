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

    if request.json['request']['original_utterance'].lower() in ['хватит', 'стоп']:
        response["response"]["text"] = "Очень жаль. Будет скучно обращайтесь"
        response['response']['end_session'] = True
    else:
        handle_dialog(response, request.json)

    return json.dumps(response)


def handle_dialog(res, req):
    if req['session']['new']:
        res['response']['text'] = "Привет! Я навык Бинарный поиск.\nДавай сыграем!"
    else:
        if req['request']['original_utterance'].lower() in ['давай', 'хорошо', 'ладно', 'я только за']:
            res['response']['tts'] = "Ура!!! Загадывай число а я подожду. <speaker audio=\"alice-music-drum-loop-1.opus\"> Всё... время вышло!"
            res['response']['text'] = "Ура!!! Загадывай число а я подожду. Всё, время вышло!"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)