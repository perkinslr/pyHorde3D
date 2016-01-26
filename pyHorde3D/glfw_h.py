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



import os, re, subprocess
t=subprocess.Popen(('gcc -E %s/glfw3.h'%os.environ.get('GLFWINCLUDE', '/usr/include/GLFW')).split(),stdout=subprocess.PIPE)
data=''
while t.poll() is None:
	data+=t.stdout.read()
data = (data+t.stdout.read()).replace('\r\n','\n')

data=data.split('typedef void ( * PFNGLEGLIMAGETARGETRENDERBUFFERSTORAGEOESPROC) (GLenum target, GLeglImageOES image);')[1].replace('\n ','\n')
import cffi
ffi=cffi.FFI()
ffi.cdef(data)



def getfunctions(lib):
	functions={}
	for f in re.findall('\n[a-zA-Z* ]+? \*{0,1}([a-zA-Z0-9]+)\(',data):
		try:
			functions[f]=getattr(lib,f)
		except:
			pass
	return functions
