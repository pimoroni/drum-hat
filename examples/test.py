import drumhat
import time

def hit_handler(event):
    print("Hit on pad: {}".format(event.pad))

def rel_handler(event):
    print("Release on pad: {}".format(event.pad))

drumhat.on_hit(drumhat.PADS, hit_handler)
drumhat.on_release(drumhat.PADS, rel_handler)

try:
    drumhat.auto_leds = False
    pads = drumhat.PADS
    while True:
        drumhat.led_on(pads[-1])
        drumhat.led_off(pads[0])
        pads.insert(0,pads.pop())
        time.sleep(0.1)

except KeyboardInterrupt:
    exit()
