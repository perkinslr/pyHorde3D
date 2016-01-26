Currently 3 examples

####window.py
Initializes the window system, sleeps, then exits

####sphere.py
Creates a window
Creates a h3dWorld
Loads a light, camera, sphere
runs 600 frames, moving the camera toward the sphere each frame

####thin.py
Similar to sphere.py, but directly using the h3d.py thin wrapper.
Demonstrates directly calling functions from libHorde3D


To use these examples

set H3DCONTENT to your sample content folder from Horde3D

either copy pyHorde3D onto your python path, or set PYTHONPATH to the location of pyHorde3D

run python examples/...
