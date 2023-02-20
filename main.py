from PIL import Image, ImageFont, ImageDraw

# img = Image.open('nikolaenkov-70-10.10.19-1.jpg')
img = Image.new("RGB", (512, 512), "black")
font_size = img.size[0] // 5
draw = ImageDraw.Draw(img)
fontAwesome = ImageFont.truetype('./fonts/Font Awesome 6 Free-Solid-900.otf', size=font_size)
calibri = ImageFont.truetype('fonts/calibri.ttf', size=font_size)
# text = chr(0xf071) # warning
# text = chr(0xf058)
# text = chr(0xe4fd)
icon = chr(0xf058)
text = 'Норма'
print(img.size)
draw.text(xy=(img.size[0] // 2, img.size[1] // 2), text=icon, font=fontAwesome, fill="green", anchor="md")
draw.text(xy=(img.size[0] // 2, img.size[1] // 2), text=text, font=calibri, fill="yellow", anchor="ma")

img.save("output.png")