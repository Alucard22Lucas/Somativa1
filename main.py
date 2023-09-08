from flask import Flask

app = Flask(__name__)

@app.route("/")

def homepage():
    return "Atividade Somativa Lucas"


app.run(debug=True)
