from PIL import Image

def resize_image(image_name, multiplier):
    with Image.open(image_name) as img:
        width, height = img.size
        new_width = int(width / multiplier)
        new_height = int(height / multiplier)
        resized_img = img.resize((new_width, new_height))
        output_name = f"resized_{image_name}"
        resized_img.save(output_name)
        print(f"Resized image saved as: {output_name}")

image_name = input("Enter the image filename: ")
multiplier = float(input("Enter the resize multiplier (e.g., 2 for half size): "))

resize_image(image_name, multiplier)
