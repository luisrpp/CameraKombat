#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


## Display configuration ##
SCREEN_SIZE = 1024, 640
BACKGROUND_COLOR = 0, 0, 0

## Segmentation configuration ##

# Segmentation strategy options: SIMPLE_SUBTRACTION_METHOD, BACKGROUND_SUBTRACTOR_MOG, BACKGROUND_SUBTRACTOR_MOG2
SEGMENTATION_STRATEGY = "BACKGROUND_SUBTRACTOR_MOG2"
NUM_COMPUTE_FRAMES = 60

# ctypes libs path
CTYPES_LIB_PATH = "/Users/luisrpp/Development/python/CameraKombat/lib/"
