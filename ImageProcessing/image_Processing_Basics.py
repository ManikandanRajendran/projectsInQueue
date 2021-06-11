from PIL import Image, ImageFilter

# use dir() command to list the available options of library

img = Image.open('./images/ironman.png')
# print(img.format)  # to check image format
# print(img.size)  # to check image size
# print(img.mode)  # to check image mode

# Filter image using ImageFilter
# blur = img.filter(ImageFilter.SHARPEN) # BLUR, SMOOTH, SHARPEN
# blur.save('mdsharpen.png', 'png')

# convert images
# convert = img.convert('L')
# rotate() will rotate the image and store it in object
# rotated = convert.rotate(180)

# resize() will helps to resize image - it will compress the image instead we can use thumbnail
# rotated = rotated.resize((300, 300))

# thumbnail will keep the images pixels as it is during resize
img.thumbnail((400,400))

# show() will show the images after converting
# img.show()

# save(0 will save the image in given format
img.save('converted.png', 'png')
