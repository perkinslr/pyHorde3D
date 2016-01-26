#  Horde3D.py
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
H3DRootNode = 1

import h3d
import os
ffi=h3d.ffi
h3dut=h3d.h3dut

globals().update(h3d.symbols)
from matrix import Matrix
glfwWindows=[]

class glfwWindow:
    opened=False
    initialized=False
    def __init__(self, width, height, title, monitor=None):
        if monitor is None:
            monitor = ffi.NULL
        self._width=width
        self._height=height
        self.title=title
        self._monitor=monitor
        glfwWindows.append(self)
    def onInitialize(self):
        self.preinit()
        self._window=glfwCreateWindow(self._width, self._height, self.title, self._monitor, ffi.NULL)
        self.makeCurrent()
        self.opened=True
        return self
    @classmethod
    def preinit(cls):
        if cls.initialized:
            return
        cls.initialized=True
        glfwInit()
    def makeCurrent(self):
        glfwMakeContextCurrent(self._window)
    def setCamera(self, cam):
        self._camera=cam
    def update(self):
        glfwSwapBuffers(self._window)
        
class h3dResource(object):
    def __init__(self, type_=H3DResTypes.SceneGraph, path=None, subpart=0):
        self._rsrc=h3dAddResource(type_, path, subpart)
        h3dutLoadResourcesFromDisk(os.environ.get("H3DCONTENT"))

class h3dNode(object):
    nodes={}
    def __init__(self, parent,x,y,z,roll,pitch,yaw):
        self.parent=parent
        while parent.parent:
            parent=parent.parent
        self.world=parent
        m=self._matrix=Matrix()
        m.translate(x,y,z)
        m.rotate(roll,pitch,yaw)
        self.setTransform()
        self.nodes[self._node]=self
    def setTransform(self):
        h3dSetNodeTransMat(self._node, list(self._matrix))
    def translate(self, x, y, z):
        self._matrix.translate(x,y,z)
        self.setTransform()
    def rotate(self, r, p, w):
        self._matrix.rotate(r,p,w)
        self.setTransform()
    def scale(self,sx,sy,sz):
        self._matrix.scale(sx,sy,sz)
        self.setTransform()

class SimpleNode(h3dNode):
    def __init__(self, parent, x, y, z, r, p, w, rsrc):
        self._node=h3dAddNodes(parent._node, rsrc._rsrc)
        super(SimpleNode, self).__init__(parent,x,y,z,r,p,w)

class h3dWorld(h3dNode):
    def __init__(self):
        h3dInit()
        self.parent=None
        self._node=H3DRootNode
        self.cameras=[]
        self.nodes[1]=self
        h3dSetOption( H3DOptions.LoadTextures, 1 );
        h3dSetOption( H3DOptions.TexCompression, 0 );
        h3dSetOption( H3DOptions.FastAnimation, 0 );
        h3dSetOption( H3DOptions.MaxAnisotropy, 4 );
        h3dSetOption( H3DOptions.ShadowMapSize, 2048 );
        h3dSetOption(H3DOptions.MaxLogLevel,0)
    def addCamera(self,camera):
        self.cameras.append(camera)
    def update(self):
        for camera in self.cameras:
            camera.render()
            h3dFinalizeFrame()
            camera.update()
            
    
        

class h3dCamera(h3dNode):
    def __init__(self, parent, name, x,y,z,roll,pitch,yaw):
        forwardPipeRes = h3dAddResource( H3DResTypes.Pipeline, "pipelines/forward.pipeline.xml", 0 );
        h3dResizePipelineBuffers( forwardPipeRes, 800, 600 );
        self._hdrPipeRes = h3dAddResource( h3d.H3DResTypes.Pipeline, "pipelines/hdr.pipeline.xml", 0 );
        self._node=h3dAddCameraNode(parent._node,name,self._hdrPipeRes)
        h3dSetupCameraView(self._node, 60, 4/3., 0.1, 1.93776e13)
        h3dSetNodeParamI( self._node, H3DCamera.ViewportXI, 0 );
        h3dSetNodeParamI( self._node, H3DCamera.ViewportYI, 0 );
        h3dSetNodeParamI( self._node, H3DCamera.ViewportWidthI, 800 );
        h3dSetNodeParamI( self._node, H3DCamera.ViewportHeightI, 600 );
        h3dSetupCameraView(self._node, 60, 4/3., 0.1, 1.93776e13)
        super(h3dCamera,self).__init__(parent,x,y,z,roll,pitch,yaw)
        self.windows=[]
        self.world.addCamera(self)
        h3dSetNodeParamI( self._node, H3DCamera.ViewportXI, 0 );
        h3dSetNodeParamI( self._node, H3DCamera.ViewportYI, 0 );
        h3dSetNodeParamI( self._node, H3DCamera.ViewportWidthI, 800 );
        h3dSetNodeParamI( self._node, H3DCamera.ViewportHeightI, 600 );

    def render(self):
        h3dRender(self._node)
    def update(self):
        for window in self.windows:
            window.update()
    
class h3dLight(h3dNode):
    def __init__(self, parent, name, x,y,z,r,p,w,radius,fov,rsrc=None,lcontext="LIGHTING",scontext="SHADOWMAP"):
        self._node=h3dAddLightNode(parent._node, name, rsrc._rsrc if rsrc else 0, lcontext,scontext );
        super(h3dLight,self).__init__(parent,x,y,z,r,p,w)
        h3dSetNodeParamF( self._node, H3DLight.RadiusF, 0, radius );
        h3dSetNodeParamF( self._node, H3DLight.FovF, 0, fov );
        h3dSetNodeParamI( self._node, H3DLight.ShadowMapCountI, 1 );
        h3dSetNodeParamF( self._node, H3DLight.ShadowMapBiasF, 0, 0.1 );
        h3dSetNodeParamF( self._node, H3DLight.ColorF3, 0, 10 );
        h3dSetNodeParamF( self._node, H3DLight.ColorF3, 1, 10 );
        h3dSetNodeParamF( self._node, H3DLight.ColorF3, 2, 10 );
        h3dSetNodeParamF( self._node, H3DLight.ColorMultiplierF, 0, 1 );
    
        
