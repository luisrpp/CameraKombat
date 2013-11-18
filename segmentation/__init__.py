#!/usr/bin/env python

###############################################################################
# Camera Kombat
# Copyright (C) 2013 Luis Roberto Pereira de Paula <luisrpp@gmail.com>

# License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)
###############################################################################


class Segmentation(object):
    def __init__(self, strategy=None):
        self.action = None
        if strategy:
            self.action = strategy()

    def reset(self):
        if self.action:
            self.action.reset()
        else:
            raise UnboundLocalError('Exception raised, no strategyClass supplied to Segmentation')

    def set_num_frames(self, num_frames):
        if self.action:
            self.action.set_num_frames(num_frames)
        else:
            raise UnboundLocalError('Exception raised, no strategyClass supplied to Segmentation')

    def is_compute_done(self):
        if self.action:
            return self.action.is_compute_done()
        else:
            raise UnboundLocalError('Exception raised, no strategyClass supplied to Segmentation')

    def compute(self, image):
        if self.action:
            self.action.compute(image)
        else:
            raise UnboundLocalError('Exception raised, no strategyClass supplied to Segmentation')

    def process(self, image):
        if self.action:
            return self.action.process(image)
        else:
            raise UnboundLocalError('Exception raised, no strategyClass supplied to Segmentation')


class SegmentationFactory(object):
    @staticmethod
    def get_instance(strategy="SIMPLE_SUBTRACTION_METHOD"):
        if strategy.upper() == "SIMPLE_SUBTRACTION_METHOD":
            from simple_subtraction_method import SimpleSubtractionMethod

            return Segmentation(SimpleSubtractionMethod)

        raise ValueError('No segmentation strategy with name "%s" found' % strategy)
