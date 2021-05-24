#!/bin/bash


for var in "$@"
do
  ffmpeg -hide_banner -y -i $var -c:v dnxhd -profile:v dnxhr_hq -c:a copy $var.mov
  rm $var
done
