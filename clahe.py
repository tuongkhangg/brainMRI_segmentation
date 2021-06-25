import cv2
import numpy as np


def contrast_enhancement(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2LUV)
    img[:,:,0] = clahe.apply(img[:,:,0])
    img = cv2.cvtColor(img, cv2.COLOR_LUV2RGB)
    return img

def center_crop(img, dim):
	"""Returns center cropped image
	Args:
	img: image to be center cropped
	dim: dimensions (width, height) to be cropped
	"""
	width, height = img.shape[1], img.shape[0]

	# process crop width and height for max available dimension
	crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
	crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
	mid_x, mid_y = int(width/2), int(height/2)
	cw2, ch2 = int(crop_width/2), int(crop_height/2) 
	crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
	return crop_img


gamma = 1.5
inverse_gamma = 1.0 / gamma
look_up_table = np.array([((i/255.0) ** inverse_gamma) * 255.0 for i in np.arange(0,256,1)]).astype("uint8")
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))




cv2.waitKey(0)
