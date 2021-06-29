import cv2
import numpy as np
import os

def cut_out(image, mask):
    if type(image) != np.ndarray:
        raise TypeError("image must be a Numpy array")
    elif type(mask) != np.ndarray:
        raise TypeError("mask must be a Numpy array")
    elif image.shape != mask.shape:
        raise ValueError("image and mask must have the same shape")

    return np.where(mask==0, 0, image)

for fol, subs, files in os.walk('./new_data/predictions_skull'):
    for file in files:
        if file[len(file)-8:-4] == 'mask':
            dir = './new_data/predictions_skull/' + file
            img_fol = file[:21]

            mask  = cv2.imread(dir)

            subfol = './dataset/kaggle_3m/' + img_fol + '/'
            basename = subfol + file[:-9] + '.tif'
            
            img = cv2.imread(basename)

            res = cut_out(img, mask)
            
            save_dir = './dset_remove/' + file[:-9] + '_remove.png'

            cv2.imwrite(save_dir, res)
            #cv2.imshow("result", res)
            cv2.waitKey(0)
