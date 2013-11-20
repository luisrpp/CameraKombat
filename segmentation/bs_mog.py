#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


import cv2
import numpy as np


class BackgroundSubtractorMOG(object):
    def __init__(self):
        self.compute_done = True
        self.fgbg = cv2.BackgroundSubtractorMOG(3, 4, 0.8)

    def reset(self):
        self.fgbg = cv2.BackgroundSubtractorMOG(3, 4, 0.8)

    def set_num_frames(self, num_frames):
        pass

    def is_compute_done(self):
        return self.compute_done

    def compute(self, image):
        pass

    def process(self, image):
        return self.fgbg.apply(image)