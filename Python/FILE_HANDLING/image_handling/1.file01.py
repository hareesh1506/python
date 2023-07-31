from PIL import Image
"""
# open an image
image_path = "C://Users//mycom//Downloads//wallpaperflare.com_wallpaper.jpg"
image = Image.open(image_path)

# display image info
print("Image format:", image.format)
print("Image size:", image.size)
print("Image mode:", image.mode)

# show image
image.show()

# Convert the image to grayscale
grayscale_image = image.convert('L')

# Save the grayscale image
grayscale_image.save('grayscale_image.jpg')

# Close the image
image.close()
"""

# CODE-2

"""
# Open an image file
with Image.open("C://Users//mycom//Downloads//wallpaperflare.com_wallpaper.jpg") as image:
    # Display image information
    print("Image format:", image.format)
    print("Image size:", image.size)
    print("Image mode:", image.mode)

    # Show the image
    image.show()

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Save the grayscale image
    grayscale_image.save('grayscale_image.jpg')

# Open the saved grayscale image
with Image.open('grayscale_image.jpg') as grayscale_image:
    # Show the grayscale image
    grayscale_image.show()
"""

# CODE-3

with Image.open("C://Users//mycom//Downloads//pexels-danne-516541.jpg")as image:
    image.show()
