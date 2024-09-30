from flask import Flask

app = Flask(__name__)

@app.route('/')
def msg():
    return "This is a simple APP! Running in ArgoCD!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')