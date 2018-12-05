# Current CPU %
usrCPU=`top -l 1 | awk 'NR==4 {printf "%.f%%", $3+$5}'`
cpuTemp=`tempmonitor -ds -c -a -l | grep "CPU A PROXIMITY" | awk '{print $5}'`

	## CPU Utilisation will display temp if "tempmonitor" is installed
[ "$cpuTemp" ] && cpuTemp="(${cpuTemp}°C)"
[ "$usrCPU" ] && echo "${bold}CPU Usage:${nobold}\t\t${usrCPU} ${cpuTemp}"


# Current RAM %
	## Credit for vm_stat: http://bit.ly/HPcgXT
myActiveMem=`vm_stat | awk 'NR==3 {printf "%.f",$3*4096/1048576}' | sed 's/\.//'`
myTotalMem=`sysctl -n hw.memsize | awk '{print $0/1048576}'`
myUsedPer=`echo|awk '{printf("%.f%%", a / t * 100)}' a=$myActiveMem t=$myTotalMem`

[ "$myActiveMem" ] && echo "${bold}Active RAM:${nobold}\t${myUsedPer} (${myActiveMem} Mb)"


# Current Disk Usage %
	## Credit: Unknown
	## Will display SMART status if it is not VERIFIED
myDiskUsePc=`df -hl | grep 'disk0s2' | awk '{print $5}'`
myDiskUseMb=`df -hl | grep 'disk0s2' | awk '{print $3}' | sed s/Gi/ Gb/`
mySMART=`diskutil info $(bless --getBoot) | grep "SMART Status" | awk '{print $3}' | grep Verified > /dev/null`

[ "$myDiskUsePc" -a "$myDiskUseMb" ] && echo "${bold}HD Usage:${nobold}\t\t"$myDiskUsePc "("$myDiskUseMb")" $mySMART

# Current User Downloads Folder Size
fdrSize=`du -sh ~/ | awk '{print $1}'`
[ "${fdrSize#${fdrSize%?}}" = "B" ] && dirSize="Empty" || dirSize="${fdrSize%?} ${fdrSize#${fdrSize%?}}b"
echo "${bold}Space Used:${nobold}\t\t${dirSize}"


# Current User Trash Folder Size
fdrSize=`du -sh ~/.Trash | awk '{print $1}'`
[ "${fdrSize#${fdrSize%?}}" = "B" ] && dirSize="Empty" || dirSize="${fdrSize%?} ${fdrSize#${fdrSize%?}}b"
echo "${bold}User Trash:${nobold}\t\t${dirSize}"


echo


ucurl="curl -s --connect-timeout 2"