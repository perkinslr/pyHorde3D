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

from h3d import *
glfwStarted=False
from matrix import Matrix
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

class Horde3DWindow:
	def __init__(self, width, height, title):
		self._window = glfwWindow(width, height, title)
	size=property(lambda self:self._window.getSize(), lambda self,width,height: self._window.setSize(width,height))
	pos=property(lambda self:self._window.getPos(), lambda self,x,y: self._window.setSize(x,y))
	title=property(lambda self: self._window.title, lambda self,title:setattr(self._window,'title',title))
	def renderView(self, camera):
		self._window.makeActive()
		glfwPollEvents()
		h3dRender(camera._camera)
		h3dFinalizeFrame()
		self._window.swapBuffers()
	def passthrough(self, func, *args):
		getattr(self._window, func)(*args)

class InputHandler:
	def onKeyPress(self, window, key, scancode, action, mods):
		self._parent().keyPress(key,scancode,action,mods)
	def onMouseClick(self, window, key, action, mods):
		self._parent().mouseClick(key,action,mods)
	def onMouseMove(self, window, x, y):
		self._parent().mouseMove(x,y)
	def onMouseWheel(self, window, x, y):
		self._parent().scroll(x,y)
	def __init__(self, parent):
		self._parent=ref(parent)
		self.keyPressCallback=ffi.callback('GLFWkeyfun',self.onKeyPress)
		self.mouseButtonCallback=ffi.callback('GLFWmousebuttonfun',self.onMouseClick)
		self.mouseMoveCallback=ffi.callback('GLFWcursorposfun',self.onMouseMove)
		self.mouseWheelCallback=ffi.callback('GLFWscrollfun',self.onMouseWheel)

class Camera:
	def __init__(self, name, parent, xoffset, yoffset, zoffset):
		ffi.cdef('_Bool h3dutLoadResourcesFromDisk( const char *contentDir );')
		hdr_resource=h3d.h3dAddResource(H3DResTypes.Pipeline, "pipelines/hdr.pipeline.xml", 0 )
		h3d.h3dResizePipelineBuffers( hdr_resource, 2880, 1600 );
		forwardPipeRes = h3d.h3dAddResource( H3DResTypes.Pipeline, "pipelines/forward.pipeline.xml", 0 );
		h3d.h3dResizePipelineBuffers( forwardPipeRes, 2880, 1600 );
		h3dut.h3dutLoadResourcesFromDisk(os.environ.get('HORDE3DCONTENTPATH'))
		self._parent=ref(parent)
		self._camera=h3d.h3dAddCameraNode(parent._node, name, hdr_resource)
		h3dSetupCameraView(self._camera, 60, 4/3., 0.1, 1.93776e13)
		h3dSetNodeTransform(self._camera, xoffset,yoffset,zoffset,0,0,0,1,1,1)
	def rotate(self,roll,pitch,yaw):
		h3dSetNodeTransform(self._camera,0,0,0,roll,pitch,yaw,1,1,1)

class DisplayObject:
	def __init__(self, name, parent, x, y, z,resource):
		resource=h3d.h3dAddResource(H3DResTypes.SceneGraph, resource, 0)
		h3dut.h3dutLoadResourcesFromDisk(os.environ.get('HORDE3DCONTENTPATH'))
		self._parent=ref(parent)
		self._node=h3d.h3dAddNodes(parent._node, resource)

class RootNode:
	_node=1

class PlayerController:
	def __init__(self, name, parent, x, y,z,roll,pitch,yaw):
		self._matrix=Matrix()
		self._matrix.translate(x,y,z)
		self._matrix.rotate(roll,pitch,yaw)
		sphere_resource=h3d.h3dAddResource(H3DResTypes.SceneGraph, "models/sphere/sphere.scene.xml", 0 )
		h3dut.h3dutLoadResourcesFromDisk(os.environ.get('HORDE3DCONTENTPATH'))
		self._parent=parent
		self._node=h3d.h3dAddNodes(1, sphere_resource)
		h3dSetNodeTransform(self._node, x,y,z,0,0,0,0.1,0.1,0.1)
		self._camera=Camera(name+"_camera", self, 0, 0, 0)
		self._inputHandler=InputHandler(self)
		self._parent.passthrough('setController', self._inputHandler)
	mousesensitivity=0.01
	def mouseMove(self, x, y):
		cx,cy=self._parent.size
		cx/=2
		cy/=2
		r=self._matrix.getRotation()
		
		
		self.rotate(self.mousesensitivity*(cx-x),Cos(r[0])*self.mousesensitivity*(cy-y),-Sin(r[0])*self.mousesensitivity*(cy-y))
		glfwSetCursorPos(self._parent._window._window, cx, cy)
	def keyPress(self, key,code, action, mods):
		if mods:
			speed=100000000000
		else:
			speed=0.1
		if key==83:
			self._matrix.forward(speed)
		elif key==87:
			self._matrix.forward(-speed)
		elif key==65:
			self._matrix.rotate(90,0,0)
			self._matrix.forward(speed)
			self._matrix.rotate(-90,0,0)
		elif key==68:
			self._matrix.rotate(-90,0,0)
			self._matrix.forward(speed)
			self._matrix.rotate(90,0,0)
		elif key==256:
			stop()
		elif key==82: #r
			self._matrix.rotate(0,0,1)
		elif key==80: #p
			self._matrix.rotate(1,0,0)
		elif key==89: #y
			self._matrix.rotate(0,1,0)
		else:
			print key
			self.update()
	def translate(self,x,y,z):
		self._matrix.translate(x,y,z)
		self.update()
	def rotate(self, yaw,pitch,roll):
		self._matrix.rotate(pitch,yaw,roll)
		self.update()
	def update(self):
		h3dSetNodeTransform(self._node,*(self._matrix.getTranslation()+self._matrix.getRotation()+self._matrix.getScale()))



class Light:
	def __init__(self, name, parent, x, y, z, roll, pitch, yaw, radius, fov, red,green,blue,ShadowMapCountI=1,ShadowMapBiasF=0.01,ColorMultiplierF=1):
		self._parent=ref(parent)
		self._node=h3d.h3dAddLightNode(parent._node, name, 0, "LIGHTING", "SHADOWMAP" );
		self._matrix=Matrix()
		self._matrix.translate(x,y,z)
		self._matrix.rotate(roll,pitch,yaw)
		h3dSetNodeTransMat(self._node, list(self._matrix))
		h3dSetNodeParamF( self._node, H3DLight.RadiusF, 0, radius );
		h3dSetNodeParamF( self._node, H3DLight.FovF, 0, fov );
		h3dSetNodeParamI( self._node, H3DLight.ShadowMapCountI, ShadowMapCountI );
		h3dSetNodeParamF( self._node, H3DLight.ShadowMapBiasF, 0, ShadowMapBiasF );
		h3dSetNodeParamF( self._node, H3DLight.ColorF3, 0, red );
		h3dSetNodeParamF( self._node, H3DLight.ColorF3, 1, green );
		h3dSetNodeParamF( self._node, H3DLight.ColorF3, 2, blue );
		h3dSetNodeParamF( self._node, H3DLight.ColorMultiplierF, 0, ColorMultiplierF );




if __name__=='__main__':
	w=Horde3DWindow(2880,1620,'xyzzy')
	p=PlayerController('demo player', w, 0,0,4563871000,0,0,0)
	w.renderView(p._camera)
	h3d.h3dSetOption( H3DOptions.LoadTextures, 1 );
	h3d.h3dSetOption( H3DOptions.TexCompression, 0 );
	h3d.h3dSetOption( H3DOptions.FastAnimation, 0 );
	h3d.h3dSetOption( H3DOptions.MaxAnisotropy, 4 );
	h3d.h3dSetOption( H3DOptions.ShadowMapSize, 2048 );
	l=Light("Light1", RootNode, 0, 15, 10, -60, 0, 0, 10, 360, 10, 10, 10.0);
	k=DisplayObject('knight',RootNode, 0,0,0,"models/knight/knight.scene.xml")
	s=DisplayObject('sphere',RootNode, 0,0,0,"models/sphere/sphere.scene.xml")
	h3dut.h3dutLoadResourcesFromDisk('/home/perkins/svn/Horde3D/Horde3D/Binaries/Content')
	h3dSetNodeTransform( s._node, 0, -20, 0, 0, 0, 0, 4563871000, 4563871000, 4563871000 );
	
	h3d.h3dSetNodeParamI( p._camera._camera, H3DCamera.ViewportXI, 0 );
	h3d.h3dSetNodeParamI( p._camera._camera, H3DCamera.ViewportYI, 0 );
	h3d.h3dSetNodeParamI( p._camera._camera, H3DCamera.ViewportWidthI, 2880 );
	h3d.h3dSetNodeParamI( p._camera._camera, H3DCamera.ViewportHeightI, 1620 );
	
	
	h3d.h3dSetOption( H3DOptions.WireframeMode, 0 );
	
	import time
	_stop=False
	def stop():
		global _stop
		_stop=True
	while not _stop:
		time.sleep(1/60.)
		w.renderView(p._camera)
	
	
