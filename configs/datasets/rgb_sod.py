# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

# _RGB_SOD_ROOT = "/home/lart/Datasets/Saliency/RGBSOD"
# _RGB_SOD_ROOT = "/home/lart/Datasets/Saliency/RGBSOD" # TODO 
_RGB_SOD_ROOT = "data" # TODO 


# default drawing info


ECSSD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "ECSSD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "mask"), suffix=".png"),
)
DUTOMRON = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "mask"), suffix=".png"),
)
HKUIS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "HKU-IS"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "image"), suffix=".png"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "mask"), suffix=".png"),
)
PASCALS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "PASCAL-S"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "mask"), suffix=".png"),
)
SOC_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "SOC/Test"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "SOC/Test", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "SOC/Test", "mask"), suffix=".png"),
)
DUTS_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/Test"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Test", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Test", "mask"), suffix=".png"),
)

DUTS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS", "mask"), suffix=".png"),
)

SOD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "SOD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "SOD", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "SOD", "mask"), suffix=".png"),
)

DUTS_TR = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/Train"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Train", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/Train", "mask"), suffix=".png"),
)

rgb_sod_data = OrderedDict(
    {
        # "DUTS-TR": DUTS_TR,
        # "DUTS": DUTS,
        # "ECSSD": ECSSD,
        # "DUT-OMRON": DUTOMRON,
        # "HKU-IS": HKUIS,
        # "PASCAL-S": PASCALS,
        "SOD": SOD,
    }
)


def make_ax_info(pr_x_lim = None, pr_y_lim = None, fm_x_lim = None, fm_y_lim = None):
    default_info = {
        "pr": {  # pr曲线的配置
            "x_label": "Recall",  # 横坐标标签
            "y_label": "Precision",  # 纵坐标标签
            "x_lim": pr_x_lim or (0.1, 1),  # 横坐标显示范围
            "y_lim": pr_y_lim or (0.1, 1),  # 纵坐标显示范围
            },
        "fm": {  # fm曲线的配置
            "x_label": "Threshold",  # 横坐标标签
            # "y_label": r"F$_{\beta}$",  # 纵坐标标签
            "y_label": r"F-measure",  # 纵坐标标签
            "x_lim": fm_x_lim or (0, 1),  # 横坐标显示范围
            "y_lim": fm_y_lim or (0, 1),  # 纵坐标显示范围
        },
    }
    return default_info
    

rgb_sod_info_for_drawing = OrderedDict(
    {
        # "DUTS-TR": DUTS_TR,
        "DUTS": make_ax_info(fm_y_lim=(0.3, 0.9), pr_y_lim=(0.4, 1)),
        "PASCAL-S": make_ax_info(fm_y_lim=(0.3, 0.9), pr_y_lim=(0.4, 1)),
        "ECSSD": make_ax_info(fm_y_lim=(0.3, 1), pr_y_lim=(0.4, 1)),
        "HKU-IS": make_ax_info(fm_y_lim=(0.3, 1), pr_y_lim=(0.4, 1)),
        "DUT-OMRON": make_ax_info(fm_y_lim=(0.3, 0.8), pr_y_lim=(0.4, 0.9)),
        # "DUTS-TE": DUTS_TE,
        "SOD": make_ax_info(fm_y_lim=(0.3, 0.9), pr_y_lim=(0.4, 1)),
    }
)

