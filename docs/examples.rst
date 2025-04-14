Simple test
------------

Ensure your device works with this simple test.

.. literalinclude:: ../examples/rfm9x_simpletest.py
    :caption: examples/rfm9x_simpletest.py
    :linenos:

Rx Single Mode Example
-----------------------

The following example demonstrates how to use the new
:func:`~adafruit_rfm9x.RFM9x.receive_single` method to perform a one-shot reception.
After a packet is received (or the timeout expires), the radio automatically goes to standby.

.. literalinclude:: ../examples/rfm9x_rx_single.py
    :caption: examples/rfm9x_rx_single.py
    :linenos:
