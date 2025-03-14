from PIL import Image

img = Image.open('image1.png')
data = img.load()
bg_color = data[0, 0]
left, right = img.width, 0
top, bottom = img.height, 0

for y in range(img.height):
    for x in range(img.width):
        if data[x, y] != bg_color:
            if x < left:
                left = x
            if x > right:
                right = x
            if y < top:
                top = y
            if y > bottom:
                bottom = y

result = img.crop((left, top, right + 1, bottom + 1))
result.save('res.png')