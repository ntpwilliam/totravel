#!/user/bin/python
# -*- coding: UTF-8 -*--

from PIL import Image
im = Image.open("desk2.png")
im2 = im.convert('L')
im2.save( "desk_gray.jpg", "JPEG" )
