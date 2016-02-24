#!/usr/bin/env python

import cap1xxx
import time
import pygame
import os
import glob

"""

4 3 2
5 7 1
 6 0

"""

BANK = os.path.join(os.path.dirname(__file__), "drums2")

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(16)

files = glob.glob(os.path.join(BANK, "*.wav"))
files.sort()

print(files)
samples = [pygame.mixer.Sound(f) for f in files]

dh = cap1xxx.Cap1188(
    i2c_addr=0x2c,
    alert_pin=25)

ledmap = [
    5,
    4,
    3,
    2,
    1,
    0,
    6,
    7
]

state = [True] * 8

def handle_press(event):
    print(event.channel)
    samples[event.channel].play(loops=0)
    print(files[event.channel])
    dh.set_led_state(ledmap[event.channel], True)

def handle_release(event):
    dh.set_led_state(ledmap[event.channel], False)

for x in range(8):
    dh.on(x,event='press',   handler=handle_press)
    dh.on(x,event='release', handler=handle_release)

dh._write_byte(cap1xxx.R_LED_LINKING, 0b000000)

while True:
    #state = [not s for s in state]
    #for x in range(8):
    #    dh.set_led_state(x, True)
    #    time.sleep(0.2)
    #    dh.set_led_state(x, False)
    #    time.sleep(0.2)

    time.sleep(1)
