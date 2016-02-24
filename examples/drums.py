#!/usr/bin/env python

import drumhat
import time
import pygame
import os
import glob

DRUM_FOLDER = "drums2"

print("""This example lets you play the drums with Drum HAT!

Pads are mapped like so:
4 3 2
5 7 1
 6 0

4 = Rim hit, 3 = Whistle, 2 = Clash
5 = Hat, 7 = Clap, 1 = Cowbell
6 = Snare, 0 = Base

Press CTRL+C to exit!
""")

BANK = os.path.join(os.path.dirname(__file__), DRUM_FOLDER)

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(16)

files = glob.glob(os.path.join(BANK, "*.wav"))
files.sort()

samples = [pygame.mixer.Sound(f) for f in files]

def handle_hit(event):
    samples[event.channel].play(loops=0)
    print("You hit channel {}, playing: {}".format(event.channel,files[event.channel]))

def handle_release():
    pass

for x in range(8):
    drumhat.on_hit(x, handle_hit)
    drumhat.on_release(x, handle_release)
 
while True:
    time.sleep(1)

