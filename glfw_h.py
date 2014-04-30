#  glfw_h.py
#  
#  Copyright 2014 Logan Perkins <perkins@gentoo-flip>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the Eclipse Public License 1.0
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#  
#  



import os, re
os.system('gcc -E /usr/include/GLFW/glfw3.h > glfw3.h')

with open('glfw3.h') as f:
	data=f.read()

data=data.split('typedef void ( * PFNGLEGLIMAGETARGETRENDERBUFFERSTORAGEOESPROC) (GLenum target, GLeglImageOES image);')[1].replace('\n ','\n')
import cffi
ffi=cffi.FFI()
ffi.cdef(data)



def getfunctions(lib):
	functions={}
	for f in re.findall('\n[a-zA-Z*]+ ([a-zA-Z0-9]+)\(',data):
		try:
			functions[f]=getattr(lib,f)
		except:
			pass
	return functions
