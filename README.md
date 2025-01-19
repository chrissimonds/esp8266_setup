# esp8266_setup
WiFi configuration setup for MicroPython on ESP-01S but code should work on most ESP8266 variants

This is using MicroPython v1.24.1 and spefically the 1MiB flash version.
https://micropython.org/download/ESP8266_GENERIC/

The 1MiB load does have some limitations but the ESP-01s is widely available, very small, very cheap and great for simple projects.

For more information see:
https://docs.micropython.org/en/latest/esp8266/quickref.html

Also note, this code assumes that initial webrepl setup was done via:
import webrepl_setup

Please see this link for details:
https://docs.micropython.org/en/latest/esp8266/quickref.html#webrepl-web-browser-interactive-prompt

