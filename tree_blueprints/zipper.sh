#!/bin/bash

#set script to fail on error
set -e

#toggling debug mode
#set -x

#exit code of cmd
STATUS="$?"

####SCRIPT START #####
echo "Which files would you like to zip up?"
echo "ex: myfiles*"

#read user input
read MYFILES

echo "do you need a new folder?"
read ANSWER

if [ "$ANSWER" == "y"];do
  echo "What is the folder name?"
  read FOLDERNAME
  echo "creating zipper folder"
  mkdir FOLDERNAME
else
  echo "continuing..."
fi

echo ""

echo "moving $MYFILES into $FOLDERNAME"
cp -aR ${MYFILES}*  /${FOLDERNAME}

echo ""
echo "zipping up contents..."
zip -r ${FOLDERNAME}.zip $FOLDERNAME

echo -e "Would you like to remove the $FOLDERNAME dir"
read USERANSWER

if [ "$USERANSWER" == "y" ]; then
  echo "removing $FOLDERNAME dir"
  rmdir $FOLDERNAME
  echo "$STATUS"
else
  echo "Script Finished"
fi
