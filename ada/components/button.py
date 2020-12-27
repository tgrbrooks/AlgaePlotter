from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
    QGraphicsDropShadowEffect, QSizePolicy)

import ada.configuration as config


class Button(QPushButton):
    def __init__(self, text, parent=None, tooltip=None, *args, **kwargs):
        super(Button, self).__init__(text, parent, *args, **kwargs)
        self.setStyleSheet(config.main_button_style)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=1, yOffset=1)
        self.setGraphicsEffect(shadow)
        if tooltip is not None:
            self.setToolTip(tooltip)

class BigButton(QPushButton):
    def __init__(self, text, parent=None, tooltip=None, *args, **kwargs):
        super(BigButton, self).__init__(text, parent, *args, **kwargs)
        self.setStyleSheet(config.big_button_style)
        shadow = QGraphicsDropShadowEffect(blurRadius=5, xOffset=1, yOffset=1)
        self.setGraphicsEffect(shadow)
        self.setFixedHeight(60)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        if tooltip is not None:
            self.setToolTip(tooltip)

class AddButton(QPushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(AddButton, self).__init__('+', parent, *args, **kwargs)
        self.setStyleSheet(config.add_button_style)
        shadow = QGraphicsDropShadowEffect(blurRadius=3, xOffset=1, yOffset=1)
        self.setGraphicsEffect(shadow)
        self.setFixedHeight(16)
        self.setFixedWidth(16)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

class DeleteButton(QPushButton):
    def __init__(self, parent=None, *args, **kwargs):
        super(DeleteButton, self).__init__('x', parent, *args, **kwargs)
        self.setStyleSheet(config.delete_button_style)
        shadow = QGraphicsDropShadowEffect(blurRadius=3, xOffset=1, yOffset=1)
        self.setGraphicsEffect(shadow)
        self.setFixedHeight(16)
        self.setFixedWidth(16)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)