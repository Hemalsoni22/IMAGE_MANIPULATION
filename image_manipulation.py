from PIL import Image
import numpy as np

while True:
    choice = input("select (e)ncryption, (d)ecryption or (q)uit: ").lower()
    if choice == 'e':
        encryptIt()
        continue
    elif choice == 'd':
        decryptIt()
        continue
    elif choice == 'q':
        print("Exitting the program.")
        break
    else:
        print("Invalid choice. Please choose 'e' for encryption, 'd' for decryption, or 'q' to quit.")

def encryptIt():
    try:
        key = int(input("Enter encryption key: ")) 
    except ValueError:
        print("Invalid encryption key. Please enter a valid integer.")
        encryptIt()
        return

    image_location = input("Enter name of the image: ")
    try:
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")
        encryptIt()

def encrypt_image(image_location, key):
    original_image = Image.open(image_location)

    #converting image into array by numpy
    image_array = np.array(original_image)
    encrypted_pixels = (image_array + key) % 256

    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save('/content/encrypted.png')
    print("Image encryption completed")

def decryptIt():
    try:
        key = int(input("Enter decryption key: ")) 
    except ValueError:
        print("Invalid decryption key. Please enter a valid integer.")
        decryptIt()
        return
    
    image_location = input("Enter name of the image: ")
    try:
        decrypt_image(image_location, key)
    except FileNotFoundError:
        print("Invalid location. Image not found. Please try again.")
        decryptIt()

def decrypt_image(image_location, key):
    original_image = Image.open(image_location)

    #converting image into array by numpy
    image_array = np.array(original_image)
    decrypted_pixels = (image_array - key) % 256

    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save('/content/decrypted.png')
    print("Image decryption completed")
