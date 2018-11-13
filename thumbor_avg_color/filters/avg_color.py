#!/usr/bin/python
# -*- coding: utf-8 -*-
from thumbor.filters import BaseFilter, filter_method
from thumbor.ext.filters import _fill


class Filter(BaseFilter):

    @filter_method()
    def avg_color(self):
        self.context.request.avg_color = self.get_median_color()

    def get_median_color(self):
        mode, data = self.engine.image_data_as_rgb()
        r, g, b = _fill.apply(mode, data)
        return '%02x%02x%02x' % (r, g, b)
