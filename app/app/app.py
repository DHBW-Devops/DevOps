from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from prometheus_flask_exporter import PrometheusMetrics
import os, re

app = Flask(__name__)
PrometheusMetrics(app)
imageLoaded = False

@app.route('/')
def index():
    imageLoaded = False
    print('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    imageLoaded = False
    name = remove_special_characters(f"{request.form.get('name')}")
    if name_is_valid(name):
        print('Request for hello page received with name=%s' % name)
        return render_template('hello.html', name = name)
    else:
        print('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))

def remove_special_characters(name):
    pattern = re.compile('[^a-zA-Z0-9 ]')

    return pattern.sub("", name)

def name_is_valid(name: str) -> bool:
    return name and "".join(name.split()).isalnum()

def image_loaded():
    imageLoaded = True
    print("fasdf")

if __name__ == '__main__':
    app.run()#100 - (avg(irate(node_cpu_seconds_total{mode="idle"}[30m])) * 100)