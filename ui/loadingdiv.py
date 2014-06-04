#!/usr/bin/python
# -*- coding: utf-8 -*-

### BEGIN LICENSE

# Copyright (C) 2013 National University of Defense Technology(NUDT) & Kylin Ltd

# Author:
#     Shine Huang<shenghuang@ubuntukylin.com>
# Maintainer:
#     Shine Huang<shenghuang@ubuntukylin.com>

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.


from PyQt4.QtGui import *
from PyQt4.QtCore import *
from models.enums import UBUNTUKYLIN_RES_PATH

class LoadingDiv(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        # self.setGeometry(40, 0, 815, 611)
        #
        # self.setAutoFillBackground(True)
        # palette = QPalette()
        # img = QPixmap(UBUNTUKYLIN_RES_PATH + "div1.png")
        # palette.setBrush(QPalette.Window, QBrush(img))
        # self.setPalette(palette)
        #
        # self.gif = QMovie(UBUNTUKYLIN_RES_PATH + "loading-big.gif")
        # self.loadinggif = QLabel(self)
        # self.loadinggif.setGeometry(815 / 2 - 25, 611 / 2 - 28, 58, 45)
        # self.loadinggif.setMovie(self.gif)
        # self.loadingtext = QLabel(self)
        # self.loadingtext.setGeometry(815 / 2 - 90, 611 / 2 + 28, 200, 20)
        # self.loadingtext.setAlignment(Qt.AlignCenter)
        # self.loadingtext.setStyleSheet("QLabel{color:#1E66A4;font-size:16px;}")

        self.setGeometry(0, 0, 815, 587)
        self.gif = QMovie(UBUNTUKYLIN_RES_PATH + "loading-big.gif")
        self.loadinggif = QLabel(self)
        self.loadinggif.setGeometry(815 / 2 - 73, 587 / 2 - 107, 146, 214)
        self.loadinggif.setMovie(self.gif)

        self.raise_()
        self.hide()

    def start_loading(self, loadingText):
        # self.loadingtext.setText(loadingText)
        self.gif.start()
        self.show()

    def stop_loading(self):
        self.gif.stop()
        self.hide()


class MiniLoadingDiv(QWidget):

    # parent of the request component
    parent_ = ''

    x_ = ''
    y_ = ''
    width_ = ''
    height_ = ''

    def __init__(self, onwhich, parent=None):
        QWidget.__init__(self, parent)

        self.parent_ = parent
        self.x_ = onwhich.x()
        self.y_ = onwhich.y()
        self.width_ = onwhich.width()
        self.height_ = onwhich.height()

        self.setGeometry(self.x_, self.y_, self.width_, self.height_)

        self.gif = QMovie(UBUNTUKYLIN_RES_PATH + "loading.gif")
        self.loadinggif = QLabel(self)
        self.loadinggif.setGeometry(self.width_ / 2 - 25, self.height_ / 2 - 25, 50, 50)
        self.loadinggif.setMovie(self.gif)
        # self.loadingtext = QLabel(self)
        # self.loadingtext.setGeometry(self.loadinggif.x() + 25 - 150, self.loadinggif.y() + 55, 300, 20)
        # self.loadingtext.setAlignment(Qt.AlignCenter)
        self.raise_()
        self.hide()

    def start_loading(self):
        self.gif.start()
        self.show()

    def stop_loading(self):
        self.gif.stop()
        self.hide()