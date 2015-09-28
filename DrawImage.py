# Demo to add rotated text to an image using PIL

import Image
import ImageFont, ImageDraw, ImageOps

im=Image.open("2.png")

f = ImageFont.truetype("/home/aswin/evalvon/rajpark/stat/css/avantgarde.otf",14)

name_txt=Image.new('L', (500,500))
name_block = ImageDraw.Draw(name_txt)
name_block.text( (15, 38), "John Hughes",  font=f, fill=255)
w=name_txt.rotate(0,  expand=3)
im.paste( ImageOps.colorize(w, (0,0,0), (255,203,4)), (242,60),  w)

phone_txt = Image.new('L',(500,500))
phone_block = ImageDraw.Draw(phone_txt)
phone_block.text( (15,70), "9869032684", font=f, fill=255)
w=phone_txt.rotate(0,  expand=3)
im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

comp_txt= Image.new('L',(500,500))
comp_block = ImageDraw.Draw(comp_txt)
comp_block.text( (30,98), "Bank of Baroda", font=f, fill=255)
w=comp_txt.rotate(0,  expand=3)
im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

route_txt= Image.new('L',(500,500))
route_block = ImageDraw.Draw(route_txt)
route_block.text( (10,124), "Kandivail - BKC", font=f, fill=255)
w=route_txt.rotate(0,  expand=3)
im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

valid_txt= Image.new('L',(500,500))
valid_block = ImageDraw.Draw(valid_txt)
valid_block.text( (35,152), "31 October, 2015", font=f, fill=255)
w=valid_txt.rotate(0,  expand=3)
im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

time_txt= Image.new('L',(500,500))
time_block = ImageDraw.Draw(time_txt)
time_block.text( (17,180), "Morning/Evening", font=f, fill=255)
w=time_txt.rotate(0,  expand=3)
im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

photo = Image.open("1.png")
size = 180,300
#photo.thumbnail(size,Image.ANTIALIAS)
photo = photo.resize((160,160),Image.ANTIALIAS)
im.paste(photo,(18,100),photo)

im.save("4.png")
