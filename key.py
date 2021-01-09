import wiringpi

# http://www.spotpear.net/download/image/RPi-1.54inch-LCD/raspbian-image/1.54inchlcd-key-test/key.c
keys = [4,9,15,16,21,22,23,24,25,26,27,28,29]
wiringpi.wiringPiSetup()

for key in keys:
    wiringpi.pinMode(key, wiringpi.GPIO.INPUT)
    wiringpi.pullUpDnControl(key, wiringpi.GPIO.PUD_UP)

while True:
    for key in keys:
        if wiringpi.digitalRead(key) == 0:
            print('press: ', key)
