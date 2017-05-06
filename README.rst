ghooks
======

Getting started
---------------

.. code:: py

    import ghooks

    @ghooks.events('push')
    def push_event(data):
        # Use/Manipulate data posted
        # Actions to take when push event is triggered

    ghooks.run()

To run the webhook:

1. To directly run(helpful while debugging stuff) ``python3 filename.py -p 5000``
2. To run the webhook with gunicorn ``gunicorn webhook:app``. Please ensure that you import the ``app`` with ``from ghooks import app``.

To create different handlers for different events:

Use ``ghooks.events`` decorator. Pass the events to be handled as arguments to
the decorator. Example:

.. code:: py

    from ghooks import app
    import ghooks

    @ghooks.events('push')
    def push_handler(data): 
        # Play with the data here

    @ghooks.events('push', 'ping')
    def push_and_ping_handler(data):
        # This will be called at both push and ping events

Installation
------------

.. code:: bash

    pip install ghooks
