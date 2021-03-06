from network import LoRa
import socket
import machine
import time

# initialize LoRa in LORA mode
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
# more params can also be given, like frequency, tx power and spreading factor
lora = LoRa(mode=LoRa.LORA, bandwidth=LoRa.BW_250KHZ, tx_power=14, sf=12, region=LoRa.EU868)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

while True:
    # send some data
    s.setblocking(True)
    s.send('Hello Gugu, transmitting from Home!')



    # wait a random amount of time
    time.sleep(machine.rng() & 0x05)
