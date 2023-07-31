from PIL import Image

# Open the image file
image = Image.open("C:/Users/mycom/PycharmProjects/pythonLearning/Image/ganesh.jpg")

# Display basic information about the image
print("Image Format:", image.format)
print("Image Size:", image.size)
print("Image Mode:", image.mode)

# Display the image using the default image viewer
image.show()




