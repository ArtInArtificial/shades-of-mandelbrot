import matplotlib.pyplot as plt
cmaps = plt.colormaps()

i = 1

fp = open("README1.md",'a')
for _ in cmaps:
    filename = "mandelbrot" + "00" + str(i) + ".png"
    fp.write("![mandelbrot](shades/{filename})".format(filename=filename))
    i += 1


