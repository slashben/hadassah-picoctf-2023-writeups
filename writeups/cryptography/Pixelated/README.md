# Pixelated
This is the write-up for the challenge "Pixelated" challenge in PicoCTF

# The challenge

# Description
I have these 2 images, can you make a flag out of them
this is the images:


![](img/scrambled1.png)
![](img/scrambled2.png)


# Hints
1. Look at this site: https://en.wikipedia.org/wiki/Visual_cryptography - about "Visual cryptography"
2. Think of different ways you can "stack" images

# Solution
Add the two images together to get the flag. 
This approach can be seen in this code running:


import numpy as np
from PIL import Image

# Open images
im1 = Image.open("scrambled1.png")
im2 = Image.open("scrambled2.png")

# Make into Numpy arrays
im1np = np.array(im1)
im2np = np.array(im2)

# Add images
result = im2np + im1np
# Convert back to PIL image and save
Image.fromarray(result).save('result.png')


The flag is:
![](img/result.png)


