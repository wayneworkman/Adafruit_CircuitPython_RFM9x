# SPDX-FileCopyrightText: 2023 Your Name for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
Rx Single Mode Continuous Example for RFM9x
===========================================

This example continuously demonstrates how to use the new
receive_single() method in a loop to perform one-shot reception.
After each packet is received (or a timeout occurs), the radio automatically
returns to standby and the process repeats.
"""

import board
import busio
import digitalio
import adafruit_rfm9x

RADIO_FREQ_MHZ = 915.0

# Define pins connected to the radio.
CS = digitalio.DigitalInOut(board.D5)
RESET = digitalio.DigitalInOut(board.D6)

# Initialize the SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize the RFM9x radio.
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

while True:
    print("Waiting for a single packet (Rx Single mode)...")
    # Use the receive_single() method with a 5-second timeout.
    packet = rfm9x.receive_single(timeout=5.0)
    if packet is None:
        print("No packet received.")
    else:
        print("Received packet (raw bytes):", packet)
