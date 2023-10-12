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
    
# Start the radio module
radio.on()

channelSelect()


while True:
    if button_a.is_pressed():
        # Get a message from the user
        message = input("#")

        # Send the message
        radio.send(message)
    if button_b.is_pressed():
        channelSelect()
        
    # Continuously check for an incoming message
    received = radio.receive()
    if received:
        music.BA_DING
        print(received)
        display.scroll(received)