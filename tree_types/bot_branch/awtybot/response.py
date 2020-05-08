#!/usr/local/bin/python3

import callhome

def response():
    answer = input("would you like to send a tweet today?")
    if answer.lower() in 'yeah yes yep yea yup'.split():
        print('you typeed', answer)
        callhome.update_status()
        # checking()
        #maybe add another function for something?
    elif answer == 'no' or 'NO':
        print("continue on")
        # checking()
    else:
        print("response not accecpted")

def main():
    response()

if __name__ == "__main__":
    main()