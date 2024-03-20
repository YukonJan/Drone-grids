This repo contains the ipython notebooks used to create the combined drone grid images. 

The functions_only code is a cleaned up version with only the functions used to make the drone grids and contour the rhodamine dye. 
Calling the ```mapper``` function on a folder of drone images will combine them and return Image object, which can be shown with ```display(Image)``` and saved with ```Image.save('name.jpg')```.
It will also return some important location information about the image, such as the scale.

Image_stitch_5 is the current working document for making grids, might have random extra cells on top of the functions.
