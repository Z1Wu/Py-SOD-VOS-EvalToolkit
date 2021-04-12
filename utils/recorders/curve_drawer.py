# -*- coding: utf-8 -*-
# @Time    : 2021/1/4
# @Author  : Lart Pang
# @GitHub  : https://github.com/lartpang

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
# plt.switch_backend('agg')
import numpy as np


class CurveDrawer(object):
    def __init__(self, row_num, col_num, ax_w = 4, ax_h = 3):
        fig, axes = plt.subplots(nrows=row_num, ncols=col_num, figsize=( ax_w * col_num, ax_h * row_num))
        self.fig = fig
        try:
            self.axes = axes.flatten()
        except:
            print("only one axes")
            self.axes = [axes]

        self.num_subplots = row_num * col_num
        self.font_cfg = {
            "title": {
                "fontsize": 13,
                "fontweight": "bold",
                "fontname": "Liberation Sans",
            },
            "label": {
                "fontsize": 12,
                "fontweight": "normal",
                "fontname": "Liberation Sans",
            },
            "ticks": {
                "fontsize": 10,
                "fontweight": "normal",
                "fontname": "Liberation Sans",
            },
            "legend": {
                "size": 10,
                "weight": "normal",
                "family": "Liberation Sans",
            },
        }

        self.init_subplots()

    def init_subplots(self):
        plt.style.use("default")
        for ax in self.axes:
            ax.grid(False)
            ax.set_axis_off()

    def draw_method_curve(
        self,
        curr_idx,
        dataset_name,
        method_curve_setting,
        x_label,
        y_label,
        x_data,
        y_data,
        x_lim: tuple = (0, 1),
        y_lim: tuple = (0, 1),
        mode = None,
    ):
        """
        :param method_curve_setting:  {
                "line_color": "color"(str),
                "line_style": "style"(str),
                "line_label": "label"(str),
                "line_width": width(int),
            }
        """
        assert isinstance(curr_idx, int) and 0 <= curr_idx < self.num_subplots
        ax = self.axes[curr_idx]
        ax.grid(True)
        ax.set_axis_on()

        # give plot a title
        ax.set_title(dataset_name, fontdict=self.font_cfg["title"])

        # make axis labels
        ax.set_xlabel(x_label, fontdict=self.font_cfg["label"])
        ax.set_ylabel(y_label, fontdict=self.font_cfg["label"])

        # 对坐标刻度的设置
        
        label = [f"{x:.1f}" for x in np.linspace(0, 1, 6)]
        if mode == "pr":
            x_ticks = np.linspace(0, 1, 6)
            x_ticks_label = label
        elif mode == "fm":
            step_size = 100
            ticks = np.arange(0, 255, step_size)
            x_ticks = ticks
            x_ticks_label =  [f"{x}" for x in x_ticks]
            x_lim = (0, 255)
        ax.set_xticks(x_ticks)
        ax.set_xticklabels(labels=x_ticks_label, fontdict=self.font_cfg["ticks"])

        ax.set_yticks(np.linspace(0, 1, 6))
        ax.set_yticklabels(labels=label, fontdict=self.font_cfg["ticks"])

        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)

        # [CPFP, "red", "-", "OURS", 3],
        ax.plot(
            x_data,
            y_data,
            linewidth=method_curve_setting["line_width"],
            label=method_curve_setting["line_label"],
            color=method_curve_setting["line_color"],
            linestyle=method_curve_setting["line_style"],
        )

        # loc=0，自动将位置放在最合适的
        ax.legend(loc=3, ncol = 2, prop=self.font_cfg["legend"], frameon=False)

        # 对坐标轴的框线进行设置, 设置轴
        ax.spines["top"].set_linewidth(1)
        ax.spines["bottom"].set_linewidth(1)
        ax.spines["left"].set_linewidth(1)
        ax.spines["right"].set_linewidth(1)

    def show(self):
        # plt.tight_layout(
        #     # w_pad=0.26, 
        # )
        plt.subplots_adjust(
            top=0.886,
            bottom=0.173,
            left=0.03,
            right=0.99,
            hspace=0.2,
            wspace=0.215
        )
        plt.show()
    
    def save_fig(self, file_name):
        plt.tight_layout()
        self.fig.savefig(file_name)


if __name__ == "__main__":
    drawer = OldCurveDrawer(4, 4)
