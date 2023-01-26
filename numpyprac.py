import numpy as np
import random

# Creates an array that is 0 -> 69 with a step of 1
arr = np.array(range(0,70))
# Creates a copy of the originial before changing for comparison
# UC means unchanged
arrUC = arr

# A while loop that changes 21 of the numbers to be pseudo-random everytime I run the command
i = 1
while i < 23:
    # You cannot use random.randint(0,70) because offset 70 does not exist!
    randoffset = random.randint(0,69)
    arr[randoffset] = random.randint(0,100)
    i += 1

# A bunch of possible things to do with numpy arrays
# Note these will be different everytime because our while loop runs everytime
print(np.sum(arr))
print(np.mean(arr))
print(np.average(arr))
print(np.std(arr))
print(np.prod(arr))
# np.max and np.min may also be helpful

# The following is examples of usage of np.any() and np.all()
print(f'''Using the np.any() command we can tell whether any values in arr are greater than 70 
and the answer is: {np.any(arr > 70)}''')

print(f'''Using the np.all() command we can tell if all the values in arr are greater than 70 
and the answer is {np.all(arr > 70)}''')

# np.argmax() and np.argmin() return the offset of the max or min value respectively
arrMaxOffset = np.argmax(arr)
arrUCMaxOffset = np.argmax(arrUC)

print(f'arr and arrUC have their maximum value at the same offset: {arrMaxOffset == arrUCMaxOffset}')

# I love NUMPY
#ILN = 'I love NUMPY!'
#for i in range(0,100):
#    print(ILN)