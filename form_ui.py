# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 300)
        
        self.verticalLayout_8 = QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_distribution = QLabel(Form)
        self.label_distribution.setObjectName(u"label_distribution")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_distribution.sizePolicy().hasHeightForWidth())
        self.label_distribution.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(True)
        self.label_distribution.setFont(font)

        self.horizontalLayout.addWidget(self.label_distribution)

        self.comboBox_distribution = QComboBox(Form)
        self.comboBox_distribution.setObjectName(u"comboBox_distribution")

        self.horizontalLayout.addWidget(self.comboBox_distribution)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_disc = QLabel(Form)
        self.label_disc.setObjectName(u"label_disc")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_disc.sizePolicy().hasHeightForWidth())
        self.label_disc.setSizePolicy(sizePolicy1)
        self.label_disc.setFont(font)

        self.horizontalLayout.addWidget(self.label_disc)

        self.comboBox_disc = QComboBox(Form)
        self.comboBox_disc.setObjectName(u"comboBox_disc")

        self.horizontalLayout.addWidget(self.comboBox_disc)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_clean = QCheckBox(Form)
        self.checkBox_clean.setObjectName(u"checkBox_clean")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_clean.sizePolicy().hasHeightForWidth())
        self.checkBox_clean.setSizePolicy(sizePolicy2)
        self.checkBox_clean.setFont(font)

        self.horizontalLayout_5.addWidget(self.checkBox_clean)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.progressBar_clean = QProgressBar(Form)
        self.progressBar_clean.setObjectName(u"progressBar_clean")
        self.progressBar_clean.setStyleSheet(u" QProgressBar {\n"
"                border: 2px solid #333333;\n"
"                border-radius: 5px;\n"
"                text-align: center;\n"
"                background-color: #2b2b2b;\n"
"                color: white; \n"
"                font-weight: bold;\n"
"            }\n"
"            QProgressBar::chunk {\n"
"                background-color: #ff0000; \n"
"                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ff0000, stop:1 #990000);\n"
"                border-radius: 3px;\n"
"            }")
        self.progressBar_clean.setValue(0)

        self.verticalLayout_4.addWidget(self.progressBar_clean)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_record = QCheckBox(Form)
        self.checkBox_record.setObjectName(u"checkBox_record")
        self.checkBox_record.setFont(font)

        self.horizontalLayout_4.addWidget(self.checkBox_record)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.progressBar_record = QProgressBar(Form)
        self.progressBar_record.setObjectName(u"progressBar_record")
        self.progressBar_record.setStyleSheet(u" QProgressBar {\n"
"                border: 2px solid #333333;\n"
"                border-radius: 5px;\n"
"                text-align: center;\n"
"                background-color: #2b2b2b;\n"
"                color: white; \n"
"                font-weight: bold;\n"
"            }\n"
"            QProgressBar::chunk {\n"
"                background-color: #ff0000; \n"
"                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #ff0000, stop:1 #990000);\n"
"                border-radius: 3px;\n"
"            }")
        self.progressBar_record.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar_record)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 50, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton_run = QPushButton(Form)
        self.pushButton_run.setObjectName(u"pushButton_run")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.pushButton_run)

        self.horizontalSpacer_8 = QSpacerItem(40, 50, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_distribution.setText(QCoreApplication.translate("Form", u"Distribution:", None))
        self.label_disc.setText(QCoreApplication.translate("Form", u"Disc:", None))
        self.checkBox_clean.setText(QCoreApplication.translate("Form", u"Clean", None))
        self.checkBox_record.setText(QCoreApplication.translate("Form", u"Record", None))
        self.pushButton_run.setText(QCoreApplication.translate("Form", u"Run", None))
    # retranslateUi

