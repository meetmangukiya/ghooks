EVENTS = {
    "commit_comment": [],
    "create": [],
    "delete": [],
    "deployment": [],
    "deployment_status": [],
    "fork": [],
    "gollum": [],
    "issue_comment": [],
    "issues": [],
    "label": [],
    "member": [],
    "membership": [],
    "milestone": [],
    "organization": [],
    "page_build": [],
    "project_column": [],
    "project": [],
    "public": [],
    "pull_request_review_comment": [],
    "pull_request_review": [],
    "pull_request": [],
    "push": [],
    "repository": [],
    "release": [],
    "status": [],
    "team": [],
    "team_add": [],
    "watch": []
}

def events(*args, **kwargs):
    def wrapper(func):
        for event in args:
            if event in EVENTS:
                EVENTS[event].append(func)
            else:
                raise ValueError("Unrecognized event")
        return func
    return wrapper

def call_handlers(data, event):
    for handlers in EVENTS[event]:
        handlers(data)

from ghooks.hooks import run
