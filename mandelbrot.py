# -*- coding: utf-8 -*-
"""
Mandelbrot Visualizer 1.0

Usage:
  mandelbrot.py [options] -o <file>
  mandelbrot.py color [options] -o <file>
  mandelbrot.py (-h | --help)
  mandelbrot.py --version

Options:
  -n --iter <int>      The max iteration number to check.
                       [default: 25]
  -s --size <int>      Width/Height of the output image.
                       [default: 250]
  --x1 <float>         Left endpoint of the bounding box.
                       [default: -2.0]
  --x2 <float>         Right endpoint of the bounding box.
                       [default: 2.0]
  --y1 <float>         Bottom endpoint of the bounding box.
                       [default: -2.0]
  --y2 <float>         Top endpoint of the bounding box.
                       [default: 2.0]
  -p --power <float>   The power z is raise to in z -> z^p+c.
                       [default: 2]
  -o --out <file>      Output file path.
  -m --cmap <string>   Colormap to use (if the "color" argument is given).
  -h --help            Show this screen.
  -v --verbose         Show runtime info.
  --version            Show version.
"""

from docopt import docopt

import time
import numpy as np
import matplotlib.pyplot as plt

def sequence(c, n=25, p=2):
    z = np.zeros(n, dtype=np.complex64)
    z[0] = c
    for i in range(1, n):
        z[i] = z[i-1]**p + c
    return z

def limit(c, n=25, p=2):
    z = 0
    for i in range(1, n):
        z = z**p + c
        if np.abs(z) > 2:
            return np.inf
    return z

def mandelbrot(n=25, size=250, xlim=(-2,2), ylim=(-2,2), p=2):
    x = np.linspace(xlim[0], xlim[1], size)
    y = np.linspace(ylim[0], ylim[1], size)
    m = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            z = limit(x[i] + y[j]*1j, n, p)
            if z < 2:
                m[j,i] = 1
    
    return m

def mandelbrot_color(n=25, size=250, xlim=(-2,2), ylim=(-2,2), p=2):
    x = np.linspace(xlim[0], xlim[1], size)
    y = np.linspace(ylim[0], ylim[1], size)
    m = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            c = x[i] + y[j]*1j
            z = 0
            for k in range(n):
                z = z**p + c
                if np.abs(z) < 2:
                    m[j,i] += 1
                else:
                    break
    
    return m


if __name__ == '__main__':
    arguments = docopt(__doc__, version = "Mandelbrot Visualizer 1.0")
    
    n = int(arguments["--iter"])
    size = int(arguments["--size"])
    xlim = (float(arguments["--x1"]), float(arguments["--x2"]))
    ylim = (float(arguments["--y1"]), float(arguments["--y2"]))
    p = int(arguments["--power"])
    output = arguments["--out"]
    color = arguments["color"]
    verbose = arguments["--verbose"]
    
    if verbose:
        start = time.time()
    if color:
        k = "<="
        cmap = plt.get_cmap(arguments["--cmap"])
        mandel = mandelbrot_color(n, size, xlim, ylim, p)
    else:
        k = "="
        cmap = plt.get_cmap("gray_r")
        mandel = mandelbrot(n, size, xlim, ylim, p)
    if verbose:
        end = time.time()
        print "Time elapsed: %s seconds" % (end-start)
    
    fig = plt.figure(figsize=(10,10), frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.title("Mandelbrot set (z -> z^%s+c) at iteration %s %s" % (p, k, n))
    plt.imshow(mandel, cmap = cmap)
    plt.savefig(output)
