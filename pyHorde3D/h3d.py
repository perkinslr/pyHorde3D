#  h3d.py
#  
#  Copyright 2014 Logan Perkins <perkins@lp-programming.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the Eclipse Public License 1.0
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#  
#  
import subprocess, os
def loadLibrary(libname, ffi):
	print "Looking for", libname
	t=subprocess.Popen(['ld', '-o', '/dev/null', '--verbose', '-L%s'%os.environ.get('HORDELIB','/usr/local/lib'), '-l%s'%libname ],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	t.wait()
	p=t.stdout.read().split('-l%s'%libname)[1].split('(')[1].split(')')[0]
	print "Results:",p
	return ffi.dlopen(p,ffi.RTLD_GLOBAL)


from math import sin,cos,radians

import os
import glfw_h
import horde3d_h
import cffi

ffi=cffi.FFI()
ffi.include(glfw_h.ffi)
ffi.include(horde3d_h.ffi)

from weakref import ref

loadLibrary('X11',ffi)
h3d=loadLibrary('Horde3D',horde3d_h.ffi)
h3dut=loadLibrary('Horde3DUtils',horde3d_h.ffi)
glfw=loadLibrary('glfw',glfw_h.ffi)

symbols=dict(
	Sin=lambda s:sin(radians(s)),
	Cos=lambda s:cos(radians(s))
)



symbols.update(horde3d_h.getfunctions(h3dut))
#symbols.update(horde3d_h.getfunctions(h3d))

symbols.update(glfw_h.getfunctions(glfw))
symbols.update(horde3d_h.s)

globals().update(symbols)

print "GLFW Version:", ffi.string(glfwGetVersionString())
print "Horde3d Version:", ffi.string(h3dGetVersionString())
