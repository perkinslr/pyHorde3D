#  glfw_h.py
#  
#  Copyright 2014 Logan Perkins <perkins@injeanieousdeisng.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
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
