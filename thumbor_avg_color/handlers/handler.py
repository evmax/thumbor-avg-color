#!/usr/bin/python
# -*- coding: utf-8 -*-
from thumbor.handlers.imaging import ImagingHandler


class Handler(ImagingHandler):

    def _write_results_to_client(self, results, content_type):
        avg_color = None
        try:
            avg_color = getattr(self.context.request, 'avg_color')
        except AttributeError:
            pass

        if avg_color is not None:
            self.set_header('X-Avg-Color', str(avg_color))
        super(Handler, self)._write_results_to_client(results, content_type)
