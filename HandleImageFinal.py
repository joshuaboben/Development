from HandleImage import HandleImage
from PIL import Image, ImageFilter
import os



img_list = []
CurrPath = "C:/original_pictures/"
img_list =  os.listdir(CurrPath)          
for i  in range(len(img_list)):
    Img = HandleImage(CurrPath+img_list[i])
    Img.thumbNailFile()
    Img.blurImage()
    Img.addBorder('Yellow')
    Img.addBorder('Red')
    Img.contourImageSupplied()
    Img.addTextToPic("Photos for Demo", "Red", (105,105), "arial.ttf", 22)
    Img.blendImage()
    

    
NewPath = "C:/output_pictures/"
img_list_out = []
img_list_out =  os.listdir(NewPath)
for y  in range(len(img_list_out)):
    imgx = Image.open(NewPath+img_list_out[y])
    imgx.show()
    
    