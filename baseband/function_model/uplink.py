#! $PATH/python
# -*- coding: utf-8 -*-

# file name: uplink.py
# author: lianghy
# time: 11/30/2020 3:41:27 PM

"""This is an uplink data channel sample.
The configuration of the channel is:

    * 
"""

import logging

import sys
sys.path.append("E:\\work\\public_tools\\nuanfeng\\project_nf\\")
from nuanfeng.func_model import *
from . import bb as bf

class PUSCH(Module):
    """sample for PUSCH"""
    def __init__(self):
        super(PUSCH, self).__init__()
        self.b__q = Input()
        self.channel_para = {
                "q":    0,  #codeword length, [0,1]
                "n_FNTI": 1, #
                "N_ID_cell": 1, #
                "n_s": 0, #
                "x": 1, #
                "y": 0, #
                #"": , #
                }
        self.mode(self.body, 0)
        self.mode(self.config_channel, 1)

    def body(self):
        for d in self.b__q:
            b__qw = bf.scrambing(d,
                    q = self.channel_para["q"],
                    n_RNTI = self.channel_para["n_RNTI"],
                    N_ID_cell = self.channel_para["N_ID_cell"],
                    n_s = self.channel_para["n_s"],
                    x = self.channel_para["x"],
                    y = self.channel_para["y"],
                    )
    def config_channel(self, **argv):
        """config channel parameters."""
        for para, value in argv:
            self.channel_para[para] = value

if __name__ == "__main__":
    print("uplink.py")
