from pyHorde3D.Horde3D import h3dWorld, h3dCamera, glfwWindow, h3dLight, h3dResource, SimpleNode, h3dut, H3DResTypes, H3DOptions

window=glfwWindow(800,600,"sphere").onInitialize()

world=h3dWorld()
c=h3dCamera(world, "objective", 0,0,1.93776e12,0,0,0)
c.windows.append(window)
l=h3dLight(world, "light1", 0, 15, 10, -60, 0, 0,10,360,)

sphere_rsrc=h3dResource(H3DResTypes.SceneGraph, "models/sphere/sphere.scene.xml", 0)
sphere=SimpleNode(world, 0, 0, 0, 0, 0, 0, sphere_rsrc)
sphere._matrix.scale(45638710000, 45638710000, 45638710000)
sphere.setTransform()


h3dut.h3dSetOption( H3DOptions.WireframeMode, 0 );
import time
for i in range(600):
    world.update()
    time.sleep(1/60.)
    c.translate(0,0,-16666666666.66666/5.3)
    
