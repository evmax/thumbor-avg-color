from thumbor.app import ThumborServiceApp
from thumbor.url import Url

from thumbor_avg_color.handlers.handler import Handler


class App(ThumborServiceApp):

    def get_handlers(self):
        handlers = super(App, self).get_handlers()
        handlers.insert(0, (Url.regex(), Handler, {'context': self.context}))
        return handlers
