# Configure for PyLab #

We are not in the Unit-2 and there are example which are dependent on a module of python called `PyLab`. Now there is no clear documentation to install it. So I am trying to provide that.

## Windows Installation ## 

There are lot of documentation available for installing it, but none of it worked for me. So to Install this is the route I took.

My `pip` installation is in this path:-

````
C:\Python27\Scripts
````

So opened command line window in this folder by pressing `Shift + Ctrl + right Click`. It gives a option in the context menu `Open Command Window here`

There are two modules which we need to install.

* [NumPy](http://www.numpy.org/)
* [matplotlib](http://matplotlib.org/)

Both of these have to be installed, But before this for [NumPy](http://www.numpy.org/), we need a prerequisite [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266).

So once [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266) is installed we need to use `pip` to install [NumPy](http://www.numpy.org/) and [matplotlib](http://matplotlib.org/) by this instruction.

````
pip install numpy
pip install matplotlib
````

Once done, try this code, is it working:-

````
import pylab

pylab.plot([1,2,3,4], [1,2,3,4])
pylab.plot([1,4,2,3], [5,6,7,8])
pylab.show()
````

## Few Error which I got ##


````
Traceback (most recent call last):
  File "example02.py", line 1, in <module>
    import pylab
  File "C:\Python27\lib\site-packages\pylab.py", line 1, in <module>
    from matplotlib.pylab import *
  File "C:\Python27\lib\site-packages\matplotlib\__init__.py", line 180, in <module>
    from matplotlib.cbook import is_string_like
  File "C:\Python27\lib\site-packages\matplotlib\cbook.py", line 33, in <module>
    import numpy as np
ImportError: No module named numpy
````