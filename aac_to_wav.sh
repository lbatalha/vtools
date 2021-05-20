#!/bin/bash


for var in "$@"
do
  ffmpeg -hide_banner -y -i $var -c:v copy -c:a pcm_s32le "$var"_wav.mov
  rm $var
done
