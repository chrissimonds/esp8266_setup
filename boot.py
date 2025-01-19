# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)       # turn off vendor O/S debugging messages
# esp.osdebug(0)          # redirect vendor O/S debugging messages to UART(0)

#os.dupterm(None, 1) # disable REPL on UART(0)
import sys
import time
import binascii
import network
wlan = network.WLAN(network.WLAN.IF_STA) # create station interface
wlan.active(True)       # activate the interface

# Load WiFi login data
from secrets import secrets

print("Welcome, here is the system info:")
print(str(sys.implementation))
print("----------")

# See the MAC address in the wireless chip OTP
mac = binascii.hexlify(network.WLAN().config("mac"), ":").decode()
print("MAC = " + mac)
print("Is WLAN connected = " + str(wlan.isconnected()))

# To make the esp8266 an acess point instead of client
# ap = network.WLAN(network.WLAN.IF_AP) # create access-point interface
# ap.active(True)         # activate the interface
# ap.config(ssid='ESP-AP') # set the SSID of the access point


print("----------")



print("WLAN Scan: ")
# print(wlan.scan())
print("#  |  SSID  |  BSSID  |  Channel  |  RSSI  |  auth_mode  |  access point count ")

# Currently last 2 values do not match documentation
# in https://docs.micropython.org/en/latest/library/network.WLAN.html
# Security/auth_mode value has a bug see:
# https://github.com/micropython/micropython/issues/10017
# Also see: https://github.com/micropython/micropython/issues/6430

accessPoints = wlan.scan() # scan for access points
# list with tuples (ssid, bssid, channel, RSSI, auth_mode,
# count of times access point name was seen)
# accessPoints.sort(key=lambda x:x[3],reverse=True) # sorted on RSSI (3)
for i, w in enumerate(accessPoints):
    print(
        i + 1,
        " | ",
        w[0].decode(),
        " | ",
        binascii.hexlify(w[1], ":").decode(),
        " | ",
        w[2],
        " | ",
        w[3],
        " | ",
        w[4],
        " | ",
        w[5],
    )
print("----------")

# Load WiFi login info from different secrets.py file for safety reasons
ssid = secrets["ssid"]
key = secrets["key"]

# To disconnect from the currently connected wireless network
# wlan.disconnect()

def do_connect():
    if not wlan.isconnected():  # check if the station is connected to an AP
        print('connecting to network...')
        wlan.connect(ssid, key) # connect to an AP
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
do_connect()

wlan_status = wlan.status()

print("WLAN Status = " + str(wlan_status))


# Display valid WLAN config parameters
print("MAC = " + str(binascii.hexlify(wlan.config("mac"), ":").decode()))
print("SSID " + str(wlan.config("essid")))
# print("WLAN Channel " + str(wlan.config("channel")))
# print("WLAN Security " + str(wlan.config("security")))
# print("TXPower " + str(wlan.config("txpower")))
print("Power Management = " + hex(wlan.config("pm")))

# Other parameters appear not fully suported yet by esp8266
# hidden - Whether SSID is hidden (boolean))
# print('Hidden ' + str(wlan.config('hidden')))
# key - Access key (string)
# print('Key ' + str(wlan.config('key')))
# reconnects - Number of reconnect attempts to make (integer, 0=none, -1=unlimited)# print (wlan.config('reconnects'))

# print (wlan.config('hostname'))
# The above line works but may be removed in future updates
# hostname - Deprecated for wlan.config so use below instead
print("Hostname = " + str(network.hostname()))
import gc
import webrepl
webrepl.start()
gc.collect()
