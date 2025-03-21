from PIL import Image, ImageEnhance, ImageFilter

# Load the image
image_path = "20.jpg"  # Change this to your image file
image = Image.open(image_path)

# Convert to grayscale
gray_image = image.convert("L")

# Apply blur filter
blurred_image = image.filter(ImageFilter.BLUR)

# Adjust brightness (1.5 times brighter)
brightness_enhancer = ImageEnhance.Brightness(image)
bright_image = brightness_enhancer.enhance(1.5)

# Adjust contrast (1.8 times higher contrast)
contrast_enhancer = ImageEnhance.Contrast(image)
contrast_image = contrast_enhancer.enhance(1.8)

# Save the edited images
gray_image.save("gray_sample.jpg")
blurred_image.save("blur_sample.jpg")
bright_image.save("bright_sample.jpg")
contrast_image.save("contrast_sample.jpg")

# Show all the images
image.show(title="Original Image")
gray_image.show(title="Grayscale Image")
blurred_image.show(title="Blurred Image")
bright_image.show(title="Brighter Image")
contrast_image.show(title="High Contrast Image")

print("✅ Image processing complete! Check your directory for the new images.")
