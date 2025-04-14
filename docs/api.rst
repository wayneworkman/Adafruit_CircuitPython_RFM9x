
.. If you created a package, create one automodule per module in the package.

.. If your library file(s) are nested in a directory (e.g. /adafruit_foo/foo.py)
.. use this format as the module name: "adafruit_foo.foo"

.. automodule:: adafruit_rfm9x
   :members:

.. currentmodule:: adafruit_rfm9x

New in this Release: Rx Single Mode
====================================

The :meth:`~adafruit_rfm9x.RFM9x.receive_single` method has been added to enable a one-shot reception mode.
In this mode the radio is configured to receive a single packet and then automatically switches to standby.

**Parameters:**

- **with_header** (bool): If True, the returned packet includes the 4-byte RadioHead header.
- **with_ack** (bool): If True, an ACK is sent on receipt (for reliable datagram mode).
- **timeout** (Optional[float]): Maximum time in seconds to wait for a packet. Defaults to the object's
  ``receive_timeout`` value.

**Returns:**

- A bytearray containing the received packet (with header stripped unless ``with_header`` is True), or
  ``None`` if no packet is received within the timeout.
