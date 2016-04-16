from setuptools import setup

setup(name = "Mandelbrot",
      version = "1.0",
      description = "Mathematical tool for visualizing sections of the Mandelbrot set to arbitrary resolution.",
      author = "Troy P. Kling",
      author_email = "troykling1308@gmail.com",
      url = "https://gitlab.com/CoronalRain/Mandelbrot",
	  py_modules = ["mandelbrot"],
	  install_requires=[
		"numpy",
		"matplotlib",
		"time",
		"docopt"
	  ],
     )