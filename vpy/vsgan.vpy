import vapoursynth as vs

from vsgan import VSGAN

# ...

core = vs.get_core()
clip = core.ffms2.Source(source=source, fpsnum=int(fpsnum), fpsden=int(fpsden))

# PyTorch device, e.g. "cpu", "cuda", "cuda:0", "cuda:1", 0, 1, ..., e.t.c
device = "cuda"

# ESRGAN model file, see https://rlaphoenix.github.io/VSGAN/VSGAN/models/
# tip: prepend path with r" ... " if path separaters use \ and not /
model = "RRDB_PSNR_x4.pth"

# 1. Create a VSGAN instance, which creates a PyTorch device instance
vsgan = VSGAN(device)

# 2. Load an ESRGAN model into the VSGAN instance
# tip: You can run load_model() at any point to change the model
vsgan.load_model(model)

# 3. Convert the clip to RGB24 as ESRGAN can only work with linear RGB data
clip = core.resize.Point(clip, format=vs.RGB24)

# 4. Use the VSGAN instance (with its loaded model) on a clip
clip = vsgan.run(clip=clip, chunk=True)

# (optional) Convert back to any other color space if you wish.
# clip = core.resize.Point(clip, format=vs.YUV420P8)

# ...

# Don't forget to set the output clip
clip.set_output()
