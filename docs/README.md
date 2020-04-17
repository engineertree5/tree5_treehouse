# Treehouse5 - Working With GeekTools

## Desktop WallPaper

<figure>
    <img src="media/img/desktopshot.jpeg" alt="Screenshot of Desktop" title="My Desktop">
</figure>

**REQUIREMENTS (Mac OSX)**
* A working computer with macOS installed
* [GeekTool](https://www.tynsoe.org/v2/geektool/documentation/)
* basic understanding of the mac terminal
* Willingness to fail & learn

To duplicate the screenshot above you will first need to download and install [GeekTool](https://www.tynsoe.org/v2/geektool/documentation/). Geektool is a macOS application that will let you customize your desktop in a few different ways. You can keep it simple with the date and time or get complex and show how many CPU cores your computer is using at the current time. Whichever pace you move, Geektool is a great way to learn scripting or just improve your desktop cosmetics. 

Lets get started with the basics and iterate our way through until the end. 

The wallpaper was created using Photoshop and the image came from [Mustafah Abdulaziz](http://www.mustafahabdulaziz.com). If you'd like to use this wallpaper you can download it [here](https://imgur.com/a/iwlS20G)

## Date & Uptime

?> Vist [GeekTool](https://www.tynsoe.org/v2/geektool/documentation/) for the quick start guide or follow along by using your mac terminal

The day and date was generated using shell commands via the terminal. Every mac comes with the terminal already installed, so if you are using a mac you are good to go (sorry, windows users). To get your terminal open, search for `terminal` under your applications or through finder. Once you have your terminal open type in the following:

?> The `$` represents the start of a new line within the terminal. DO NOT COPY/TYPE THE `$`

```bash
    $ date '+%A %d'
```
This should display the day and then the date. Try changing the `A` to lowercase and see what happens. Have fun and experiment with different combinations. If you are curious and would like to try more date combinations. I would recommend reading over the `man page` for date. type the following to get to the man page:

```bash
    $ man date
```

use the arrow keys or spacebar to scroll the page
q - to quit

# Computer Uptime {docsify-ignore}

You will need to be familiar with the shell command `awk`- can do simple text replacements and much more advanced parsing. However, we will need to combine the `sub()` function with `regular expressions` to manuipulate the output we get from `uptime`.

the below command is what I used display how long the system has been running:

```bash
     $ uptime | awk '{sub(/[0-9]|user\,|users\,|load/, "", $6); sub(/mins,|min,/, " min", $6); sub(/user\,|users\,/, "", $5); sub(",", " min", $5); sub(":", "h ", $5); sub(/[0-9]/, "", $4); sub(/day,/, " day ", $4); sub(/days,/, " days ", $4); sub(/mins,|min,/, "min", $4); sub("hrs,", "h", $4); sub(":", "h ", $3); sub(",", "min", $3); print "Uptime: " $3$4$5$6}'
```

lets break it down this command -

`uptime` - Print how long the system has been running 

```bash
    Example: from your terminal run the below cmd:
    $ uptime
```

*from the uptime man page* - The uptime utility displays the current time, the length of time the system has been up, the number of users, and the load average of the system over the last 1, 5, and 15 minutes.

` | ` - (pipe) each command in a pipeline is executed as a seperate process

`awk` - pattern scanning and processing.

    Example: column selection with awk. 
    echo "Testing Treehouse cmds" | awk '/cmds/{print $2}'

`sub` - string subsistution function. we are omitting and subsistuting text from the uptime command so we can display the text to our liking 

    Template for sub() function:
    sub(regexp,replstring,mystring)

Using the `uptime` command we are able to print how long the system has been running. We then `pipe` that output into an `awk` command where we are only looking for values in columns [3-6]. For each of those colums we use the `sub()` function to remove text that is not necessary, such as `:` and `,`.

## PKC

Sooooo PKC is the shit! You get TWO EXTREMELY LONG prime numbers - these are going to be your private keys - and combine them. Those combined prime numbers will be your public key. So, now you can assign that prime number to a txt message. Then send it out into the wild, across the internet, into your receivers hands safely. Ah! But keep in mind that in order to read (decrypt) the txt message you need th other large prime number to read it. If another person try’s to read your message they will need the other large prime number (private key) to decrypt the message.... fuckin’ PKC. Cool shit

## Tweepy

> I'm assuming you have a basic understanding of how a python program is created.py   

Why `Tweepy`? I chose to use the python module tweepy because I wanted to tinker with python and create something that I would use in my everyday life. I find learning through a personal project is a great way to pickup a skill and `Tweepy` did just that for me. For this post I'm going to get you familiar with the the bot I wrote using `Tweepy` to respond to tweets while I'm away on vacation. Let me stop all this jaw jabbering and get into the technicals of how this all works.

> The [Tweepy API](http://docs.tweepy.org/en/latest/index.html) docs will be the first place you will need to visit if you have never used the `tweepy` module before. Follow the `Getting Started` section from within the docs before you begin this tutorial.

### Twitter Voicemail


```
    search_for = "@MisterFili"
    tweets_mentioned = 1

    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            username = tweet.user.screen_name
            tweet_id = tweet.id_str
            away_msg = f"@{username} Seems to me that you are looking for my creator, Monsieur Fili. He is probably at where ya sista went... If urgent, please send m'Lord a text msg. standard rates apply."
            
        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
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
                        print(f"old tweet from: @{username}\n", tweet.text)
                        continue
                    else:
                        with open(cheapDB, "a") as f:
                        #if tweet_id exist in file skip writing to file
                        #else write to file
                            f.write(f"{tweet_id}\n")
                            print(f"\nAdding tweet id: {tweet_id} to file for tracking")
                            print("update status")
                            api.update_status(status=away_msg, in_reply_to_status_id=tweet.id)
                            print(f"@{username} said:\n{tweet.text} \n")
```



Now that you are able to send a tweet you are one step closer to building a low-level bot! Lets add some cooler funcationality to this basic bot so we can A) learn some python and B) create something cool while learning.

One more thing before we jump into this hackathon. It is a good habbit to write out how your program will work so you can refrence your coding roadmap if you get lost or want to go a different direction. Below you'll find my high-level logic roadmap for my voicemail function.

* Search for users who have @'ed you
    * pick a number of mentions to cycle through.
* For each user who @ you. send automated reply
* save the response into a "cheap" database
    * this is so you dont respond to the same tweet twiice

#### Search For Users Who've @'ed You
For me to find out which users @'ed me. I need to use Tweepy's `Cursor` object. We will be passing in the [`api.serch`](http://docs.tweepy.org/en/latest/api.html#API.search) method within the object, so we can search against my @ name and see who has mentioned me. 

```    
    search_for = "@MisterFili"
    tweets_mentioned = 1
    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
```
All of this the results will be stored in a for loop. This `for loop` will let me respond to more than one person @'ing me at a time. I'm looping through the results so I can respond to X amount of users in a batch like manner. The next few lines I'm assigning the results of my search to variables(`name`, `tweet_id`, & `away message`). Then setting up an exception to catch any errors that may appear within the `for loop`.


```
for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            username = tweet.user.screen_name
            tweet_id = tweet.id_str
            away_msg = f"@{username} Seems to me that you are looking for my creator, Monsieur Fili. He is probably at where ya sista went... If urgent, please send m'Lord a text msg. standard rates apply."
```
Still within the for loop, we are going to write/save the tweetid to a file, so we will not respond to the same tweet twice. Twitter may cover the double tweet but we may receive error codes like "tweet has been previously tweeted". Or  your fame could be dropping in popularity so not that many people are searching for you. You'll end up responding to the same fans multiple times, possibly throwing errors we should avoid as nerds. 

With the use of the `with open` statement we open our `cheapDB` which is a text file, and begin to write to it. Next, a for loop is created to cycle through our `tweet_ids` and find out if we responded to an @ before or not. If the `tweet_id` is found within the `cheapDb`, we skip it and do not respond. IF the `tweet_id` has not been saved, then we are going to write the `tweet_id` to file, then tweet out our away message. 

```
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
                        print(f"old tweet from: @{username}\n", tweet.text)
                        continue
                    else:
                        with open(cheapDB, "a") as f:
                        #if tweet_id exist in file skip writing to file
                        #else write to file
                            f.write(f"{tweet_id}\n")
                            print(f"\nAdding tweet id: {tweet_id} to file for tracking")
                            print("update status")
                            api.update_status(status=away_msg, in_reply_to_status_id=tweet.id)
                            print(f"@{username} said:\n{tweet.text} \n")
```
Looks like we have reached the end of our logic roadmap. We should have a bot responding ! We can continue to improve this bot within endless features. Such as:
* Sending snarky responses if someone responds multiple times to the bot under a certain time frame. 
* Cycling through your frends list and tweeting random information your followers love you for. 
* Scraping twitter for a #hashtag you started and saving respones to a document to prove your're a trend setter. 

