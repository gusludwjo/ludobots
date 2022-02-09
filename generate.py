import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
lenght = 1
width = 1
height = 1
x = 0
y = 0
z = height/2
#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[lenght,width, height])
#pyrosim.Send_Cube(name="Box2", pos=[x+lenght,y,z+height] , size=[lenght,width, height])

for i in range (3):
    x=0
    y+=1.1
    for j in range (3):
        lenght = 1
        width = 1
        height = 1
        z= height/2
        x+=1.1
        for k in range (10): #box-stacking loop
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[lenght,width, height])
            z+=1
            lenght*=0.9
            width*=0.9
            height*=0.9


pyrosim.End()