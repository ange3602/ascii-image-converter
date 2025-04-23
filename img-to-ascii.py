from PIL import Image

#ASCII_CHARS = ['@', '#', '%', '*', '+', ':', ',', '.']
ASCII_CHARS = ['.', ':', '+', '*', '%', '&', '#', '@']

def main():
    path = input("Enter image path (e.g. my_image.png): ")
    image = Image.open(path)
    ascii_art = convert(image)
    with open("output.txt", "w") as f:
        f.write(ascii_art)
    print(ascii_art)

    

def convert(image):
    # Resize the image to 100px wide
    width, height = image.size
    aspect_ratio = height/width
    new_width = 100
    new_height = aspect_ratio*new_width*0.5
    image = image.resize((new_width, int(new_height)))

    # Convert to grayscale
    image = image.convert("L")

    # Pixel data
    pixels = image.getdata()

    ascii_art = ""  
    for i, pixel in enumerate(pixels):
        if (pixel < 10):
            ascii_char = ASCII_CHARS[0]
        elif (pixel < 30):
            ascii_char = ASCII_CHARS[1]
        elif (pixel < 90):
            ascii_char = ASCII_CHARS[2]
        elif (pixel < 140):
            ascii_char = ASCII_CHARS[3]
        elif (pixel < 180):
            ascii_char = ASCII_CHARS[4]
        elif (pixel < 210):
            ascii_char = ASCII_CHARS[5]
        elif (pixel < 240):
            ascii_char = ASCII_CHARS[6]
        else:
            ascii_char = ASCII_CHARS[7]
       # ascii_char = ASCII_CHARS[pixel // 32]
        ascii_art += ascii_char

        if ((i+1)% new_width == 0):
            ascii_art+= "\n"

    
    return ascii_art

if __name__ == "__main__":
    main()
