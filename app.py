from flask import Flask, render_template, request, send_file
from googletrans import Translator
from datetime import datetime
from gtts import gTTS
import os

app = Flask(__name__)

def translate_text(text, source_language='en', target_language='te'):
    translator = Translator(service_urls=['translate.google.com'])
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    return translated_text.text

def text_to_speech(text, lang='te', save_to_file=True, filename='output.mp3'):
    tts = gTTS(text=text, lang=lang, slow=False)

    if save_to_file:
        tts.save(filename)
        print(f'File saved as {filename}')
    else:
        tts.save('temp.mp3')
        os.system('temp.mp3')


@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']
        translated_text = translate_text(text, target_language=target_language)
        text_to_speech(translated_text, lang=target_language, filename='static/output.mp3')
        return render_template('index.html', translated_text=translated_text, audio=True, time=datetime.now().timestamp())

    return render_template('index.html', time=datetime.now().timestamp())

@app.route('/download')
def download():
    return send_file('static/output.mp3', as_attachment=True, download_name='output.mp3')


if __name__ == '__main__':
    app.run(debug=True)
