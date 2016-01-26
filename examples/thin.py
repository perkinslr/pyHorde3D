from h3d import *
import os
glfwInit()
w1=glfwCreateWindow(800,600,"hello1", ffi.NULL, ffi.NULL)
glfwMakeContextCurrent(w1)
h3dInit()

glfwSwapBuffers(w1)


h3dSetOption( H3DOptions.LoadTextures, 1 );
h3dSetOption( H3DOptions.TexCompression, 0 );
h3dSetOption( H3DOptions.FastAnimation, 0 );
h3dSetOption( H3DOptions.MaxAnisotropy, 4 );
h3dSetOption( H3DOptions.ShadowMapSize, 2048 );

light = h3dAddLightNode(1, "light1", 0, "LIGHTING", "SHADOWMAP" );
h3dSetNodeTransform( light, 0, 15, 10, -60, 0, 0, 1, 1, 1 );
h3dSetNodeParamF( light, H3DLight.RadiusF, 0, 10 );
h3dSetNodeParamF( light, H3DLight.FovF, 0, 360 );
h3dSetNodeParamI( light, H3DLight.ShadowMapCountI, 1 );
h3dSetNodeParamF( light, H3DLight.ShadowMapBiasF, 0, 0.1 );
h3dSetNodeParamF( light, H3DLight.ColorF3, 0, 10 );
h3dSetNodeParamF( light, H3DLight.ColorF3, 1, 10 );
h3dSetNodeParamF( light, H3DLight.ColorF3, 2, 10 );
h3dSetNodeParamF( light, H3DLight.ColorMultiplierF, 0, 1 );

hdr_resource=h3dAddResource(H3DResTypes.Pipeline, "pipelines/hdr.pipeline.xml", 0 )
h3dResizePipelineBuffers( hdr_resource, 800, 600 );
forwardPipeRes = h3dAddResource( H3DResTypes.Pipeline, "pipelines/forward.pipeline.xml", 0 );
h3dResizePipelineBuffers( forwardPipeRes, 800, 600 );

h3dut.h3dutLoadResourcesFromDisk(os.environ.get('H3DCONTENT',''))
camera=h3dAddCameraNode(1, "camera", hdr_resource)

h3dSetupCameraView(camera, 60, 4/3., 0.1, 1.93776e13)
h3dSetNodeTransform(camera, 0,1000,1.93776e12,0,0,0,1,1,1)



h3dRender(camera)
spherer=h3dAddResource(H3DResTypes.SceneGraph, "models/sphere/sphere.scene.xml", 0)
h3dut.h3dutLoadResourcesFromDisk(os.environ.get('H3DCONTENT',''))
sphere=h3dAddNodes(1, spherer)
h3dSetNodeTransform( sphere, 0, -20, 0, 0, 0, 0, 45638710000, 45638710000, 45638710000 );


h3dSetNodeParamI( camera, H3DCamera.ViewportXI, 0 );
h3dSetNodeParamI( camera, H3DCamera.ViewportYI, 0 );
h3dSetNodeParamI( camera, H3DCamera.ViewportWidthI, 800 );
h3dSetNodeParamI( camera, H3DCamera.ViewportHeightI, 600 );


h3dSetOption( H3DOptions.WireframeMode, 0 );















import time
for i in range(600):
    glfwPollEvents()
    h3dRender(camera)
    h3dFinalizeFrame()
    glfwSwapBuffers(w1)
    time.sleep(1/60.)
    h3dSetNodeTransform(camera, 0,0,1.93776e13-i*166666666666.66666/5.2,15,15,0,1,1,1)
    
