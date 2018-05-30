#!/bin/bash
cd ~
a=`pwd`
p="`pwd`\image"
if [ ! -d "`pwd`\image" ]
then
   mkdir image
fi
  # mkdir image
  # echo creat directory image
echo $a
ffmpeg -ss $1 -r 1 -i $2 -t $3 -q:v 2 -f image2 -y image/%d.jpg

