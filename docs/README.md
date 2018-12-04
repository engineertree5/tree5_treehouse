# Treehouse5 - Working With GeekTools

<figure class="thumbnails">
    <img src="media/img/desktopshot.jpeg" alt="Screenshot of Desktop" title="My Desktop">
</figure>

**REQUIREMENTS (Mac OSX)**
* A working computer (any OS will do)
* basic understanding of mac terminal
* Willingness to fail & learn

## Desktop WallPaper

The wallpaper I designed myself. The images I used came from [Mustafah Abdulaziz](http://www.mustafahabdulaziz.com). If you'd like to use this wallpaper you can download it [here](https://google.com)

## Date & Uptime

The date and update was generated using bash commands via the terminal. it was really quite simple and if you followed the geektool introuduction you are probably already familar with how to display the date. However, if you did not view the geektool how-to i'll show you how I was able to print the current date. I typed the following into the terminal:

    $ date '+%A %d'

# Computer Uptime {docsify-ignore}

This was achieved through a lot of trial and error with understanding the `awk` command and manipulating txt. I was able to print the uptime of my computer by min, hr, and days by typing the following:

     $ uptime | awk '{sub(/[0-9]|user\,|users\,|load/, "", $6); sub(/mins,|min,/, " min", $6); sub(/user\,|users\,/, "", $5); sub(",", " min", $5); sub(":", "h ", $5); sub(/[0-9]/, "", $4); sub(/day,/, " day ", $4); sub(/days,/, " days ", $4); sub(/mins,|min,/, "min", $4); sub("hrs,", "h", $4); sub(":", "h ", $3); sub(",", "min", $3); print "Uptime: " $3$4$5$6}'
    
This command can look agressive if it is your first time seeing a command like this, so lets break it down.

`uptime` - Print how long the system has been running 

    Example:
    from your terminal run the below command
    $ uptime

from the uptime man page - The uptime utility displays the current time, the length of time the system has been up, the number of users, and the load average of the system over the last 1, 5, and 15 minutes.

` | ` - (pipe) each command in a pipeline is executed as a seperated process

`awk` - pattern scanning and processing

`sub` - string subsistution function

    Template for sub() function:
    sub(regexp,replstring,mystring)


---------------
###FIX LATER
## GeekTool How-GeekTo

Before I begin explaining how I customized my desktop background I'd like to preface with why I'm doing what I"m doing. The main reason behind me sharing this "how-to" is for me to open up and share my tech journey. I'm also doing this so anyone new or old can follow along. Although there are many places to get started with how-to program. I'm hopping I can help someone through this site. If anything, this will be a pretty neat digital journal to look back on.

Now that the sentimental piece is out of the way we can start the requirements. 