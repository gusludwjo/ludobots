from cProfile import label
import numpy as np
import matplotlib.pyplot as pp

backLegSensorValues = np.load("data/backLeg_sensor_data.npy")
frontLegSensorValues = np.load("data/frontLeg_sensor_data.npy")
targetAngles = np.load("data/targetAngles.npy")

print (backLegSensorValues)
print (frontLegSensorValues)

#pp.plot(backLegSensorValues, label="BackLeg", linestyle="solid", linewidth=2) #plotting sensordata from backLeg
#p.plot(frontLegSensorValues, label="FrontLeg", linestyle="dashed", linewidth=1) #plotting sensordata from fronLeg
pp.plot(targetAngles)

pp.legend()
pp.show()
