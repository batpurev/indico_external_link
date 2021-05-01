# encoding=utf-8
from __future__ import unicode_literals
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
        self.template_hook('page-footer', self._inject_footer_links)

    def _extend_top_menu(self, sender, **kwargs):
        return TopMenuItem('my-menu-item', 'Google', 'https://www.google.com', weight=105)
    def _inject_footer_links(self, **kwargs):
        return '''
        <a href="#">aaa</a></il>
        <li><a href="#">bbb</a></il>
        <li><a href="#">ccc</a>
        '''
