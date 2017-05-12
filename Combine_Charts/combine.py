import numpy as np
import PIL
from PIL import Image

# load images
list_im = ['example1a.png', 'example2.png', 'example3.png','example4.png', 'example5.png','example6.png']
imgs    = [PIL.Image.open(i) for i in list_im]

# crop images 
n=0
cropped = []
shave = [38,44] # shave amt in pixels [top,bottom]
for i in imgs:
	w, h = i.size
	# box dims from original upper left corner: (dist to left edge, dist to top edge, dist to right edge, dist to bottom edge)
	name = 'tmp/'+list_im[n]
	if n>0:
		i.crop((0, shave[0], w, h-shave[1])).save(name)
	else:
		i.crop((0, 0, w, h-shave[1])).save(name)
	cropped.append(name)
	n+=1

list_im = cropped
name = list_im[0].strip('.png').strip('/tmp')+' through '+list_im[-1].strip('.png').strip('/tmp')+'.png'
imgs    = [PIL.Image.open(i) for i in list_im]

# resize to smallest image 
min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

# combine images vertially 
imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
imgs_comb = PIL.Image.fromarray(imgs_comb)
imgs_comb.save(name)