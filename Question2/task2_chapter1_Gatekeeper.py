from PIL import Image
import time

# Generate the number
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

# Use a relative path if the image is in the same directory as the script
image_path = 'Chapter1.jpg'
new_image_path = 'chapter1out.png'

# Load the image
try:
    image = Image.open(image_path)
    pixels = image.load()

    # Create a new image to store the modified pixels
    new_image = Image.new('RGB', image.size)

    # Process each pixel
    red_sum = 0
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            # Add generated_number to each RGB component
            new_r = min(r + generated_number, 255)
            new_g = min(g + generated_number, 255)
            new_b = min(b + generated_number, 255)
            new_image.putpixel((i, j), (new_r, new_g, new_b))
            # Add to the sum of red pixel values
            red_sum += new_r

    # Save the new image
    new_image.save(new_image_path)

    # Print the sum of the red pixel values
    print(red_sum)

except FileNotFoundError:
    print(f"File not found: {image_path}")
except Exception as e:
    print(f"An error occurred: {e}")
