#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


import cv2
import pygame


def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "RGB")


def cvgrayimage_to_pygame(image):
    """Convert cvimage (gray) into a pygame image"""
    frame = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return pygame.image.frombuffer(frame.tostring(), frame.shape[1::-1], "RGB")