import os
from flask import Flask, render_template
from livereload import Server

template_dir = os.path.dirname(__file__)
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

app.debug = True
server = Server(app.wsgi_app)

@app.route("/")
def index():
    return render_template(r'index.html')

if __name__ == "__main__":
    server.serve()