import pyrosim.pyrosim as pyrosim
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    lenght = 1
    width = 1
    height = 1
    x = 0
    y = 0
    z = height/2

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[lenght,width, height])


    pyrosim.End()