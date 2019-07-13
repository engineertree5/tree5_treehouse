#!/bin/bash

#Creat a function for each option
# copy contents, create new folder, zip cosntents etc....

#set script to fail on error
set -e

#toggling debug mode
#set -x

#exit code of cmd
STATUS="$?"

####SCRIPT START #####

echo "#########"
echo -e "WELCOME TO ZIPPER!\n"
echo -e "How would you like to proceed?\nSelect One Option:"
echo "a) Move file(s) to an existing directory"
echo "b) Create new folder/dir and move files to location"
echo "c) Create new folder, move contents to folder and zip up"
echo "D). Zipping contenets "
read QUESTION

#Function for option A
function option_a() {
    echo "Great! Let's move those files"
    echo -e "\nWhich file(s) would you like to move?"
    echo "ex: myfiles. Assume that there will be a * at the end of your input"

    #read user input
    read MYFILES
    echo -e "These are the files I will move for you `ls ${MYFILE}*`"
    echo ""

    echo "do you need a new folder?"
    read ANSWER

    if [ "$ANSWER" == "y" ]; then
      echo "What is the folder name?"
      read FOLDERNAME
      mkdir $FOLDERNAME
      echo "moving `ls | grep 120mm` into $FOLDERNAME"
      mv ${MYFILES}*  ${FOLDERNAME}
    else
      echo "continuing..."
    fi

    echo "Would you like to move the file(s) or folder"


    echo ""
    echo ""
    echo "Would you like a zipped version of the folder?"
    read ANSWER3
    if [ "$ANSWER3" == "y" ]; then
      echo "zipping up contents..."
      #toggling debug mode 
      set -x
      zip -r ${FOLDERNAME}.zip $FOLDERNAME
      #turning off debug mode
      set +x
    else
      set +x
    fi

    echo -e "Would you like to remove the $FOLDERNAME dir"
    read USERANSWER

    if [ "$USERANSWER" == "y" ]; then
      echo "removing $FOLDERNAME dir"
      rmdir $FOLDERNAME
      echo "$STATUS"
    else
      echo "Script Finished"
    fi

}

# B). Create new folder/dir and move files to location"
function option_b() {
    echo -e "\nNew Directroy coming up"
}

# C). Renaming File(s)"
function option_c {
    echo -e "\nCreating new folder"
    #list the files you would like to copy or move
    #Where would you like? to copy the files too?
    #do you need a folder?
    #Do you want to remove the files that were copied?
}

# D). Package and Zip contents"
function option_d {
    echo -e "D). Package and Zip contents"
    echo "which file(s) and/or folder(s) do you want to zip up!?"
    echo "do you need a new folder?"
    read NEEDF

    if [ "$NEEDF" == "y" ] || [ "$NEEDF" == "yes" ]; then
        echo "What would you like to name the folder? (no spaces please)"
        read NEWFOLDERNAME
        echo -e "Creating Folder $NEWFOLDERNAME in `pwd`"
        mkdir $NEWFOLDERNAME
        
    else
        echo "continuing..."  
    fi

}

while true; do #loop through options until true
  if [ "$QUESTION" = "a" ] || [ "$QUESTION" = "A" ]; then
      option_a
      break 
    elif [ "$QUESTION" = "b" ] || [ "$QUESTION" = "B" ]; then
      option_b
      break
    elif [ "$QUESTION" = "c" ] || [ "$QUESTION" = "C" ]; then
      option_c
      break
    elif [ "$QUESTION" = "d" ] || [ "$QUESTION" = "D" ]; then
      option_d
      break
    else
        clear
        echo -e "$QUESTION is not from the list. \nTRY AGAIN"
        echo " ################################### "
        sleep 1
        echo " "
        echo -e "How would you like to proceed?\nSelect One Option:"
        echo "A). Move file(s) to an existing directory? "
        echo "B). Create new folder/dir and move files to location"
        echo "C). Renaming File(s)"
        echo "D). Package and Zip contents"
        read QUESTION
  fi
done

echo "BLAH"
