#  Horde3D.py
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

import h3d
ffi=h3d.ffi

globals().update(h3d.symbols)

glfwStarted=False

class glfwWindow:
	def __init__(self, width, height, title, monitor=ffi.NULL):
		global glfwStarted
		if not glfwStarted:
			glfwInit()
			self._window=glfwCreateWindow(width, height, title, monitor, ffi.NULL);
			glfwMakeContextCurrent(self._window)
			h3d.h3dInit()
			glfwStarted=True
		else:
			self._window=glfwCreateWindow(width, height, title, monitor, ffi.NULL);
		self._onclose=ffi.callback('void(*)(GLFWwindow *)',self.onClose)
		glfwSetWindowCloseCallback(self._window, self._onclose)
	def __del__(self):
		glfwDestroyWindow(self._window)
	title=property(lambda self: self._title, lambda self,title:[setattr(self,'_title',title),glfwSetWindowTitle(self._window, title)])
	def getPos(self):
		xpos=ffi.new('int[1]')
		ypos=ffi.new('int[1]')
		glfwGetWindowPos(self._window, xpos, ypos)
		return [xpos[0], ypos[0]]
	def setPos(self, x, y):
		glfwSetWindowPos(self._window, x, y)
	def getSize(self):
		width=ffi.new('int[1]')
		height=ffi.new('int[1]')
		glfwGetWindowSize(self._window, width, height)
		return [width[0],height[0]]
	def setSize(self, width, height):
		glfwSetWindowSize(self._window, width, height)
	def onClose(self, *args):
		print "onClose stub"
	def swapBuffers(self):
		glfwSwapBuffers(self._window)
	def makeActive(self):
		glfwMakeContextCurrent(self._window)
	def setController(self, controller):
		self._controller=ref(controller)
		glfwSetKeyCallback(self._window, controller.keyPressCallback)
		glfwSetMouseButtonCallback(self._window, controller.mouseButtonCallback)
		glfwSetCursorPosCallback(self._window, controller.mouseMoveCallback)
		glfwSetScrollCallback(self._window, controller.mouseWheelCallback)


if __name__=='__main__':
	glfwWindow(2880,1620,'xyzzy')
