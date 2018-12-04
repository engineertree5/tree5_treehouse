# Treehouse5 - Working With GeekTools

<figure class="thumbnails">
    <img src="media/img/desktopshot.jpeg" alt="Screenshot of Desktop" title="My Desktop">
</figure>

**REQUIREMENTS (Mac OSX)**
* A working computer (any version of macOS will do)
* [GeekTool](https://www.tynsoe.org/v2/geektool/documentation/)
* basic understanding of the mac terminal
* Willingness to fail & learn

To duplicate what i've created you will first need to get GeekTool. Geektool is a macOS application that will let you customize your desktop. You can keep it simple with the date and time or go more complex and show how many CPU cores your computer is using at the current time.

Lets get started with the basics. I'll share with you how I was able to create my desktop background using geektool.

## Desktop WallPaper

My Desktop wallpaper I designed using photoshop. The image I used came from [Mustafah Abdulaziz](http://www.mustafahabdulaziz.com). If you'd like to use this wallpaper you can download it [here](https://google.com)

## Date & Uptime

?> Vist [GeekTool](https://www.tynsoe.org/v2/geektool/documentation/) for the quick start guide or follow along by using your mac terminal

The day and date was generated using shell commands via the terminal. Every mac comes with the terminal already installed. search for `terminal` under your applications or through finder. Once you have your terminal open type in the following:

?> The `$` represents the start of a new line within the terminal. DO NOT COPY THE `$`

    $ date '+%A %d'

This should display the day and then the date. Try changing the `A` to lowercase and see what happens. If you are curious and would like to try more date combinations. I would recommend reading over the man page for date. type the following to get to the man page:

    $ man date

use the arrow keys or spacebar to scroll the page
q - to quit

# Computer Uptime {docsify-ignore}

You will need to be familiar with the shell command `awk`- can do simple text replacements and much more advanced parsing. I only used the `sub()` function with `regular expressions` to manuipulate the output of `$ uptime`.

the below command was used to display how long the system has been running:

     $ uptime | awk '{sub(/[0-9]|user\,|users\,|load/, "", $6); sub(/mins,|min,/, " min", $6); sub(/user\,|users\,/, "", $5); sub(",", " min", $5); sub(":", "h ", $5); sub(/[0-9]/, "", $4); sub(/day,/, " day ", $4); sub(/days,/, " days ", $4); sub(/mins,|min,/, "min", $4); sub("hrs,", "h", $4); sub(":", "h ", $3); sub(",", "min", $3); print "Uptime: " $3$4$5$6}'
    
lets break it down this command -

`uptime` - Print how long the system has been running 

    Example: from your terminal run the below command
    $ uptime

*from the uptime man page* - The uptime utility displays the current time, the length of time the system has been up, the number of users, and the load average of the system over the last 1, 5, and 15 minutes.

` | ` - (pipe) each command in a pipeline is executed as a seperate process

`awk` - pattern scanning and processing.

    Example: column selection with awk. 
    echo "Testing Treehouse cmds" | awk '/cmds/{print $2}'

`sub` - string subsistution function. we are omitting and subsistuting text from the uptime command so we can display the text to our liking 

    Template for sub() function:
    sub(regexp,replstring,mystring)
