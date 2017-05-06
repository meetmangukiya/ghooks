import argparse

# Only do argument parsing if run directly, otherwise gunicorn doesn't work
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', '-p', type=int)
    parser.add_argument('--end-point', '--end', '-e')

    args = parser.parse_args()

args = {}

import os

from ghooks import EVENTS, call_handlers

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/' + (args.get("end_point") if args.get("end_point") else 'ghooks'), methods=["POST"])
def hook():
    gh_event = request.headers.get('X-GitHub-Event')
    gh_signature = request.headers.get('X-Hub-Signature')
    gh_id = request.headers.get('X-GitHub-Delivery')

    data = request.form

    call_handlers(data, gh_event)

if __name__ == "__main__":
    app.run(degug=True, host='127.0.0.1', port=args.get('port') if
                                               args.get('port') else 8080)
