#!/usr/bin/env python

import time
import pygame

import drumhat

print("""This example lets you trigger samples.

They can either be loops, or single-shot samples.

Press CTRL+C to exit!
""")

drumhat.auto_leds = False

pygame.mixer.init(44100, -16, 1, 512)
pygame.mixer.set_num_channels(8)

class Sample():
    def __init__(self, channel_index, filename, volume=1.0, loops=0, sync=False):
        self.volume = volume
        self.loops = loops
        self.sync = sync
        self.filename = filename
        self.sound = pygame.mixer.Sound(filename)
        self.channel = pygame.mixer.Channel(channel_index)

    def busy(self):
        if self.sync:
            return self.channel.get_volume() > 0

        return self.channel.get_busy()

    def toggle(self):
        if self.sync and self.busy():
            self.stop()
            return False
        else:
            self.play()
            return True

    def start(self):
        if self.sync:
            self.channel.set_volume(0)
            self.channel.play(self.sound, loops=-1)
        else:
            self.channel.set_volume(self.volume)

    def stop(self):
        if self.sync:
            self.channel.set_volume(0)

    def play(self):
        if self.sync:
            self.channel.set_volume(self.volume)
        else:
            self.channel.play(self.sound, loops=self.loops)

"""
Change your sample selection below.

If you want loops to start playing when the script launches and
stay syncronised then set sync=True.

Fine tune your sample balance with volume=N

You can also specify the number of loops a triggered sample
should play for with loops=N. A value of 1 will cause the
sample to play twice.
"""
samples = [
    Sample(0, "loops/fn-melody.ogg", sync=True),
    Sample(1, "loops/fn-bass.ogg", sync=True, volume=0.8),
    Sample(2, "loops/fn-percussion.ogg", sync=True),
    Sample(3, "drums/crash.wav", sync=False),
    Sample(4, "drums/thud.wav", sync=False),
    Sample(5, "drums/clap.wav", sync=False),
    Sample(6, "drums/smash.wav", sync=False),
    Sample(7, "drums/rim.wav", sync=False)
]

def handle_hit(event):
    # event.channel is a zero based channel index for each pad
    # event.pad is the pad number from 1 to 8
    try:
        sample = samples[event.channel]
        if sample.toggle():
            drumhat.led_on(event.pad)
            print("Playing: {}".format(sample.filename))
        else:
            drumhat.led_off(event.pad)
            if sample.sync:
                print("Stopping: {}".format(sample.filename))

    except IndexError:
        print("Error: No sound mapped for {}".format(event.channel))
        pass

def main():
    drumhat.all_off()

    for sample in samples:
        sample.start()

    drumhat.on_hit(drumhat.PADS, handle_hit)

    while True:
        for channel, sample in enumerate(samples):
            if not sample.sync and not sample.busy():
                drumhat.led_off(drumhat.NUMMAP[channel])
            
        time.sleep(1.0 / 30)


if __name__ == "__main__":
    main()
