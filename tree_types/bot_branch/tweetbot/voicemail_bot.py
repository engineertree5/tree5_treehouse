#!/usr/local/bin/python3

# v.4
#### Breakout spotify module to another file
import random
import tweepy
from secrets import *
from time import sleep
######spotipy stuff
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# twitter requires all request to use OAuthhandler for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
###### SPOTIPY #######
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
######################

# constructing API instance
api = tweepy.API(auth)
user = api.get_user('lordfili')
old_tweet = []
twitter_fan = "MisterFili"
cheapDB = "/Users/MisterFili/Documents/github_projects/tweetbot/basiclist.txt"

def tweetcheck(tweet_id, screenname, msg):

    with open(cheapDB, 'r') as file:
            rd = file.read().splitlines()
            # using the enumerate method we can create an indexed list
            # we then seperate the count(i) and value(line) and look to see
            # if tweet_id is found in the file. if so, ignore the tweet
            for i, line in enumerate(rd):
                if tweet_id == line:
                    old_tweet.append(tweet_id)
                    continue
            if tweet_id in old_tweet:
                print(f"old tweet from: @{screenname}")
                # continue
            else:
                with open(cheapDB, "a") as f:
                #if tweet_id exist in file skip writing to file
                #else write to file
                    f.write(f"{tweet_id}\n")
                    print(f"\nNew Tweet found\nAdding tweet id: {tweet_id} to file for tracking")
                    print("\n####\nUPDATING STATUS\n####")
                    print(f"\nRESPONDING TO TWEET")
                    print(msg)
                    # api.update_status(status=msg, in_reply_to_status_id=tweet_id)
                    return 0
                    
def OOTO():
    
    search_for = "@MisterFili"
    tweets_mentioned = 2

    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            screenname = tweet.user.screen_name
            tweet_id = tweet.id_str
            msg = f"@{screenname} Seems that you are looking for my creator, Monsieur Fili. He is currently Out of the office... May I help you with some music in his absence? Reply to me with an artist name wrapped in double quotes \"artist name\""
        
        #look at previously tweeted user @ names. If name is within last 5 @'s respond a certain way
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
        if tweetcheck(tweet_id, screenname, msg) == 0:
            print(f"@{screenname} said:\n{tweet.text} \n")
            print("Status Updated")
        else:
            print("\nAlready responsed to this tweet. BYE!")
        

def artist_info():
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API
    album_coverart = []
    album_names = []
    album_hyperlinks = []
    search_for = "@FiliTheTester"
    tweets_mentioned = 8

    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            print("######\nLOOP START\n####")
            screenname = tweet.user.screen_name
            tweet_id = tweet.id_str
            raw_user_response = tweet.text
            #There was a set of "special quotes" being returned from the user response
            #Replacing special quotes with standard double quotes
            special_quote1 = str(raw_user_response).replace("“", '"')
            user_response = str(special_quote1).replace("”", '"')
            # The split() method splits a string into a list.
            # the [1::2] is a slicing which extracts odd values | pull everything between double quotes
            response_list = user_response.split('"')[1::2]   
            print(f"User is looking for {response_list}")

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
            
        if len(response_list) == 1:
            no_list = " "
            user_artist = no_list.join(response_list)
            print(f'searching for an album from {user_artist}. Hang tight, {screenname}!\n')

        elif len(response_list)  == 0 :
            print(f'user tweeted:\n{user_response}')
            msg = f'@{screenname} did not wrap the response in quotes. No artist found'
            print(msg)
            if tweetcheck(tweet_id, screenname, msg) == 0:
                print(f"@{screenname} said:\n{tweet.text} \n")
                print("Status Updated")
            else:
                print("\nAlready responsed to this tweet. BYE!")
            continue

        elif len(response_list) > 2:
            print(f'user tweeted:\nf{user_response}')
            msg = f'I can only search 1 artist at a time, @{screenname}. The next version of me will be better'
            if tweetcheck(tweet_id, screenname, msg) == 0:
                print(f"@{screenname} said:\n{tweet.text} \n")
                print("Status Updated")
            else:
                print("\nAlready responsed to this tweet. BYE!")            
            print(msg)
            continue
        ### return a random artist album, link, and image
        result = sp.search(user_artist) #search query name var
        #Extract Artist's uri
        artist_name = result['tracks']['items'][0]['artists'][0]['name']
        artist_uri = result['tracks']['items'][0]['artists'][0]['uri']
        #Pull all of the artist's albums
        
        album_uris = []
        print("\n\n")
        #while loop to check if artist name matches properly
        count = 0
        print(f"ARTIST NAME: {artist_name}\nUSER ARIST {user_artist}\n")
        try:
            while artist_name.lower() != user_artist.lower():
                count = count + 1 
                print(f"not track{count}")
                print("printing count", count)
                tempname = result['tracks']['items'][count]['artists'][0]['name']
                artist_name = tempname.lower()
                print(f"{artist_name} does not match {user_artist}")
                artist_uri = result['tracks']['items'][count]['artists'][0]['uri']

                if count > 10:
                    msg = f"{screenname} There was an issue processing your request. Try again later."
                    if tweetcheck(tweet_id, screenname, msg) == 0:
                        print(f"@{screenname} said:\n{tweet.text} \n")
                        print("Status Updated")
                    else:
                        print("\nAlready responsed to this tweet. BYE!")
                    # with open(cheapDB, 'r') as file:
        except IndexError as e:
                error = e
                error_status_update = f"@{screenname} There was a problem on the back end... \"{error}\".\nsearching for {user_artist} but found {artist_name}. New feature(s) to handles this coming soon!"
                ######## WRITE TO DB FUNCTION
                # api.update_status(status=error_status_update, in_reply_to_status_id=tweet.id)
                print(error_status_update)
                pass    

        print(f"\tEXITED WHILE LOOOP\n ARTIST IS {artist_name}")
        sp_albums = sp.artist_albums(artist_uri, album_type='album')
        for i in range(len(sp_albums['items'])):
            try:
                album_names.append(sp_albums['items'][i]['name'])
                album_uris.append(sp_albums['items'][i]['uri'])        
                album_coverart.append(sp_albums['items'][i]['images'][0]['url'])
                album_hyperlinks.append(sp_albums['items'][i]['external_urls']['spotify'])
            except IndexError as e:
                print(e)
                continue
        hyperlink_list = []
        list_album_names = []
        # print(random.choice(album_coverart))
        for i in album_names:
            list_album_names.append(i)
        for i in album_hyperlinks:
            try:
                hyperlink_list.append(i)
            except IndexError as e:
                print(e)
                break

        random_selection = random.choice(hyperlink_list)
        if artist_name.lower() == user_artist.lower():
            print(f"artist name: {artist_name}\nuser_artist: {user_artist}")
            msg = f"@{screenname} Here is something you can listen to from {user_artist} while you wait. {random_selection}"
            print(msg)
            continue
        else:
            pass
        if tweetcheck(tweet_id, screenname, msg) == 0:
            print(f"@{screenname} said:\n{tweet.text} \n")
            print("Status Updated")
        else:
            print("\nAlready responsed to this tweet. BYE!")
        # with open(cheapDB, 'r') as file:
def main():
    artist_info()

if __name__ == "__main__":
    main()