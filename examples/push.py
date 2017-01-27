import ghooks

@ghooks.events('push')
def push_event(data):
    print("Push event triggered!")

if __name__ == "__main__":
    ghooks.run()
