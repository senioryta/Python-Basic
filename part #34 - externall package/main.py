from PIL import Image
import numpy as np

img = Image.open("1.jpg")

print("image format " + img.format)
print("image size " + str(img.size))
print("image mode " + img.mode)

img.show()

print(20*"-")

a = np.array([1,2,3])
b = np.array([10,5,2.5])

print(a + b)