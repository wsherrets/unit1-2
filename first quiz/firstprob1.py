print ("Hey, please write your name, then the height, width, and length of your pool.")
name = input(1)
lengthorrad = int(input(2))
width = int(input(3))
height = int(input(4))

cysum =  lengthorrad * height // 5.78

squaresum = lengthorrad * width * height // 7.5

print (name)
print ("cylindrical:" +str(cysum))
print ("square:" +str(squaresum))