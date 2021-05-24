import vapoursynth as vs

core = vs.get_core()
clip = core.ffms2.Source(source=source, fpsnum=int(fpsnum), fpsden=int(fpsden))
#clip = core.resize.Point(clip, format=vs.YUV420P8, matrix_s="709")

super = core.svp1.Super(clip, "{\"gpu\":1,\"pel\":2,\"full\":true}")
vectors = core.svp1.Analyse(super["clip"],super["data"],clip,"{}")
smooth = core.svp2.SmoothFps(clip,super["clip"],super["data"],vectors["clip"],vectors["data"],"{}")
smooth = core.svp2.SmoothFps(clip,super["clip"],super["data"],vectors["clip"],vectors["data"],"{\"rate\":{\"num\":2,\"den\":1,\"abs\":false}}")


smooth.set_output()
