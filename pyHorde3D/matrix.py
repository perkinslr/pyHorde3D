#  matrix.py
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

from math import sin,cos,radians
Sin=lambda s:sin(radians(s))
Cos=lambda s:cos(radians(s))
import cffi,subprocess
ffi=cffi.FFI()

t=subprocess.Popen(['gcc','-E','matrix.h'],stdout=subprocess.PIPE)
t.wait()
dta=t.stdout.read()

ffi.cdef(dta)

matrix=ffi.dlopen('./_matrix.so')


class Matrix:
	def __init__(self, floats=[1.000000,0.000000,0.000000,0.000000,0.000000,1.000000,0.000000,0.000000,0.000000,0.000000,1.000000,0.000000,0.000000,0.000000,0.000000,1.000000]):
		self._matrix=matrix.matrixFromFloats(floats)
	def update(self, floats):
		matrix.updateMatrixFromFloats(self._matrix, floats)
	def __iter__(self):
		f=matrix.floatsFromMatrix(self._matrix)
		return iter((f+i)[0] for i in range(16))
	def scale(self, x,y,z):
		matrix.scaleMatrix(self._matrix,x,y,z)
	def rotate(self, x,y,z,aboutCenter=True):
		if aboutCenter:
			center=self.getTranslation()
			scale=self.getScale()
			self.translate(-center[0],-center[1],-center[2])
			self.scale(1/scale[0],1/scale[1],1/scale[2])
			matrix.rotateMatrix(self._matrix,x,y,z)
			self.scale(*scale)
			self.translate(*center)
		matrix.rotateMatrix(self._matrix,x,y,z)
	def translate(self, x,y,z):
		matrix.translateMatrix(self._matrix,x,y,z)
	def getRotation(self):
		f = ffi.new('float[3]');
		matrix.rotationFromMatrix(self._matrix, f)
		return [f[i] for i in range(3)]
	def getTranslation(self):
		f = ffi.new('float[3]');
		matrix.translationFromMatrix(self._matrix, f)
		return [f[i] for i in range(3)]
	def getScale(self):
		f = ffi.new('float[3]');
		matrix.scaleFromMatrix(self._matrix, f)
		return [f[i] for i in range(3)]
	def forward(self, distance):
		print distance
		r=self.getRotation()
		z = Cos(r[1])*Cos(r[2])
		y = Sin(r[0])*Cos(r[2])
		x = Sin(r[2])
		
		d=(x**2+y**2+z**2)**0.5
		distance/=d
		
		print self.getTranslation()
		self.translate(x*distance,y*distance,z*distance)
		print self.getTranslation()
