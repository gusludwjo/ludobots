from cProfile import label
import numpy as np
import matplotlib.pyplot as pp

backLegSensorValues = np.load("data/backLeg_sensor_data.npy")
frontLegSensorValues = np.load("data/frontLeg_sensor_data.npy")

print (backLegSensorValues)
print (frontLegSensorValues)

pp.plot(backLegSensorValues, label="BackLeg", linestyle="solid", linewidth=2)
pp.plot(frontLegSensorValues, label="FrontLeg", linestyle="dashed", linewidth=1)

pp.legend()
pp.show()
