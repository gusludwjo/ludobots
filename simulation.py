import pybullet as p
import time
import pybullet_data
import numpy as np
from generate import *
import pyrosim.pyrosim as pyrosim

Create_World()

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")

robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(200)
frontLegSensorValues = np.zeros(200)


for i in range (200):
    p.stepSimulation()
    time.sleep(1./240.)
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i] = backLegTouch
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    frontLegSensorValues[i] = frontLegTouch
p.disconnect()

np.save("data/backLeg_sensor_data", backLegSensorValues)
np.save("data/frontLeg_sensor_data", frontLegSensorValues)
print (backLegSensorValues)
