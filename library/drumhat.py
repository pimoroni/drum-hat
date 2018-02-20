import time
from sys import exit

try:
    import cap1xxx
except ImportError:
    raise ImportError("This library requires the cap1xxx module\nInstall with: sudo pip install cap1xxx")

__version__ = '0.1.0'

dh = None

auto_leds = True

PADS = list(range(1,9))

LEDMAP = [
    5, 4, 3, 2,
    1, 0, 6, 7
]

NUMMAP = [
    4, 3, 2, 1, 
    7, 6, 5, 8
]

_on_press = [None] * 8
_on_release = [None] * 8
_is_setup = False

def on_hit(pad, handler=None):
    """Register a function to be called when a pad or pads are hit.

    The function should expect one argument: event. You can look at event.pad to determine which pad was hit.

    :param pad: A single integer from 0 to 7, or a list of integers
    :param handler: The handler function to call on hit
    """
    global _on_press

    setup()

    if type(pad) == list:
        for ch in pad:
            on_hit(ch, handler)
        return

    try:
        channel = NUMMAP.index(pad)
    except ValueError:
        raise TypeError("Invalid drum pad #{}".format(pad))

    if handler is None:
        def decorate(handler):
            global _on_press
            _on_press[channel] = handler
        return decorate

    _on_press[channel] = handler 

def on_release(pad, handler=None):
    """Register a function to be called when a pad or pads are released.

    The function should expect one argument: event. You can look at event.pad to determine which pad was released.

    :param pad: A single integer from 0 to 7, or a list of integers
    :param handler: The handler function to call on release
    """
    global _on_release

    setup()

    if type(pad) == list:
        for ch in pad:
            on_release(ch, handler)
        return

    try:
        channel = NUMMAP.index(pad)
    except ValueError:
        raise TypeError("Invalid drum pad #{}".format(pad))

    if handler is None:
        def decorate(handler):
            global _on_release
            _on_release[channel] = handler
        return decorate

    _on_release[channel] = handler

def _handle_press(event):
    global _on_press
    channel = event.channel
    event.pad = NUMMAP[channel]

    if auto_leds:
        dh.set_led_state(LEDMAP[channel], True)

    if callable(_on_press[channel]):
        try:
            _on_press[channel](event)
        except TypeError:
            _on_press[channel]()

def _handle_release(event):
    global _on_release
    channel = event.channel
    event.pad = NUMMAP[channel]

    if auto_leds:
        dh.set_led_state(LEDMAP[channel], False)

    if callable(_on_release[channel]):
        try:
            _on_release[channel](event)
        except TypeError:
            _on_release[channel]()

def led_on(pad):
    """Turn on an LED corresponding to a single pad.

    :param pad: A single integer from 0 to 7, corresponding to the pad whose LED you want to turn on.
    """

    setup()

    idx = -1

    try:
        idx = NUMMAP.index(pad)
    except ValueError:
        raise TypeError("Invalid drum pad #{}".format(pad))

    led = LEDMAP[idx]
    dh.set_led_state(led, True)

def all_off():
    """Turn off all LEDs"""

    setup()

    for pad in PADS:
        led_off(pad)

def all_on():
    """Turn on all LEDs"""

    setup()

    for pad in PADS:
        led_on(pad)

def led_off(pad):
    """Turn off an LED corresponding to a single pad.

    :param pad: A single integer from 0 to 7, corresponding to the pad whose LED you want to turn off.
    """
    setup()

    idx = -1

    try:
        idx = NUMMAP.index(pad)
    except ValueError:
        raise TypeError("Invalid drum pad #{}".format(pad))

    led = LEDMAP[idx]
    dh.set_led_state(led, False)

def setup():
    global dh, _is_setup

    if _is_setup:
        return True

    dh = cap1xxx.Cap1188(
        i2c_addr=0x2c,
        alert_pin=25)

    for x in range(8):
        dh.on(x,event='press',   handler=_handle_press)
        dh.on(x,event='release', handler=_handle_release)

    """Unlink the LEDs since Drum HAT's LEDs don't match up with the channels"""
    dh._write_byte(cap1xxx.R_LED_LINKING, 0b00000000)

    _is_setup = True

