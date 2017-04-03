## Drum HAT Function Reference

The pads on Drum HAT are laid out like so:

```
7    1    2
6    8    3
  5    4
```

Drum HAT can call a function when a pad is hit, or when it is released. For example, to do something when the middle pad (number 8) is hit, you should:

```python
import drumhat

@drumhat.on_hit(8)
def middle_pad():
    print("Middle Pad Hit!")
```

If you want to control the LED underneath a specific pad, you can turn it on or off like so:

```
drumhat.led_on(8)  # Turn on the middle pad LED
drumhat.led_off(8) # Turn off the middle pad LED
```

Or you can turn them all on/off like so:

```
drumhat.all_on()
drumhat.all_off()
```

You can optionally disable DrumHAT's automatic LED control like so:

```
drumhat.auto_leds = False
```
