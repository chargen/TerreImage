# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QGIS_Edu
                                 A QGIS plugin
 Segmentation using OTB application
                              -------------------
        begin                : 2014-05-06
        copyright            : (C) 2014 by CNES
        email                : alexia.mondot@c-s.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 """

import os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_terre_image_curve import Ui_Form


class TerreImageCurve(QtGui.QWidget, Ui_Form):
    
    __pyqtSignals__ = ("curveTitleChanged(str)", "hideCurve(int)", "colorChanged(QtGui.QColor)", "deleteCurve()")
    
    
    
    
    def __init__(self, name, x, y, color, points):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
        self.name = name
        self.lineEdit_curve_name.setText(name)
        
        self.coordinates = "[ x=" + str(x) + ", " + str(y) + "]"
        self.label_coordinates.setText(self.coordinates)
        
        
        self.lettersToQColor = {"b": QColor(0, 132, 255),\
        "green": QColor(148, 255, 69),\
        "red": QColor(255, 30, 0),\
        "cyan": QColor(0, 255, 204),\
        "magenta": QColor(255, 0, 255),\
        "yellow": QColor(255, 255, 0),\
        "black": QColor(0, 0, 0),\
        "white": QColor(255, 255, 255)}
        self.lettersToNameColor = {"b": "blue",\
        "g": "green",\
        "r": "red",\
        "c": "cyan",\
        "m": "magenta",\
        "y": "yellow",\
        "k": "black",\
        "w": "white"}
        self.nameColorsToLetters = dict((v,k) for k, v in self.lettersToNameColor.iteritems())
        
        
        self.color = color
        
        pixmap = QtGui.QPixmap(self.pushButton_color.size())
        pixmap.fill(QColor(self.lettersToNameColor[self.color]))
        icon = QtGui.QIcon(pixmap)
        self.pushButton_color.setIcon(icon)
        
        self.points = points
        
        
        self.connect(self.lineEdit_curve_name, QtCore.SIGNAL("textChanged(str)"),  self, QtCore.SIGNAL("curveTitleChanged(str)"))
        self.connect(self.pushButton_color, QtCore.SIGNAL("clicked()"), self.set_color)
        self.connect(self.pushButton_delete_curve, QtCore.SIGNAL("clicked()"), self, QtCore.SIGNAL("deleteCurve()"))
        


    def display_points(self):
        return self.checkBox_curve_visible.checkState() == Qt.Checked
    
    def set_color(self):
        couleur = QtGui.QColorDialog.getColor(QtCore.Qt.white)
#         testqt, ok = QtGui.QInputDialog.getItem(iface.mainWindow(), "Couleur", "Selection d'une couleur", self.lettersToQColor.keys(), False)
#         if ok :
#             couleur = self.nameColorsToLetters[testqt]
#             print couleur
#         else :
#             couleur = "k"

        self.color = str(couleur.name())
        print couleur.name()
        
        pixmap = QtGui.QPixmap(self.pushButton_color.size())
        pixmap.fill(QColor(self.color))
        icon = QtGui.QIcon(pixmap)
        self.pushButton_color.setIcon(icon)
        print QColor(self.color)
        
        #self.pushButton_color.setStyleSheet("background-color: " + self.color )
 
 
#         palette = QtGui.QPalette()
#         #palette.setColor(QtGui.QPalette.ButtonText, self.lettersToQColor[testqt])
#         palette.setColor(10, couleur)
#         self.pushButton_color.setPalette(palette)
        #self.emit( QtCore.SIGNAL("colorChanged"), self.color )
        
        
        
        
        
    