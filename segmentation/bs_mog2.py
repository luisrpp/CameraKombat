#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


import ctypes as C

import cv2
import numpy as np

import settings


class BackgroundSubtractorMOG2(object):
    def __init__(self):
        self.compute_done = True

    def reset(self):
        pass

    def set_num_frames(self, num_frames):
        pass

    def is_compute_done(self):
        return self.compute_done

    def compute(self, image):
        pass

    def process(self, image):
        foreground = getfg(image)
        element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        cv2.erode(foreground, element, foreground, iterations=1)
        cv2.dilate(foreground, element, foreground, iterations=1)

        return foreground


libmog2 = C.cdll.LoadLibrary(settings.CTYPES_LIB_PATH + "libmog2.so")


def getfg(img):
    (rows, cols) = (img.shape[0], img.shape[1])
    res = np.zeros(dtype=np.uint8, shape=(rows, cols))
    libmog2.getfg(img.shape[0], img.shape[1],
                  img.ctypes.data_as(C.POINTER(C.c_ubyte)),
                  res.ctypes.data_as(C.POINTER(C.c_ubyte)))
    return res

