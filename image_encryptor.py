from PIL import Image
import os

def swap_pixels(image):
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(0, width - 1, 2):
            pixel1 = pixels[x, y]
            pixel2 = pixels[x + 1, y]
            pixels[x, y] = pixel2
            pixels[x + 1, y] = pixel1

    return image

def apply_math_operation(image, operation):
    pixels = image.load()
    width, height = image.size

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if operation == "invert":
                pixels[x, y] = (255 - r, 255 - g, 255 - b)
            elif operation == "increase":
                pixels[x, y] = (min(255, r + 10), min(255, g + 10), min(255, b + 10))
            elif operation == "decrease":
                pixels[x, y] = (max(0, r - 10), max(0, g - 10), max(0, b - 10))

    return image

def main():
    print("Simple Image Encryption Tool 🔒")
    path = input("Enter the path to your image: ")

    if not os.path.isfile(path):
        print("Error: File not found. Please check the path.")
        return

    try:
        image = Image.open(path)
        image = image.convert("RGB")  # Ensure RGB format
    except Exception as e:
        print("Error: Could not open the image. Make sure it's a valid image file.")
        print("Details:", e)
        return

    print("Choose an operation:")
    print("1. Swap pixel values")
    print("2. Invert colors")
    print("3. Increase brightness")
    print("4. Decrease brightness")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        encrypted_image = swap_pixels(image)
    elif choice == "2":
        encrypted_image = apply_math_operation(image, "invert")
    elif choice == "3":
        encrypted_image = apply_math_operation(image, "increase")
    elif choice == "4":
        encrypted_image = apply_math_operation(image, "decrease")
    else:
        print("Invalid choice.")
        return

    output_path = input("Enter the output file path (e.g., encrypted.png): ")
    try:
        encrypted_image.save(output_path)
        print("Encryption complete! Encrypted image saved as:", output_path)
    except Exception as e:
        print("Error: Could not save the image.")
        print("Details:", e)

if __name__ == "__main__":
    main()
