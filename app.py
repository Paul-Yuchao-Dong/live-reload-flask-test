import os
from flask import Flask, render_template

template_dir = os.path.dirname(__file__)
template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    return render_template(r'index.html')

if __name__ == "__main__":
    app.run()