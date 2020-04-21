from PIL import Image, ImageFont, ImageDraw

def decode_image(file_location):
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

    decoded_image.save("images/decoded_image.png")

if __name__ == '__main__':
    decode_image('images/encoded_sample.png')
