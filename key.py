import wiringpi

# http://www.spotpear.net/download/image/RPi-1.54inch-LCD/raspbian-image/1.54inchlcd-key-test/key.c
# keys = [4,9,15,16,21,22,23,24,25,26,27,28,29]
keys = {
    'tl': 4,
    'press': 9,
    'tr': 15,
    'x': 16,
    'up': 21,
    'right': 22,
    'left': 23,
    'start': 24,
    'select': 25,
    'y': 26,
    'down': 27,
    'b': 28,
    'a': 29
}
wiringpi.wiringPiSetup()

for key in keys:
    wiringpi.pinMode(keys[key], wiringpi.GPIO.INPUT)
    wiringpi.pullUpDnControl(keys[key], wiringpi.GPIO.PUD_UP)

while True:
    for key in keys:
        if wiringpi.digitalRead(keys[key]) == 0:
            print('press:', key)
