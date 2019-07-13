#!/bin/bash

#basic script to empty contents within the Trash dir

#set script to fail on error
set -e 

error_exit() {
	echo "$1" 1>&2
	exit 1
}

#var for later use
TRASH="/Users/MisterFili/.Trash"

#get size of trash 
TRASH_SIZE=`du -sh ${TRASH}`

echo -e "\nTrash Size:\n${TRASH_SIZE}"

#Function to empty Trash
funcRemoveAllTrash () {
    echo "These are the files that will be deleted"
    
    #cd to trash dir and list files that will be delete
    cd $TRASH
    ls -lo ${FILE_NAME}* | awk '{print "Size: "$5, "\t", "Name: "$9}'
    
    echo -e "\nAre you sure you want to remove these files? (yes or no)"
    read ANSWER
    
#condition statement to identify if user wants to remove files or not
    if [ "$ANSWER" == "y" ] || [ "$ANSWER" == "yes" ]; then
      echo "deleteing...."
      rm -rf $TRASH/*
      sleep 1
      echo "DONE!"
      echo -e "\nTrash Size:\n${TRASH_SIZE}"
      exit 1
    
    elif [ "$ANSWER" == "n" ] || [ "$ANSWER" == "no" ]; then
      echo -e "\n\nYou are not sure. \nExiting.."
      exit 1
    else
      echo "$ANSWER not an option"
      echo "exiting"
      exit
    fi
}

#Function to remove select items from trash
funcRemoveSelectItems () {

    #list files for user to make selection
    echo -e "listing files by \n "
    ls -lSh ${TRASH} | awk '{print "Size: "$5, "\t", "Name: "$9}'
    echo -e "name the files you'd like to have deleted:"
    echo "Usage: FILENAME(s)"
    
    #ls abc*   list all files starting with abc---
    #ls *abc*  list all files containing --abc--
    #ls *abc   list all files ending with --abc
    
    read FILE_NAME
    echo "These are the files that will be deleted"
    cd $TRASH
    
    ls -lo ${FILE_NAME}* | awk '{print "Size: "$5, "\t", "Name: "$9}'
    
    echo -e "\nAre you sure you want to remove these files? (yes or no)"
    read ANSWER
    
    #condition statement to identify if user wants to remove files or not
    if [ "$ANSWER" == "y" ] || [ "$ANSWER" == "yes" ]; then
      echo "deleteing...."
      rm $FILE_NAME*
      sleep 1
      echo "DONE!"
      echo -e "\nTrash Size:\n${TRASH_SIZE}"
      exit 1
    elif [ "$ANSWER" == "n" ] || [ "$ANSWER" == "no" ]; then
      echo -e "\n\nYou are not sure. \nExiting.."
      exit 1
    else
      echo "$ANSWER not an option"
      echo "exiting"
      exit
    fi
}

#while loop to identify if user wants to remove All files or a select few
while : 
do
    echo -e "\nHow would you like to proceed?"
    echo -e "\na) Delete everything"
    echo -e "\nb) Delete certain objects"
    
    read OPTION

    case $OPTION in
    'a'|'A')
    echo -e "You selected option ${OPTION}. Proceding to delet everything" 
    funcRemoveAllTrash
    break ;;
    #Delete everything
    'B'|'b')
    echo -e "\nYou selected option ${OPTION}. Type of out the name of the files you want removed"
    funcRemoveSelectItems 
    break ;;
    #Delete certain objects
    *)
    echo -e "${OPTION} is not an option" ;;
    #   exit 1;;
    esac
    sleep 1
    clear

done