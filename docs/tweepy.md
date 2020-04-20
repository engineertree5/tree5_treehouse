# Tweepy
<figure>
    <img src="media/img/tbot.jpg" alt="tbot image" title="tbot image">
</figure>

!> I'm assuming you have a basic understanding of how a python program is created.py   

Why `Tweepy`? I chose to use the python module tweepy because I wanted to tinker with python and create something that I would use in my everyday life. I find learning through a personal project is a great way to pickup a skill and `Tweepy` did just that for me. For this post I'm going to get you familiar with the the bot I wrote using `Tweepy` to respond to tweets while I'm away on vacation. Let me stop all this jaw jabbering and get into the technicals of how this all works.

> The [Tweepy API](http://docs.tweepy.org/en/latest/index.html) docs will be the first place you will need to visit if you have never used the `tweepy` module before. Follow the `Getting Started` section from within the docs before you begin this tutorial.<br>
Another good source is from `realpython.com`. [Following this](https://realpython.com/twitter-bot-python-tweepy/#how-to-make-a-twitter-bot-in-python-with-tweepy) may be a better start if you have not setup your bot yet. 

## Twitter Voicemail

<figure>
    <center><img src="media/img/zero.gif" alt="zero gif" title="zero gif"></center>
</figure>

```python
    search_for = "@MisterFili"
    tweets_mentioned = 1

    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            username = tweet.user.screen_name
            tweet_id = tweet.id_str
            away_msg = f"@{username} Seems that you are looking for my creator, Monsieur Fili. He is currently Out of the office... May I help you with some music in his absence. Reply to me with an artist name wrapped in double quotes \"artist name\" "
            
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

- [x] Search for users who have @'ed you
  - [x] pick a number of mentions to cycle through.
- [x] For each user who @ you. send automated reply
- [x] save the response into a "cheap" database
  - [x] this is so you dont respond to the same tweet twiice

### Search For Users Who've @'ed You
For me to find out which users @'ed me. I need to use Tweepy's `Cursor` object. We will be passing in the [`api.serch`](http://docs.tweepy.org/en/latest/api.html#API.search) method within the object, so we can search against my @ name and see who has mentioned me. 

```python 
    search_for = "@MisterFili"
    tweets_mentioned = 1
    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
```
All of the results of the search will be stored in a for loop. This `for loop` will let me respond to more than one person @'ing me at a time. I'm looping through the results so I can respond to X amount of users in a batch like manner. The next few lines I'm assigning the results of my search to variables(`name`, `tweet_id`, & `away message`). Then setting up an exception to catch any errors that may appear within the `for loop`.


```python
for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            username = tweet.user.screen_name
            tweet_id = tweet.id_str
            away_msg = f"@{username} Seems to me that you are looking for my creator, Monsieur Fili. He is probably at where ya sista went... If urgent, please send m'Lord a text msg. standard rates apply."
```
Still within the for loop, we are going to write/save the tweetid to a file, so we will not respond to the same tweet twice. Twitter may cover the double tweet but we may receive error codes like "tweet has been previously tweeted". Or  your fame could be dropping in popularity so not that many people are searching for you. You'll end up responding to the same fans multiple times, possibly throwing errors we should avoid as nerds. 

With the use of the `with open` statement we open our `cheapDB` which is a text file, and begin to write to it. Next, a for loop is created to cycle through our `tweet_ids` and find out if we responded to an @ before or not. If the `tweet_id` is found within the `cheapDb`, we skip it and do not respond. IF the `tweet_id` has not been saved, then we are going to write the `tweet_id` to file, then tweet out our away message. 

```python
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
<figure>
    <center><img src="media/img/mybad.gif" alt="not working" title="no funny"></center>
</figure>
Looks like we have reached the end of our logic roadmap. We should have a bot responding ! We can continue to improve this bot within endless features. Such as:
* Sending snarky responses if someone responds multiple times to the bot under a certain time frame. 
* Cycling through your frends list and tweeting random information your followers love you for. 
* Scraping twitter for a #hashtag you started and saving respones to a document to prove your're a trend setter. 

### Class of Dicts 
I figured I'd add more detail to this snippet of code so newbies can get a better understanding HOW the code actually works. Knowing how something works will only make you a better troubleshooter. 

So, We have this `for loop` which will pull in users who've @'ed me. But how did I know `tweet.user.screen_name` was an attribute? There are a few ways to go about this, and that is the beauty of programming. Many different ways to get to the finish line. I'm going to use methods that are sitting within python3. First we need to know what type of object we are dealing with here. so lets call the type method to get a better look at what we are dealing with. 

```python
    search_for = "@MisterFili"
    tweets_mentioned = 1
    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        print(type(tweet))
------------
#RESPONSE
<class 'tweepy.models.Status'>
```
Ok, so we know the properties of `tweet` are the type of model class `<class 'tweepy.models.Status'>`. The model class defines our search response as a datastore entity. So we are going to look at the properties of the model class, `tweet`,  by using the [`vars([object])`](https://docs.python.org/2/library/functions.html#vars). This method will "Return the __dict__ attribute for a module, class, instance, or any other object with a __dict__ attribute." This means that the object model `tweet` datastore is defined by a dict. 

```python
    search_for = "@MisterFili"
    tweets_mentioned = 1
    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        checking = vars(tweet)
        print(type(checking))
````
If you printed the output you should see that the data returned is a dict. Its a messy dict, so lets clean it up a little so we can look at it with some respect. Lets toss it in a for loop and seperate the items. 

```python
### RESPONSE
    search_for = "@MisterFili"
    tweets_mentioned = 1
    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        checking = vars(tweet)
        for i in checking:
            print(i)
    ...
    truncated
    entities
    metadata
    source
    source_url
    in_reply_to_status_id
    in_reply_to_status_id_str
    in_reply_to_user_id
    in_reply_to_user_id_str
    in_reply_to_screen_name
    author
    user
    ....
```
To look at the `keys` of the dict. We will need to use dot notation to pick through the `keys` and see what data is within the dict. You may have to do this a few times to get what information you need. To find the users screen-name you have to look at `tweet.user`. Then you will find a `name` and `screen_name` attribure. I'm looking to reply back to the user so I used `screen_name` username = tweet.user.screen_name

```python
    
    search_for = "@MisterFili"
    tweets_mentioned = 1
    for tweet in tweepy.Cursor(api.search, search_for).items(tweets_mentioned):
        try:
            username = tweet.user.screen_name
            tweet_id = tweet.id_str
            away_msg = f"@{username} Seems to me that you are looking for my creator, Monsieur Fili. He is probably at where ya sista went... If urgent, please send m'Lord a text msg. standard rates apply."
```
