import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', '-p', type=int)

args = parser.parse_args()

import os

from ghooks import EVENTS, call_handlers

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/ghooks')
def hook(methods=["POST"]):
    gh_event = request.headers.get('X-GitHub-Event')
    gh_signature = request.headers.get('X-Hub-Signature')
    gh_id = request.headers.get('X-GitHub-Delivery')

    data = request.form

    call_handlers(data, gh_event)

def run():
    app.run(debug=True, port=args.port if args.port else 8000)

if __name__ == "__main__":
    main()
