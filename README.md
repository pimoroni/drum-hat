# Drum HAT

* 8 Capacitive Touch Buttons
* Finger-friendly drum pad layout
* 8 under-mounted LEDs

# Installing Drum HAT

We've created a super-easy installation script that will install all pre-requisites and get your Drum HAT up and running in a jiffy. To run it fire up Terminal which you'll find in Menu -> Accessories -> Terminal on your Raspberry Pi desktop like so:

![Finding the terminal](terminal.jpg)

In the new terminal window type the following and follow the instructions:

```bash
curl -sSL get.pimoroni.com/drumhat | bash
```

If you choose to download examples you'll find them in `/home/pi/Pimoroni/drumhat`, but you can also check out the examples for Drum HAT in: [examples](examples)

## Manual Install

You can install Drum HAT manually like so:

```
git clone https://github.com/pimoroni/drum-hat
cd drum-hat/library
sudo python setup.py install
```

Or, for Python 3:

```
git clone https://github.com/pimoroni/drum-hat
cd drum-hat/library
sudo python3 setup.py install
```
