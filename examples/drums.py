#!/usr/bin/env python

import drumhat
import time
import pygame
import os
import glob

DRUM_FOLDER = "drums2"

print("""This example lets you play the drums with Drum HAT!

Pads are mapped like so:

7 = Rim hit, 1 = Whistle, 2 = Clash
6 = Hat,     8 = Clap,   3 = Cowbell
      5 = Snare,   4 = Base

Press CTRL+C to exit!
""")

BANK = os.path.join(os.path.dirname(__file__), DRUM_FOLDER)

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(16)

files = glob.glob(os.path.join(BANK, "*.wav"))
files.sort()

samples = [pygame.mixer.Sound(f) for f in files]

def handle_hit(event):
    # event.channel is a zero based channel index for each pad
    # event.pad is the pad number from 1 to 8
    samples[event.channel].play(loops=0)
    print("You hit pad {}, playing: {}".format(event.pad,files[event.channel]))

def handle_release():
    pass

drumhat.on_hit(drumhat.PADS, handle_hit)
drumhat.on_release(drumhat.PADS, handle_release)
 
while True:
    time.sleep(1)
