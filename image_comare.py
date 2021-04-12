from genericpath import exists
import matplotlib.pyplot as plt
from numpy.lib.npyio import save
plt.switch_backend('agg')
import numpy as np
import cv2
import os
import json

## 6324 之后的是没选入伪标签的。

data_root = ''
im_name_list_path = 'z_debug_img/whole.txt'

name2var_path = "z_debug_img/name2var.json"

im_dir_list = [
    ('data/DUTS/image', '.jpg'),
    ('z_debug_img/fda', '.png'),
    ('data/DUTS/mask', '.png'),
    ('z_debug_img/pred', '.png'),
    ('z_debug_img/flip_pred', '.png'),
    ('z_debug_img/fda_pred', '.png'),
    ('z_debug_img/rs_pred', '.png'),
    ('z_debug_img/var', '.png'),
    # (dir, ext), 
]

res_dir = 'fuse_compare'
# if os.path.exists(res_dir)
os.makedirs(res_dir,exist_ok=True)

def show_in_cv2(im_name_list, fig, axes):
    c = 0
    while(1):
        im_name = im_name_list[c]
        print(im_name)
        for ax_i, tup in enumerate(im_dir_list):
            im_dir, ext = tup
            im = read_img(os.path.join(im_dir, im_name + ext))
            axes[ax_i].imshow(im)
            axes[ax_i].set_title(im_dir.split('/')[1])
        plt.tight_layout()
        fig.canvas.draw()
        # convert canvas to image
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8,
                sep='')
        img  = img.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        c += 1
        cv2.imshow('frame',img)
        cv2.waitKey(3) # 等待图片转化，如果使用 0 的话，需要 focus 在 窗口出按键
        print("cmd:")
        next = input()
        print(next)

def save_imgs(im_name_list, fig, axes):
    c = 0
    while(1):
        im_name = im_name_list[c]
        print(im_name)
        for ax_i, tup in enumerate(im_dir_list):
            im_dir, ext = tup
            im = read_img(os.path.join(im_dir, im_name + ext))
            axes[ax_i].imshow(im)
            axes[ax_i].set_title(im_dir.split('/')[1])
        plt.tight_layout()
        fig.savefig(os.path.join(res_dir, im_name + '.png'))
        c += 1

def save_imgs_var(im_name_list, fig, axes, name2var):
    c = 0
    prefix = ''
    while(1):
        im_name = im_name_list[c]
        print(im_name)
        # if c >= 6324:
        #     prefix = 'zw_'
        for ax_i, tup in enumerate(im_dir_list):
            im_dir, ext = tup
            if ax_i == (len(im_dir_list) - 1):
                im = read_img(os.path.join(im_dir, im_name + ext), mode = 0)
                axes[ax_i].imshow(im, cmap='jet')
            else:
                im = read_img(os.path.join(im_dir, im_name + ext))
                axes[ax_i].imshow(im)
            axes[ax_i].set_title(im_dir.split('/')[1])
        plt.tight_layout()
        fig.savefig(os.path.join(res_dir, f'{c}_{im_name}_{name2var[im_name]}.png'))
        c += 1

def read_img(img_path, dsize = None, mode = 1):
    """
    dsize(w, h)
    """
    im = cv2.imread(img_path, mode)
    if mode == 1:
        return im[:, :, ::-1]
    else:
        return im

if __name__ == '__main__':
    col_num = 3
    tot_num = len(im_dir_list)
    row_num = int(tot_num // col_num)
    if tot_num % col_num !=0 and tot_num > col_num:
        row_num += 1
    fig, axes = plt.subplots(row_num, col_num, figsize=(col_num * 4, row_num * 3))
    axes = axes.flatten()
    for ax in axes:
        ax.set_axis_off()

    im_name_list = [l.strip() for l in open(im_name_list_path, 'r')]
    name2var = json.load(open(name2var_path, 'r'))
    # show_in_cv2(im_name_list, fig, axes)

    save_imgs_var(im_name_list, fig ,axes, name2var)