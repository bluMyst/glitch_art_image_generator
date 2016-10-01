from PIL import Image

def image_map(image, f):
    ''' f(x,y) should return a pixel value (generally 3-int tuple) '''
    for y in xrange(image.height):
        for x in xrange(image.width):
            image.putpixel((x, y), f(x, y))

    return image

if __name__ == '__main__':
    import sys

    def f(x, y):
        return (x**y & 0xFF, y**x & 0xFF, y**2 & 0xFF)

    image = image_map(Image.new('HSV', (100, 100)), f)
    print('HSV')
    image.show()

    image = image_map(Image.new('RGB', (100, 100)), f)
    print('RGB')
    image.show()

    #image.convert('RGB').save('generated_image.png')
