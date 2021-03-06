import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from test import GetStringFromImage

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static/img'

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST' and 'photo' in request.files:
        checkStatus = request.form['pdfCheckbox']
        print(checkStatus)
        for f in request.files.getlist('photo'):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            print('OCR..')
 
            ocrResults = GetStringFromImage(f)
            # session['ocrResults'] =  ocrResults
            return render_template('search.html', value=ocrResults, pdfStatus=checkStatus)
	        # run Erick's function here with filename (returns a cropped image)
	        # run Adam's function here with cropped image (returns an array of strings)
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        result = '[' + request.form['correction'] + ']'
        return render_template('search.html', value=result)
    return render_template('search.html')

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == "__main__":
	app.run()