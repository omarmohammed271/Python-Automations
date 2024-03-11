import pywhatkit
import time

# Phone number (with country code) of the recipient
phone_number = '+2001283133302'
phone_numbers = ['+2001283133302','+2001028227167',]
# Message you want to send
message = "Hello, this is a test message sent using Python!"


# Specify the time to send the message (24-hour format)
hour = 15
minute = 19

# Send the message
for number in phone_numbers:
    # pywhatkit.sendwhatmsg(number, message, hour, minute)
    pywhatkit.sendwhatmsg_instantly(number, message)
    time.sleep(15)
print('Done')