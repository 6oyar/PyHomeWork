from PIL import Image, ImageDraw
from datetime import datetime
#Программа сравнивает две картинки, в случае различий в журнал записываются дата и время
img1 = Image.open('pic1.jpg')
img2 = Image.open('pic2.jpg')
ans = Image.open('pic1.jpg')
draw = ImageDraw.Draw(ans)
pix1 = img1.load()
pix2 = img2.load()

width = min(img1.size[0], img2.size[0])
height = min(img1.size[1], img2.size[1])

cleanpixel = (255, 255, 255)
hasChanged = False
for i in range (width):
    for j in range(height):
        dx1 = pix1[i, j][0] - pix2[i, j][0]
        dx2 = pix1[i, j][1] - pix2[i, j][1]
        dx3 = pix1[i, j][2] - pix2[i, j][2]
        draw.point((i, j), (255 - abs(dx1), 255-abs(dx2), 255 - abs(dx3)))
        if(cleanpixel != ans.getpixel((i,j))):
            hasChanged = True

ans.save('ans.jpg', "JPEG")
if(hasChanged):
    f = open('log.txt', 'a')
    currentdate =  str(datetime.now())
    f.write('Изменения зафиксированы:' + currentdate + '\n')
    f.close()
del draw
