from PIL import Image, ImageOps, ImageDraw

def get_circular_img(image):
    bigsize = (image.size[0] * 3, image.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(image.size, Image.ANTIALIAS)
    image.putalpha(mask)
    return image