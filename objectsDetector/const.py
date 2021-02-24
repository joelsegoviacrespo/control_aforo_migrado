import random 

classes = ["Background", "Beroplane", "Bicycle", "Bird", "Boat","Bottle", "Bus", "Car", "Cat", "Chair", "Cow", "Diningtable","Dog", "Horse", "Motorbike", "Person", "Pottedplant", "Sheep", "Sofa", "Train", "Tvmonitor"]

colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for i in classes]