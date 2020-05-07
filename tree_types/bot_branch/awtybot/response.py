#!/usr/local/bin/python3

import callhome

def response():
    answer = input("would you like to send a tweet today?")
    if answer == 'yes' or "Yes":
        
        callhome.update_status()
    elif answer == 'no' or 'NO':
        print("continue on")
    else:
        print("response not accecpted")

response()
