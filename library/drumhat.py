import cap1xxx
import time

dh = cap1xxx.Cap1188(
    i2c_addr=0x2c,
    alert_pin=25)

LEDMAP = [
    5,
    4,
    3,
    2,
    1,
    0,
    6,
    7
]

_on_press = [None] * 8
_on_release = [None] * 8

def on_hit(channel, handler=None):
    global _on_presss
    if handler is None:
        def decorate(handler):
            global _on_press
            _on_press[channel] = handler
        return decorate
    _on_press[channel] = handler 

def on_release(channel, handler=None):
    global _on_release
    if handler is None:
        def decorate(handler):
            global _on_release
            _on_release[channel] = handler
        return decorate
    _on_release[channel] = handler

def handle_press(event):
    global _on_press
    dh.set_led_state(LEDMAP[event.channel], True)
    if event.channel in _on_press and callable(_on_press[event.channel]):
        _on_press[event.channel]

def handle_release(event):
    global _on_release
    dh.set_led_state(LEDMAP[event.channel], False)
    if event.channel in _on_release and callable(_on_release[event.channel]):
        _on_release[event.channel]

for x in range(8):
    dh.on(x,event='press',   handler=handle_press)
    dh.on(x,event='release', handler=handle_release)

"""
Unlink the LEDs since Drum HAT's LEDs don't match up with the channels
"""
dh._write_byte(cap1xxx.R_LED_LINKING, 0b00000000)
