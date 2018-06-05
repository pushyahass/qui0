import os, csv
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    loc1 = os.path.join(APP_ROOT, 'orig/')
    print(loc1)

    if not os.path.isdir(loc1):
        os.mkdir(loc1)

    for file in request.files.getlist("file"):
        print (file)
        filename = file.filename
        dest_loc1 = "/".join([loc1, filename])
        print(dest_loc1)
        file.save(dest_loc1)

    return render_template("success.html")

@app.route("/upload_dups", methods=['POST'])
def upload_dups():
    loc2 = os.path.join(APP_ROOT, 'dups/')
    print(loc2)

    if not os.path.isdir(loc2):
        os.mkdir(loc2)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        dest_loc2 = "/".join([loc2, filename])
        print(dest_loc2)
        file.save(dest_loc2)

    return render_template("success.html")

if __name__ == '__main__':
    app.run()
