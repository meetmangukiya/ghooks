from flask import Flask

app = Flask(__name__)

@app.get('/ghooks')
def hook():
    return "This is the hook!"

if __name__ == "__main__":
    app.run(debug=True, port=port if port else 8000)
