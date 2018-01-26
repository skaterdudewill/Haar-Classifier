import PIL
import glob
from PIL import Image
number = 0
image_list = []
for File in glob.glob('positive_images/*.pgm'):
	im = Image.open(File)
	rgb_im = im.convert('RGB')
	rgb_im.save('newImages/pos-' + str(number)+'.jpg')
	number = number + 1
