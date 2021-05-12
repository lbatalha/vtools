import vapoursynth as vs
import muvsfunc_numpy as mufnp

core = vs.get_core()
clip = core.ffms2.Source(source=source, fpsnum=int(fpsnum), fpsden=int(fpsden))

clip = core.resize.Point(clip, format=vs.RGB24)
clip = mufnp.super_resolution(clip=clip, model_filename="RCAN_BIX2", up_scale=2, is_rgb_model=True, pad=None, crop=None, pre_upscale=False)

clip = core.resize.Point(clip, format=vs.YUV420P8, matrix_s="709")

clip.set_output()
