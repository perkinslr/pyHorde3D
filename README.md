pyHorde3D
=========

Dynamic python wrapper for Horde3D

Note that the high level wrapper is still mostly incomplete and the API isn't final.  The low level api is automatically generated from glut3.h, Horde3D.h, and Horde3dUtils.h, so it should adapt to new versions of Horde3D seamlessly.  
It should work with mingw/msys or cygwin on windows, but relies on the ld library loader and pexpect which are not normally available on windows.
I'm using pypy-2.1 with cffi 0.8.2 for this, 'though it does work with python2.7 as well.  
To use the matrix library, compile matrix.cpp to _matrix.so (Makefile included)
Set HORDE3DCONTENTPATH to the content directory containing your resources and HORDE3DINCLUDE to the location that holds glfw3.h and Horde3DUtil.h
Running Horde3D.py by itself should bring up a demo with the sphere and let you look around and move.
Note that matrix.cpp expects Horde3D's root directory to be up two levels, if it isn't, you'll need to change the include in matrix.cpp.  
	matrix.cpp will probably be removed soon, since the Matrix4f class that it wraps is rather useless...
