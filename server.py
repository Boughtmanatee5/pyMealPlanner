from flask import Flask, request

app = Flask(__name__, static_url_path='');

@app.route('/')
def index():
    return "hello app"

if __name__ == "__main__":
    app.run()
