

import os
from PIL import Image, ImageEnhance, ImageFilter

# Ask the user to input the path to the image file
image_path = input("Please enter the path to your image file: ").strip()

# Load the image
image = Image.open(image_path)

# Get the base name (file name without extension)
base_name = os.path.splitext(os.path.basename(image_path))[0]

# Create a folder for saving images if it doesn't exist
output_folder = "generated_images"
os.makedirs(output_folder, exist_ok=True)

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

# Save the edited images with the base name
gray_image.save(os.path.join(output_folder, f"{base_name}_gray.jpg"))
blurred_image.save(os.path.join(output_folder, f"{base_name}_blur.jpg"))
bright_image.save(os.path.join(output_folder, f"{base_name}_bright.jpg"))
contrast_image.save(os.path.join(output_folder, f"{base_name}_contrast.jpg"))

# Show all the images
image.show(title="Original Image")
gray_image.show(title="Grayscale Image")
blurred_image.show(title="Blurred Image")
bright_image.show(title="Brighter Image")
contrast_image.show(title="High Contrast Image")

print(f"✅ Image processing complete! Check your 'generated_images' folder for the new images.")
