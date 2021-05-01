from indico.web.menu import TopMenuItem
from indico.core import signals
from indico.core.plugins import IndicoPlugin


class MyCustomTopMenuLinkPlugin(IndicoPlugin):
    """My Custom Top Menu Link

    Add a new top menu link.
    """

    def init(self):
        super(MyCustomTopMenuLinkPlugin, self).init()
        self.connect(signals.menu.items, self._extend_top_menu, sender='top-menu')

    def _extend_top_menu(self, sender, **kwargs):
        return TopMenuItem('my-menu-item', 'Google', 'https://www.google.com', weight=95)
