
import Image
import ImageFont, ImageDraw, ImageOps
from pyexcel_xls import get_data
import json



details = get_data("details.xls")

for customer_detail in details["Sheet1"]:
        
	im=Image.open("2.png")

	f = ImageFont.truetype("avantgarde.otf",14)

	name_txt=Image.new('L', (500,500))
	name_block = ImageDraw.Draw(name_txt)
	name_block.text( (15, 38), customer_detail[0],  font=f, fill=255)
	w=name_txt.rotate(0,  expand=3)
	im.paste( ImageOps.colorize(w, (0,0,0), (255,203,4)), (242,60),  w)

	phone_txt = Image.new('L',(500,500))
	phone_block = ImageDraw.Draw(phone_txt)
	phone_block.text( (15,70), str(customer_detail[1]), font=f, fill=255)
	w=phone_txt.rotate(0,  expand=3)
	im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

	comp_txt= Image.new('L',(500,500))
	comp_block = ImageDraw.Draw(comp_txt)
	comp_block.text( (30,98), customer_detail[2], font=f, fill=255)
	w=comp_txt.rotate(0,  expand=3)
	im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

	route_txt= Image.new('L',(500,500))
	route_block = ImageDraw.Draw(route_txt)
	route_block.text( (10,124),customer_detail[3], font=f, fill=255)
	w=route_txt.rotate(0,  expand=3)
	im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

	valid_txt= Image.new('L',(500,500))
	valid_block = ImageDraw.Draw(valid_txt)
	valid_block.text( (35,152), customer_detail[4], font=f, fill=255)
	w=valid_txt.rotate(0,  expand=3)
	im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

	time_txt= Image.new('L',(500,500))
	time_block = ImageDraw.Draw(time_txt)
	time_block.text( (17,180), customer_detail[5], font=f, fill=255)
	w=time_txt.rotate(0,  expand=3)
	im.paste( ImageOps.colorize(w, (0,0,0), (0,0,0)), (242,60),  w)

        if "Morning" in customer_detail[5] and "Evening" in customer_detail[5]:
            morning = Image.open("morning.png").resize((25,25),Image.ANTIALIAS)
            im.paste(morning,(380,240),morning)
            
            evening = Image.open("evening.png").resize((25,25),Image.ANTIALIAS)
            im.paste(evening,(405,240),evening)

        elif "Morning" in customer_detail[5]:
            morning = Image.open("morning.png").resize((25,25),Image.ANTIALIAS)
            im.paste(morning,(320,240),morning)

        elif "Evening" in customer_detail[5]:
            evening = Image.open("evening.png").resize((25,25),Image.ANTIALIAS)
            im.paste(evening,(320,240),evening)

	photo = Image.open(customer_detail[6])
	size = 180,300
	#photo.thumbnail(size,Image.ANTIALIAS)
	photo = photo.resize((160,160),Image.ANTIALIAS)
	im.paste(photo,(18,100),photo)

	im.save(customer_detail[0] + "_" + str(customer_detail[1]) + ".png")
