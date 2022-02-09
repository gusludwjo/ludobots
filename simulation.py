import pybullet as p
import time


physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
    print (i)
p.disconnect()
