from cmath import sin
from math import pi
import pybullet as p
import time
import pybullet_data
import numpy as np
import random
from generate import *
import pyrosim.pyrosim as pyrosim


Create_World()

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


p.setGravity(0,0,-9.8) #loading gravity
planeId = p.loadURDF("plane.urdf") #generates a plane

robotId = p.loadURDF("body.urdf") #defines a robot from .urdf file called "body.urdf"

n_steps = 1000 #number of time steps
amplitude = pi/4
frequency = 1
phaseOffset = 0

p.loadSDF("world.sdf") #load the world from a .urdf file
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(n_steps)
frontLegSensorValues = np.zeros(n_steps)

targetAngles = np.zeros(n_steps)


for i in range (n_steps):
    #targetAngles[i] = np.sin(np.deg2rad(i) * 0.4) * pi/4
    targetAngles[i] = amplitude * np.sin((frequency * i + phaseOffset))

np.save("data/targetAngles", targetAngles)



for i in range (n_steps):
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

    targetPosition = targetAngles[i],

    maxForce = 25)

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robotId,

    jointName = "Torso_FrontLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = targetAngles[i],

    maxForce = 25)
p.disconnect()

np.save("data/backLeg_sensor_data", backLegSensorValues)
np.save("data/frontLeg_sensor_data", frontLegSensorValues)
print (backLegSensorValues)
