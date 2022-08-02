from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fewfewf56482fwefds48ght'

Bootstrap(app)

@app.route("/home")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999)
