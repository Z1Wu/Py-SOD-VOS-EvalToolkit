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
exp_root = "z_debug_res"

o_im_dir = 'data\DUTS\image'
gt_dir = 'data\DUTS\mask'
summary_dir = 'round_imgs_view'

im_name_list = [
    'ILSVRC2012_test_00002863',
    'ILSVRC2012_test_00005457',
    'ILSVRC2012_test_00008036',
    'ILSVRC2012_test_00009635',
    'ILSVRC2012_test_00063791',
    'ILSVRC2013_test_00005586',
]

res_dir = "per_round_imgs"

# dir_list = [o_im_dir] + [
#     os.path.join(exp_root, e ) for e in [
#         'fda',
#         'pred',
#         'var'
#     ]
# ]

dir_list =[
    'warmup',
    'round_1_checkpoint.pth',
    'round_2_checkpoint.pth',
    'round_3_checkpoint.pth',
    'round_4_checkpoint.pth',
    'round_5_checkpoint.pth',
]

dir2sufflix = {
    'warmup': 0,
    'round_1_checkpoint.pth': 1,
    'round_2_checkpoint.pth': 2,
    'round_3_checkpoint.pth': 3,
    'round_4_checkpoint.pth': 4,
    'round_5_checkpoint.pth': 5,
}

def save_img(im_path, img):
    """
    img[h, w]
    """
    plt.imshow(img / 255.0 , cmap='jet')
    plt.axis('off')
    plt.savefig(im_path, bbox_inches='tight')

# def copy_to(src_dir, im_name, res_dir)

if __name__ == "__main__":
    ### all wegiht
    if not os.path.exists(res_dir):
        os.makedirs(res_dir)
    for im_name in im_name_list:

        # orginal image
        sn = os.path.join(o_im_dir, im_name + '.jpg')
        tn = os.path.join(res_dir, f'{im_name}.jpg')
        shutil.copyfile(sn, tn)

        sn = os.path.join(gt_dir, im_name + '.png')
        tn = os.path.join(res_dir, f'{im_name}_gt.png')
        shutil.copyfile(sn, tn)

        sn = os.path.join(summary_dir, im_name + '.png')
        tn = os.path.join(res_dir, f'{im_name}_a_summary.png')
        shutil.copyfile(sn, tn)

        for dir_name in dir_list:
            sn = os.path.join(exp_root, dir_name,'DUTS',  im_name + '.png')
            tn = os.path.join(res_dir, f'{im_name}==={dir2sufflix[dir_name]}.png')
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
