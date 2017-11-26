# https://github.com/olemb/mido
# https://github.com/SpotlightKid/python-rtmidi

import time
start = time.time()
import mido
import rtmidi
from mido import Message
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--fuzz")
parser.add_argument("--od")
parser.add_argument("--phaser")
parser.add_argument("--amp")

args = parser.parse_args()

print (args.fuzz)


# open midi ports, etc.
#port_index = out_ports.index('Bome MIDI Translator 1 2')
port = mido.open_output("Bome MIDI Translator 1 2")


def m(cc, val):
    return mido.Message("control_change", control=cc, value=val, channel=1)

def send(cc, val):
    port.send(m(cc, val))
    time.sleep(0.01)

# write midi messages based on args

if args.fuzz:
    send(14, 127)
else:
    send(14, 0)

if args.od:
    send(15, 127)
else:
    send(15, 0)

if args.phaser:
    send(16, 127)
else:
    send(16, 0)

if args.amp == '1':
    send(20, 0)
    print("amp #1")
elif args.amp == '2':
    send(20, 2)
    print ("amp #2")

print (args)

port.close()

end = time.time()
print (end - start)


