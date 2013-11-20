#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


import cv2
import numpy as np


class SimpleSubtractionMethod(object):
    def __init__(self):
        self.num_frames = 30
        self.computed_frames = 0
        self.compute_done = False
        self.background = None

    def reset(self):
        self.computed_frames = 0
        self.compute_done = False
        self.background = None

    def set_num_frames(self, num_frames):
        self.num_frames = num_frames

    def is_compute_done(self):
        return self.compute_done

    def compute(self, image):
        if self.computed_frames == self.num_frames:
            divide = np.zeros(self.background.shape, np.uint8)
            divide[:, :] = self.num_frames
            self.background = cv2.divide(self.background, divide, dtype=cv2.CV_8U)
            self.compute_done = True
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            if self.background is None:
                self.background = gray
            else:
                self.background = cv2.add(self.background, gray, dtype=cv2.CV_32S)
            self.computed_frames += 1

    def process(self, image):
        if self.compute_done:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            diff_image = np.zeros(gray_image.shape, np.uint8)

            cv2.absdiff(gray_image, self.background, diff_image)
            cv2.threshold(diff_image, 40, 255, cv2.THRESH_BINARY, diff_image)

            element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
            cv2.erode(diff_image, element, diff_image, iterations=1)
            cv2.dilate(diff_image, element, diff_image, iterations=2)

            return diff_image
        else:
            return image
