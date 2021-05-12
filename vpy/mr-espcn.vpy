import vapoursynth as vs
import muvsfunc_numpy as mufnp

core = vs.get_core()
clip = core.ffms2.Source(source=source, fpsnum=int(fpsnum), fpsden=int(fpsden))

# Convert to YUV
clip = core.resize.Point(clip, format=vs.YUV444P8, matrix_s="709")

# Extract Y channel for superres
Y = core.std.ShufflePlanes(clips=clip, planes=0, colorfamily=vs.GRAY)
# Superres
Y = mufnp.super_resolution(clip=Y, model_filename="MR-ESPCN_2x", up_scale=2, is_rgb_model=False, pad=None, crop=None, pre_upscale=False, upscale_uv=False)

# Rebuild YUV
Y = core.fmtc.bitdepth (clip=Y, bits=8)
clip = core.std.ShufflePlanes(clips=[Y,clip], planes=[0,1,2], colorfamily=vs.YUV)


clip.set_output()
