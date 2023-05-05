from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return 안녕하세요 #render_template('./index.html')
