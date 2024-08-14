from flask import Flask, render_template, request
from google.cloud import translate_v2 as translate
import os

app = Flask(__name__)

# Verify the environment variable
credentials_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
if not credentials_path:
    raise EnvironmentError('GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.')

# Initialize the translate client
translate_client = translate.Client()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        target_language = request.form['language']
        translated_text = translate_client.translate(text, target_language=target_language)['translatedText']
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)

