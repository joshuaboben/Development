from PIL import Image, ImageFilter, ImageOps, ImageFont, ImageDraw
import os

class HandleImage:
   "image handling class" 
   def __init__(self, SourceFile):       
       self.Fname = SourceFile 
       self.small_size = (64,  64)                                                         
   def saveFileAsPNG(self):
        "this will save the file as .png"
        if (os.path.splitext(self.Fname)[1] != "PNG" and os.path.splitext(self.Fname)[1] != "png"):
           newFileName = os.path.splitext(self.Fname)[0] + ".png"
           img = Image.open(self.Fname)
           img.save(newFileName)                     
   def saveFileasBMP(self):
       "this will save the file as .bmp"
       if (os.path.splitext(self.Fname)[1] != "BMP" and os.path.splitext(self.Fname)[1] != "bmp"):
           newFileName = os.path.splitext(self.Fname)[0] + ".bmp"
           img = Image.open(self.Fname)
           img.save(newFileName)           
   def saveFileasJPG(self):
       "this will save the file as .JPG"
       if (os.path.splitext(self.Fname)[1] != "JPG" and os.path.splitext(self.Fname)[1] != "jpg"):
           newFileName = os.path.splitext(self.Fname)[0] + ".jpg"
           img = Image.open(self.Fname)
           img.save(newFileName)                       
   def thumbNailFile(self):
        "this will resize the file and return the changed file"
        DirName, FileName = os.path.split(os.path.abspath(self.Fname))
        FileName, FileExt = os.path.splitext(FileName)
        FileNameT = FileName + "_thumbnail" + FileExt
        im = Image.open(self.Fname)
        im.thumbnail(self.small_size)
        im.save("C:/output_pictures/"+FileNameT)
       # im.show()                               
   def blurImage(self):
        "this will blur the file and return the changed file"
        DirName, FileName = os.path.split(os.path.abspath(self.Fname))
        FileName, FileExt = os.path.splitext(FileName)
        FileNameT = FileName + "_blurred" + FileExt
        im = Image.open(self.Fname)
        Img_blurred = im.filter(ImageFilter.BLUR)
        Img_blurred.save("C:/output_pictures/"+FileNameT)
       #Img_blurred.show()                                        
   def contourImageSupplied(self):
        "apply contour filter and return the changed file"
        DirName, FileName = os.path.split(os.path.abspath(self.Fname))
        FileName, FileExt = os.path.splitext(FileName)
        FileNameT = FileName + "_Countour" + FileExt
        im = Image.open(self.Fname)
        imgFile = im.filter(ImageFilter.CONTOUR)
        imgFile.save("C:/output_pictures/" + FileNameT )
   def addBorder(self, borderColor):
       "add border to the images"
       DirName, FileName = os.path.split(os.path.abspath(self.Fname))
       FileName, FileExt = os.path.splitext(FileName)
       FileNameT = FileName + "_bordered"+"_"+borderColor + FileExt
       im = Image.open(self.Fname)
       image_bordered = ImageOps.expand(im,border=150,fill=borderColor)
       image_bordered.save("C:/output_pictures/"+FileNameT)
   def addTextToPic(self, TexttoAdd, TextColor, Text_Pos = (10,10), TextFontName = "arial.ttf", TextFontSize = 10):
       "add text to the image"
       TextFont = ImageFont.truetype(TextFontName,TextFontSize)
       DirName, FileName = os.path.split(os.path.abspath(self.Fname))
       FileName, FileExt = os.path.splitext(FileName)
       FileNameT = FileName + "_TextAdded"+"_"+TexttoAdd + FileExt             
       im = Image.open(self.Fname)
       img = im.convert("RGB");
       draw = ImageDraw.Draw(img)
       draw.text(Text_Pos, TexttoAdd, fill=TextColor, font=TextFont)
       img.save("C:/output_pictures/"+FileNameT)
   def blendImage(self):
       "blend same image by rotating"
       DirName, FileName = os.path.split(os.path.abspath(self.Fname))
       FileName, FileExt = os.path.splitext(FileName)
       FileNameT = FileName + "_Blended"+ FileExt             
       im = Image.open(self.Fname)
       img = im.rotate(180)
       img_blend = Image.blend(im, img, 0.5)
       img_blend.save("C:/output_pictures/"+FileNameT)       

       
    
           
       
       
        
        
        
      

    
      
      