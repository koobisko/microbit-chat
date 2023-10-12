import radio, music
from microbit import *

def channelSelect():
    while True:
            try:
                channel = int(input('Channel: '))
                if 0 <= channel <= 83:
                    break
                else:
                    print("Channel must be between 0 and 83.")
                    display.show('E')
            except ValueError:
                print("Invalid channel.")
                display.show('E')
        
    radio.config(channel=channel, power=7)
    display.show(channel)
    
radio.on()

channelSelect()

while True:
    if button_a.is_pressed():
        message = input("#")
        radio.send(message)
        
    if button_b.is_pressed():
        channelSelect()
        
    received = radio.receive()
    if received:
        music.BA_DING
        print(received)
        display.scroll(received)