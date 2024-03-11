from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels
            encrypted_pixel = (b, g, r)

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # swapping red and blue channels back
            decrypted_pixel = (b, g, r)

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrpted successfully!")

  # image path
    input_image = r"C:\Users\Dell\Desktop\Prodigy_CS-02\input.jpg"
    encrypt_image = r"C:\Users\Dell\Desktop\Prodigy_CS-02\decrypt_image.jpg"
    decrypt_image = r"C:\Users\Dell\Desktop\Prodigy_CS-02\encrypt_image.jpg"


    # Encrypt the image
    encrypt_image(input_image, encrypt_image, key=None)

    # Decrypt the image
    decrypt_image(encrypt_image, decrypt_image, key=None)