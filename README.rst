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

To run the webhook, ``python3 filename.py -p 5000``
