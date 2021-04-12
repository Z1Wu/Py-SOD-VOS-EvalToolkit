import cv2
import os
from matplotlib import cm
import numpy as np
import shutil
import matplotlib.pyplot as plt

def var2weight(var_im):
    """
    var_im{np.ndarray}[h, w]: gray scale  
    """    
    weight = np.exp(-20 * (var_im.astype(float) / 255))
    weight = np.round(weight * 255)
    return weight
exp_root = "z_debug_img"

o_im_dir = 'data\DUTS\image'

im_name_list = [
    'ILSVRC2012_test_00043095',
    'n03127747_1382',
    'ILSVRC2014_train_00023498',
    'n04037443_10569',
    'n03445777_8620'
]

res_dir = "fuse_imgs"

# dir_list = [o_im_dir] + [
#     os.path.join(exp_root, e ) for e in [
#         'fda',
#         'pred',
#         'var'
#     ]
# ]

dir_list =[
        # 'fda',
        'fda_pred',
        'flip_pred',
        'rs_pred',
        # 'pred',
        'var'
]


def save_img(im_path, img):
    """
    img[h, w]
    """
    plt.imshow(img / 255.0 , cmap='jet')
    plt.axis('off')
    plt.savefig(im_path, bbox_inches='tight')

if __name__ == "__main__":
    ### all wegiht
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
    for im_name in im_name_list:

        # orginal image
        # sn = os.path.join(o_im_dir, im_name + '.jpg')
        # tn = os.path.join(res_dir, f'{im_name}.jpg')
        # shutil.copyfile(sn, tn)

        for dir_name in dir_list[:-1]:
            sn = os.path.join(exp_root, dir_name, im_name + '.png')
            tn = os.path.join(res_dir, f'{im_name}_{dir_name}.png')
            shutil.copyfile(sn, tn)

        # var_im = cv2.imread(os.path.join(exp_root, dir_list[-1], im_name + '.png'), 0)
        # # plt.imshow(var_im / 255.0, cmap='jet')
        # # plt.show()
        # weight_map = var2weight(var_im).astype(np.uint8)
        # # var_im = var_im # normlize
        # # var_im = cv2.applyColorMap(var_im, cv2.COLORMAP_JET)
        # # weight_map = cv2.applyColorMap(weight_map, cv2.COLORMAP_JET)
        # # cv2.imwrite( os.path.join(res_dir, f'{im_name}_loss_weight.png'),weight_map)
        # # cv2.imwrite( os.path.join(res_dir, f'{im_name}_var.png'),var_im)

        # save_img( os.path.join(res_dir, f'{im_name}_loss_weight.png'),weight_map)
        # save_img( os.path.join(res_dir, f'{im_name}_var.png'),var_im)
