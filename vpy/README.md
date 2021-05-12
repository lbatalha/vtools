# vapoursynth

Arch repos and Aur have everything needed:
### Aur
`mxnet-cuda` - 2h compile on 3600X *DOES NOT FIT IN 32GB RAM*, compile on disk.
`vapoursynth-plugin-muvsfunc-git` - 
`vapoursynth-plugin-histogram-git` - required for `ffmpeg-full`
`vapoursynth-plugin-sangnom-git` - required for `ffmpeg-full`
`vapoursynth-plugin-svpflow1` - for framerate resampling and smooth motion
`vapoursynth-plugin-svpflow2-bin` - yes, this one too!
`ffmpeg-full` - all the good stuff, includes tensorflow build flag, arch default ffmpeg does not.

### Arch repos
`openmp` - required for `ffmpeg-full` I think

# SR Models
see:
https://github.com/WolframRhodium/Super-Resolution-Zoo
Models in repo taken from there
Example usage:

## MR-ESPCN
for 59.94fps content
`vspipe --arg source=dnxhr1080.mov --arg fpsnum=60000 --arg fpsden=1001 mr-espcn.vpy --y4m test.yuv`

encoding with ffmpeg directly:

```
vspipe --arg source=dnxhr1080.mov --arg fpsnum=60000 --arg fpsden=1001 mr-espcn.vpy --y4m - | ffmpeg -hide_banner -i pipe: -c:v libx264 -crf 20
-preset fast -threads 12 crf20espcn.mkv
```

Avg 2.1FPS render on a GTX1070, even on `-preset veryslow` still get ~1.9fps due to minor concurrence snags


## RCAN
Same as ESPCN, stupid slow, useless with my 1070


