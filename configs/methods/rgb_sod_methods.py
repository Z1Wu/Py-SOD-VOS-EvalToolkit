# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.misc import curve_info_generator, simple_info_generator

# _RGBSOD_METHODS_ROOT = "/home/lart/Datasets/Saliency/PaperResults/RGBSOD" # TODO: change
_RGBSOD_METHODS_ROOT = "data"
# _RGBSOD_DATASET_NAMES = ["PASCAL-S", "ECSSD", "HKU-IS", "DUT-OMRON", "DUTS"]
_RGBSOD_DATASET_NAMES = ["PASCAL-S", "ECSSD", "HKU-IS", "DUT-OMRON", "DUTS", "SOD"]


_METHODS_DIR_NAMES = {
    # "DGRL_2018": "DGRL",
    # "PAGRN_2018": "PAGRN18",
    # "PiCANet_R_2018": "PiCANet-R",
    # "RAS_2018": "RAS",
    # "AFNet_2019": "AFNet",
    # "BASNet_2019": "BASNet",
    # "CPD_R_2019": "CPD-R",
    # "PoolNet_R_2019": "PoolNet",
    # "EGNet_R_2019": "EGNet-R",
    # "HRS_D_2019": "HRS-D",
    # "ICNet_2019": "ICNet",
    # "MLMSNet_2019": "MLMSNet",
    # "PAGENet_2019": "PAGE-Net",
    # "SCRN_R_2019": "SCRN",
    # "F3Net_R_2020": "F3",
    # "R3Net_R_2020": "R3Net",
    # "GCPANet_2020": "GCPANet_AAAI20",
    # "DFI_2020": "DFI_TIP2020",
    # "ITSD_2020": "ITSD20",

    "MBD": "mbd",
    "RBD": "rbd",

    "EDNL_2020": "EDNL", 
    "MWS_2019": "MWS",      
    "C2S_2018": "c2s_10k",
    "SCRIB_2020": "SCRIB",
    "USPS_2019": "USPS", 
    "SCWS_2021": "SCWS",
    "ASMO_2018": "ASMO",
    "MNL_2018": "MNL",

    "MINet_R_2020": "MI",
    "GateNet_2020": "GateNet_res50",
    "LDF_2020": "LDF",
    "AF_NET_2019": "AF_NET",
    "SCRN_2019": "SCRN",
    "TSPOA_2019": "TSPOANet",
    "BAS_2019": "BASNet",
    "CAPSAL_2019": "CAPSAL",
    "R3_2018": "R3Net",
    "DGRL_2018": "DGRL",
    "OURS": "OURS"
}

MINet_R_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet_R_2020"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["MINet_R_2020"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet_R_2020"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet_R_2020"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet_R_2020"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet_R_2020"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

GateNet_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet_2020"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["GateNet_2020"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet_2020"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet_2020"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet_2020"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet_2020"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

LDF_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDF_2020"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["LDF_2020"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDF_2020"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDF_2020"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDF_2020"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDF_2020"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

EDNL_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EDNL_2020"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["EDNL_2020"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EDNL_2020"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EDNL_2020"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EDNL_2020"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EDNL_2020"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

USPS_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["USPS_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["USPS_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["USPS_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["USPS_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["USPS_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["USPS_2019"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

MNL_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MNL_2018"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["MNL_2018"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MNL_2018"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MNL_2018"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    # "DUTS": dict(
    #     path=os.path.join(
    #         _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MNL_2018"], _RGBSOD_DATASET_NAMES[4],
    #     ),
    #     suffix=".png",
    # ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MNL_2018"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

MWS_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MWS_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["MWS_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MWS_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MWS_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MWS_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MWS_2019"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

C2S_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["C2S_2018"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["C2S_2018"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["C2S_2018"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["C2S_2018"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["C2S_2018"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

SCRIB_2020 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRIB_2020"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["SCRIB_2020"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRIB_2020"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRIB_2020"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRIB_2020"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRIB_2020"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}


SCWS_2021 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCWS_2021"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["SCWS_2021"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCWS_2021"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCWS_2021"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCWS_2021"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

AF_NET_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AF_NET_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["AF_NET_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AF_NET_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AF_NET_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AF_NET_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

ASMO_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["ASMO_2018"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["ASMO_2018"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["ASMO_2018"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["ASMO_2018"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["ASMO_2018"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["ASMO_2018"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}


SCRN_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRN_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["SCRN_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRN_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRN_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRN_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SCRN_2019"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

BAS_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BAS_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["BAS_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BAS_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BAS_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BAS_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BAS_2019"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}


OURS = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["OURS"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["OURS"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["OURS"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["OURS"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["OURS"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["OURS"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

CAPSAL_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAPSAL_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["CAPSAL_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAPSAL_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAPSAL_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAPSAL_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAPSAL_2019"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

TSPOA_2019 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["TSPOA_2019"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["TSPOA_2019"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["TSPOA_2019"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["TSPOA_2019"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["TSPOA_2019"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["TSPOA_2019"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

R3_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["R3_2018"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["R3_2018"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["R3_2018"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["R3_2018"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["R3_2018"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["R3_2018"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

DGRL_2018 = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DGRL_2018"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["DGRL_2018"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DGRL_2018"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DGRL_2018"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DGRL_2018"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DGRL_2018"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}


MBD = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MBD"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["MBD"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MBD"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MBD"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MBD"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MBD"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}

RBD = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["RBD"], _RGBSOD_DATASET_NAMES[0],
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT,_METHODS_DIR_NAMES["RBD"], _RGBSOD_DATASET_NAMES[1],
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["RBD"], _RGBSOD_DATASET_NAMES[2],
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["RBD"], _RGBSOD_DATASET_NAMES[3],
        ),
        suffix=".png",
    ),
    "DUTS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["RBD"], _RGBSOD_DATASET_NAMES[4],
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["RBD"], _RGBSOD_DATASET_NAMES[5],
        ),
        suffix=".png",
    ),
    # "SOC": None,
}




curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {

        "EDNL_2020": curve_info(EDNL_2020, "EDNL_2020", line_label='EDNL', line_style=':', line_color='darkorange'),
        "SCRIB_2020": curve_info(SCRIB_2020, "SCRIB_2020", line_label='SCRIB', line_style=':', line_color='lime'),
        "USPS_2019": curve_info(USPS_2019, "USPS_2019",  line_label='USPS', line_style=':', line_color='peru'),
        "MWS_2019": curve_info(MWS_2019, "MWS_2019", line_label="MWS", line_style=':', line_color='navy'),
        "ASMO_2018": curve_info(ASMO_2018, "ASMO_2018",line_label="ASMO", line_style=':', line_color='deeppink'),

        "MINet_R_2020": curve_info(MINet_R_2020, "MINet_R_2020",line_label="MINet", line_style='-', line_color='brown'),
        "LDF_2020": curve_info(LDF_2020, "LDF_2020",line_label="LDF", line_style='-', line_color='gold'),
        "BAS_2019": curve_info(BAS_2019, "BAS_2019",line_label="BAS", line_style='-', line_color='green'),
        "DGRL_2018": curve_info(DGRL_2018, "DGRL_2018",line_label="DGRL", line_color='purple', line_style='-'),
        "OURS": curve_info(OURS, "OURS", line_color='red', line_style='--'),

        # "MBD": curve_info(MBD, "MBD"),
        # "RBD": curve_info(RBD, "RBD"),
        # "GateNet_2020": curve_info(GateNet_2020, "GateNet_2020",line_label="GateNet"),
        # "R3_2018": curve_info(R3_2018, "R3_2018",line_label="R3"),
        # "TSPOA_2019": curve_info(TSPOA_2019, "TSPOA_2019",line_label="TSPOA"),
        # "CAPSAL_2019": curve_info(CAPSAL_2019, "CAPSAL_2019",line_label="CAPSAL"),
        # "AF_NET_2019": curve_info(AF_NET_2019, "AF_NET_2019"),
        # "SCRN_2019": curve_info(SCRN_2019, "SCRN_2019"),
        # "MNL_2018": curve_info(MNL_2018, "MNL_2018",line_label="MNL", line_style=':', line_color='skyblue'),
        # "C2S_2018": curve_info(C2S_2018, "C2S_2018"),
        # "SCWS_2021": curve_info(SCWS_2021, "SCWS_2021"),

    }
)
simple_info = simple_info_generator()
methods_info_for_selecting = OrderedDict(
    {
        "OURS": simple_info(OURS, "OURS"),
        "EDNL_2020": simple_info(EDNL_2020, "EDNL_2020"),
        "MWS_2019": simple_info(MWS_2019, "MWS_2019"),
        "C2S_2018": simple_info(C2S_2018, "C2S_2018"),
        "SCRIB_2020": simple_info(SCRIB_2020, "SCRIB_2020"),
        "ASMO_2018": simple_info(ASMO_2018, "ASMO_2018"),
        # "SCWS_2021": simple_info(SCWS_2021, "SCWS_2021"),
        "MNL_2018": simple_info(MNL_2018, "MNL_2018"),
        "USPS_2019": simple_info(USPS_2019, "USPS_2019"),


        "MINet_R_2020": simple_info(MINet_R_2020, "MINet_R_2020"),
        "GateNet_2020": simple_info(GateNet_2020, "GateNet_2020"),
        "LDF_2020": simple_info(LDF_2020, "LDF_2020"),
        # "AF_NET_2019": simple_info(AF_NET_2019, "AF_NET_2019"),
        # "SCRN_2019": simple_info(SCRN_2019, "SCRN_2019"),
        "BAS_2019": simple_info(BAS_2019, "BAS_2019"),
        "TSPOA_2019": simple_info(TSPOA_2019, "TSPOA_2019"),
        "CAPSAL_2019": simple_info(CAPSAL_2019, "CAPSAL_2019"),        
        "DGRL_2018": simple_info(DGRL_2018, "DGRL_2018"),
        "R3_2018": simple_info(R3_2018, "R3_2018"),
        "MBD": simple_info(MBD, "MBD"),
        "RBD": simple_info(RBD, "RBD"),
    }
)
