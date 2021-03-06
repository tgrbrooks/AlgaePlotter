from PyQt5.QtWidgets import QWidget, QListWidget, QGraphicsDropShadowEffect

import ada.configuration as config


class List(QListWidget):
    def __init__(self, parent=False, tooltip=None, *args, **kwargs):
        super(List, self).__init__(parent, *args, **kwargs)

        self.setStyleSheet(config.scroll_style)
        
        if tooltip is not None:
            self.setToolTip(tooltip)
