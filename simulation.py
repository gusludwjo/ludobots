import pybullet as p
import time
import pybullet_data
import numpy as np
from generate import *
import pyrosim.pyrosim as pyrosim

Create_World()

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8) #loading gravity
planeId = p.loadURDF("plane.urdf") #generates a plane

robotId = p.loadURDF("body.urdf") #defines a robot from .urdf file called "body.urdf"

p.loadSDF("world.sdf") #load the world from a .urdf file
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)


for i in range (1000):
    p.stepSimulation()
    time.sleep(1./240.)
    backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    backLegSensorValues[i] = backLegTouch
    frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    frontLegSensorValues[i] = frontLegTouch
    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = "Torso_BackLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = 0.0,

    maxForce = 500)
p.disconnect()

np.save("data/backLeg_sensor_data", backLegSensorValues)
np.save("data/frontLeg_sensor_data", frontLegSensorValues)
print (backLegSensorValues)
