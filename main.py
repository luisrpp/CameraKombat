#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


import sys

import cv2
import pygame

import settings
from helpers import video, convert
from segmentation import SegmentationFactory


class CameraKombat(object):
    def __init__(self, video_src):
        self.cam = video.create_capture(video_src)
        pygame.init()
        pygame.display.set_caption('Camera Kombat')
        self.size = settings.SCREEN_SIZE
        self.background_color = settings.BACKGROUND_COLOR
        self.screen = pygame.display.set_mode(self.size)

    def run(self):
        segmentation = SegmentationFactory.get_instance(settings.SEGMENTATION_STRATEGY)
        segmentation.set_num_frames(settings.NUM_COMPUTE_FRAMES)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            ret, self.frame = self.cam.read()  # Current frame from Webcam or video file

            if ret:
                # Resize image to fit display size
                frame = cv2.resize(self.frame, self.size, fx=0.5, fy=0.5)

                # Segmentation part
                if not segmentation.is_compute_done():
                    segmentation.compute(frame)  # Background processing
                else:
                    frame = segmentation.process(frame)  # Segmented image

                # Display part
                self.screen.fill(self.background_color)
                if len(frame.shape) == 3:
                    self.screen.blit(convert.cvimage_to_pygame(frame), (0, 0))
                else:
                    self.screen.blit(convert.cvgrayimage_to_pygame(frame), (0, 0))
                pygame.display.flip()
            else:
                sys.exit()


if __name__ == '__main__':
    try:
        video_src = sys.argv[1]
    except:
        video_src = 0

    CameraKombat(video_src).run()
