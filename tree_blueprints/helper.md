##TERMINAL HELPER DOC

#python location
#!/usr/local/bin/python3

#setting up python3 environment
/Users/MisterFili/Documents/GitHub/discovery/vspie/azpieEnv
source /bin/activate

#Getting help with functions
example: python -m pydoc os.system

Method to add something to your *PATH*:
        export PATH=$PATH:$HOME/bin

display the disk usage of all the directores and subdiretories
in current directory sorted by size:
	du -h * | sort -sh

#basiic keyboard functions
200~http://en.obins.net/user-manual#1

#Annie Pro Keyboard I shortcuts and such
https://www.reddit.com/r/AnnePro/comments/6wwsig/a_comprehensive_amateur_guide_to_the_anne_pro/
* issues with the command key or 'alt' key
    * Pressing Fn then Cmd locks the Cmd key out. You have to press Cmd then Fn then an arrow. Pressing Fn then Cmd will unlock it.

## Disconnection harddrive 
https://mycyberuniverse.com/macos/how-fix-volume-cant-be-ejected-because-currently-use.html
cmds to execute: 
- get list of volumes: $ ls /Volumes/$VOLNAME
- print list of open files: $ sudo lsof | grep /Volumes/$VOLNAME
- kill process which is preventing us from ejecting disk: sudo killall mds
- eject disk: diskutil unmount /Volumes/$VOLNAME


## Finding System (OS X)
* system_profiler command – Show Apple hardware and software configuration.
* sw_vers command – Show Mac OS X operating system version.
* uname command – Show operating system name and more.

## Reinstalling OSX High Sierra 
https://www.stellarinfo.com/blog/3-ways-to-downgrade-from-macos-mojave-to-high-sierra/
