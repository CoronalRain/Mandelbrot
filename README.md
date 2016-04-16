# Mandelbrot Visualizer

**by Troy P. Kling**

<img src="http://troykling.com/files/mandelbrot.png" alt="Mandelbrot Set" width="375" height="333">

## Description

The Mandelbrot set is the set of values of c in the complex plane for which the orbit of 0 under iteration of the complex polynomial

> z[n+1] = z[n]^p + c

remains bounded.

Images of the Mandelbrot set display an elaborate boundary that reveals progressively ever-finer recursive detail at increasing magnifications. The "style" of this repeating detail depends on the region of the set being examined. The set's boundary also incorporates smaller versions of the main shape, so the fractal property of self-similarity applies to the entire set, and not just to its parts.

The Mandelbrot set has become popular outside mathematics both for its aesthetic appeal and as an example of a complex structure arising from the application of simple rules, and is one of the best-known examples of mathematical visualization. This Python package is an attempt at a straightforward, user-friendly implementation of Mandelbrot set visualization.

## Installation

Start by ensuring that all dependencies are installed. The Mandelbrot Visualizer requires the numpy, matplotlib, and docopt packages.

Next, clone this repository.

> git clone https://gitlab.com/CoronalRain/Mandelbrot.git

Once the repo is successfully cloned, navigate to the Mandelbrot directory and install the package.

> python setup.py install

You're now ready to use the Mandelbrot Visualizer!

## How to Use

You can interface with the tool in two different ways: through Python and through the terminal/command prompt.

### Python

Start a Python instance and load the Mandelbrot package, as well as other useful packages.

> import numpy as np

> import matplotlib.pyplot as plt

> from mandelbrot import mandelbrot, mandelbrot_color

#### The mandelbrot() Function

The mandelbrot() function takes 5 arguments:

- *n*, the number of times to iterate the Mandelbrot function (default: 25)
- *size*, the size of the output image (default: 250)
- *xlim*, a tuple or 1D array containing the bounds for the real part of the complex plane (default: (-2.0,2.0)).
- *ylim*, a tuple or 1D array containing the bounds for the imaginary part of the complex plane (default: (-2.0,2.0)).
- *p*, the power of the Mandelbrot polynomial (default: 2).

The mandelbrot() function returns a 2D numpy array of 1s and 0s, indicating whether or not the escape time for each number in the complex plane converges under the given number of iterations. When executed using the default arguments, the result is a 2D array of size 500x500 that contains the results of iterating the Mandelbrot function 25 times over the region of the complex plane bounded by x=(-2,2), y=(-2,2).

> mandel = mandelbrot()

> plt.imshow(mandel, cmap=plt.get_cmap("gray_r"))

Increasing *n* gives higher precision. Increasing *size* gives higher resolution. Shrinking *xlim* and *ylim* allows one to zoom in on regions of interest. Changing *p* allows one to investigate different forms of the Mandelbrot set, though *p=2* is by far the most common power used. Trying different parameter values is highly encouraged, but it should be noted that it may take a long time to compute the Mandelbrot set for large values of *n* and *size* and for small values of *xlim* and *ylim*.

#### The mandelbrot_color() Function

The mandelbrot_color() function takes the same 5 arguments as the mandelbrot() function, although the meaning of *n* is slightly different in this case. mandelbrot_color() doesn't just generate the Mandelbrot set for a single value of $n$, it generates it for **all** values less than or equal to *n*. This tells the user which complex values always converge, which ones always diverge, and - perhaps most interesting of all - which ones only diverge after several iterations. This serves to highlight the most interesting areas of the Mandelbrot sets - the chaotic regions on the border where convergence and divergence are unpredictable.

> mandel_color = mandelbrot_color()

> plt.imshow(mandel_color, cmap=plt.get_cmap("RdGy_r"))

Although the mandelbrot_color() function has to generate a Mandelbrot set for each iteration number less than *n*, it is only marginally slower than the mandelbrot() function. This is because it utilizes information gathered in previous iterations to speed up the computation of each subsequent iteration.

Note that the command above contains the cmap argument. Users are encouraged to try out other colormaps, found [here](http://matplotlib.org/examples/color/colormaps_reference.html).

#### Other functions

The functions sequence() and limit() are also available. As the name suggests, sequence() returns a 1D array containing the values z[i] for all i<=n for a particular complex number c, i.e. the Mandelbrot sequence for c. Similarly, the limit() function computes the "limit" of this sequence. This value is either the last element in the sequence (if z[n]<2) or infinity (if z[n]>=2).

### Terminal

The Mandelbrot Visualizer can also be used from the terminal/command prompt. In order to see the documentation for this, run the following command.

> python mandelbrot.py --help

The usage of the program is essentially the same as described above, except this version automatically outputs png images of the generated Mandelbrot set using the given colormap.