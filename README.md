![Drum HAT](drum-hat-logo.png)

* 8 Capacitive Touch Buttons
* Finger-friendly drum pad layout
* 8 under-mounted LEDs

Learn more: https://shop.pimoroni.com/products/drum-hat

# Installing Drum HAT

We've created a super-easy installation script that will install all pre-requisites and get your Drum HAT up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sS get.pimoroni.com/drumhat | bash
```

If you've never enabled i2c before, you should then reboot your Pi.

If you choose to download examples you'll find them in `/home/pi/Pimoroni/drumhat`, but you can also check out the examples for Drum HAT in: [examples](examples)

## Using Drum HAT

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

## Manual Install

You can install Drum HAT manually like so:

```
sudo apt-get install python-smbus
git clone https://github.com/pimoroni/drum-hat
cd drum-hat/library
sudo python setup.py install
```

Or, for Python 3:

```
sudo apt-get install python3-smbus
git clone https://github.com/pimoroni/drum-hat
cd drum-hat/library
sudo python3 setup.py install
```

In both cases you will have to enable i2c in `raspi-config`.
