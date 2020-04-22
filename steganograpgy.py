from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location, decoded_name):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    # loop through all pixels
    for i in range(x_size):
        for j in range(y_size):
            # check to see if current pixel's red value is 0, and write to to black
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                # write black on images with 'no red'
                pixels[i, j] = (255, 255, 255)
            else:
                # write write to everything else to actually show the message
                pixels[i, j] = (0, 0, 0)

    decoded_image.save("images/{}.png".format(decoded_name))

def write_text(text, img_size):
    """Write text to an RGB image. Line wraps as well! :0"""
    img_txt = Image.new("RGB", img_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(img_txt)

    # wrap text :)
    margin = 10
    offset = 10
    for line in textwrap.wrap(text, width=160):
        drawer.text((margin, offset), line, font=font) 
        offset += 10
    return img_txt

def encode_image(text, img, encoded_name):
    """Encodes message into an image."""
    img = Image.open(img)
    red_channel = img.split()[0]
    green_channel = img.split()[1]
    blue_channel = img.split()[2]

    x_size = img.size[0]
    y_size = img.size[1]

    # txt draw
    img_txt = write_text(text, img.size)
    bw_encode = img_txt.convert('1')

    # encode txt to img
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            red_channel_pix = bin(red_channel.getpixel((i, j)))
            tencode_pix = bin(bw_encode.getpixel((i, j)))

            if tencode_pix[-1] == '1':
                red_channel_pix = red_channel_pix[:-1] + '1'
            else:
                red_channel_pix = red_channel_pix[:-1] + '0'
            pixels[i, j]  = (int(red_channel_pix, 2), green_channel.getpixel((i, j)), blue_channel.getpixel((i, j)))
    
    encoded_image.save("images/{}.png".format(encoded_name))

def main():
    a = int(input(":: Welcome to Steganography ::\n"
                "1. Encode\n2. Decode\n"))
    if a == 1:
        img = input("Enter image name (only png's): ")
        text = input("What text would you like to encode: ")
        name = input("Encoded image output name: ")
        encode_image(text, img + ".png", name)
    elif a == 2:
        img = input("Enter image name to decode (only png's): ")
        name = input("Decoded image output name: ")
        decode_image(img + ".png", name)

if __name__ == '__main__':
    main()
