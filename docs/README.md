# Treehouse5 - Working With GeekTools

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

## Desktop WallPaper

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
