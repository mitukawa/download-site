from typing import MappingView
from flask import Flask,render_template
from flask.helpers import send_file

MIMETYPE="application/zip"

app = Flask(__name__)
@app.route('/')
def index():
    downloadFileName = './static/orix_2019.zip'
    return send_file(downloadFileName, as_attachment=True, attachment_filename='orix_2019.zip', mimetype=MIMETYPE)

if __name__ == '__main__':
    app.run()