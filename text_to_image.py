from PIL import Image, ImageDraw 
text = str(input("Enter your text:"))
W, H = (200, 200)
image = Image.new("RGB", (200, 200))
draw = ImageDraw.Draw(image)
w, h = draw.textsize(text)
draw.text(((W-w)/2,(H-h)/2), text, fill="white")
image.save("result.png", "PNG")