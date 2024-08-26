from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():

    return "ESTE MEU SITE TESTE"


if __name__ == '__main__':
    app.run(debug=True)