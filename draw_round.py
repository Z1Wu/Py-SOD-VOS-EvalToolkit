import os
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.utils import who

## read image from multi

exp_root = 'z_debug_res'

methods = [
    'warmup',
    'round_1_checkpoint.pth',
    'round_2_checkpoint.pth',
    'round_3_checkpoint.pth',
    'round_4_checkpoint.pth',
    'round_5_checkpoint.pth',
]

met2name = {
    "GateNet_res50": "GateNet",
    "mbd": "MBD",
    "rbd": "RBD",
}

ambiguous_ids = [
    423,
    51,
]

im_w, im_h = 160, 120

def list_join(other_list, sep):
    ret = []
    for e in other_list[:-1]:
        ret.append(e)
        ret.append(sep)
    ret.append(other_list[-1])
    return ret

def read_img(dirc, name):
    im = cv2.imread(os.path.join(dirc, name), 1)
    im = cv2.resize(im, dsize=(im_w, im_h))
    return im


def func(ds_name):
    row_per_img = 64
    c = 0
    fig,  axes = plt.subplots(row_per_img, 1, figsize=((len(methods) + 2) * 4,row_per_img * 3))
    axes = axes.flatten()
    out_dir = 'debug'
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    v_bar = np.ones((im_h, 5, 3)) * 255

    im_dir = f'data/{ds_name}/image/'
    gt_dir = f'data/{ds_name}/mask/'
    file_list_path = f'data/{ds_name}/test.txt'
    file_name_list = []
    with open(file_list_path, 'r') as f:
        while 1:
            name = f.readline().strip()
            if name == '':
                break
            file_name_list.append(name)

    done = False
    while not done:
        for r in range(row_per_img):
            file_name = file_name_list[c]
            c += 1
            if c == len(file_name_list):
                done = True
                break
            im = read_img(im_dir, file_name + '.jpg')
            gt = read_img(gt_dir, file_name + '.png')

            others = []
            for met in methods:
                met_dir = os.path.join(exp_root, met, ds_name)
                others.append(read_img(met_dir, file_name + '.png'))
            
            row = list_join([im, gt] + others, v_bar)
            row_img = np.concatenate(row, 1)[:, :, ::-1] / 255
            axes[r].imshow(row_img)
            axes[r].set_title(f'{c}====={file_name}')
            axes[r].set_axis_off()
        print(f'save file test_{c}')
        plt.tight_layout()
        fig.savefig(os.path.join(out_dir, f'test_{c}.png'))
    

def generate_cv2_file():
    rows = []
    v_bar = np.ones((im_h, 10, 3)) * 255
    
    ds_name = 'DUTS'
    file_name_list = [
        'sun_axftbpasnkrpiacj', 
        'sun_bepsjlnfypehmpgt', 
        'sun_aabitsznxycbxvgm', ## 
        'ILSVRC2012_test_00048578',
        'ILSVRC2012_test_00005780', 
        'ILSVRC2012_test_00036696', 
        'ILSVRC2012_test_00095958', 
        'sun_bffqmlxnqvqwhsek', 
        'ILSVRC2012_test_00011906', 
        'ILSVRC2012_test_00032180', 
        'ILSVRC2012_test_00032520', 
        'ILSVRC2012_test_00033238', 
        'ILSVRC2012_test_00048578', 'sun_alcpbxhmsofmrdfl', 'ILSVRC2012_test_00036627', 'ILSVRC2012_test_00033238', 'ILSVRC2012_test_00032520', 'ILSVRC2012_test_00048578', 'sun_alcpbxhmsofmrdfl', 'ILSVRC2012_test_00006721', 'ILSVRC2012_test_00032110', 'ILSVRC2012_test_00001302', 'ILSVRC2012_test_00032529']
    im_dir = f'data/{ds_name}/image/'
    gt_dir = f'data/{ds_name}/mask/'
    im_num = 6
    for idx, file_name in enumerate(file_name_list[:6]):
        im = read_img(im_dir, file_name + '.jpg')
        gt = read_img(gt_dir, file_name + '.png')

        others = []
        for met in methods:
            met_dir = os.path.join(exp_root, met, ds_name)
            others.append(read_img(met_dir, file_name + '.png'))
        
        row = list_join([im, gt] + others, v_bar)
        row_img = np.concatenate(row, 1)

        rows.append(row_img)

    texts = []
    for met in ['Image', 'GT'] + methods:
        met_text = met if met not in met2name else met2name[met]
        font                   = cv2.FONT_HERSHEY_SIMPLEX
        # bottomLeftCornerOfText = (int(im_h / 10.0 / 10.0), int(im_w / 10.0 * 9))
        bottomLeftCornerOfText = (10, 10)
        fontScale              = 0.8
        fontColor              = (0,0,0)
        lineType               = 2
        text_size = cv2.getTextSize(
            met_text, 
            font,
            fontScale,
            lineType,
        )[0]
        text_im_h = text_size[1] + 10
        text_im_w = im_w
        img = np.ones((text_im_h, text_im_w, 3)) * 255
        # center_text = tuple([int((box_center[i] / 2) - (text_size[i] / 2)) for i in range(2)])
        textX = int((text_im_w / 2) - (text_size[0] / 2))
        # textY = int((box_center[0] / 2) + (text_size[1] / 2))
        textY = text_im_h - 10
        cv2.putText(
            img, 
            met_text, 
            # bottomLeftCornerOfText, 
            (textX, textY),
            font, 
            fontScale,
            fontColor,
            lineType
        )
        texts.append(img)
    text_v_bar = np.ones((texts[0].shape[0], 10, 3)) * 255
    text_row =list_join(texts, text_v_bar)
    rows.append(np.concatenate(text_row, 1))
    h_bar = np.ones((10, rows[0].shape[1], 3)) * 255
    whole = list_join(rows, h_bar)
    fin_im = np.concatenate(whole, 0)
    

    cv2.imwrite('test1.png', fin_im)


if __name__ == '__main__':
    # func('DUTS')
    generate_cv2_file()
    

