from PyQt5 import QtCore, QtGui, QtWidgets
import terms
import sys
import PyPDF2
import ast
import _ast


# Add all of the categories and questions to a dictionary
categories = {}
categories["Equity"] = terms.equity
categories["Buildout"] = terms.buildout
categories["Maintenance"] = terms.maintenance

# Setup the global variables to store the states, categories, and questions
selectedStates = {}
selectedCategories = []
categoryDictionary = {}
pageIndex = 0
questionIndex = 0
categoryIndex = 0
stateIndex = 0
buttonWasPushed = False
textList = {}
mode = "None"
currentTerms = []
currentQuestions = []
customTerms = []
lastMode = "None"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(51, 51, 51))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setFont(QtGui.QFont("Arial", 15))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.mainWidgetLayout = QtWidgets.QHBoxLayout(self.frame)
        self.mainWidgetLayout.setObjectName("mainWidgetLayout")
        self.catAndQuestionFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.catAndQuestionFrame.sizePolicy().hasHeightForWidth()
        )
        self.catAndQuestionFrame.setSizePolicy(sizePolicy)
        self.catAndQuestionFrame.setMinimumSize(QtCore.QSize(400, 0))
        self.catAndQuestionFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.catAndQuestionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.catAndQuestionFrame.setObjectName("catAndQuestionFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.catAndQuestionFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.catBox = QtWidgets.QGroupBox(self.catAndQuestionFrame)
        self.catBox.setFont(QtGui.QFont("Arial", 12))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.catBox.sizePolicy().hasHeightForWidth())
        self.catBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.catBox.setPalette(palette)
        self.catBox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.catBox.setObjectName("catBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.catBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maintenanceCheck = QtWidgets.QCheckBox(self.catBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.maintenanceCheck.sizePolicy().hasHeightForWidth()
        )
        self.maintenanceCheck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.maintenanceCheck.setFont(font)
        self.maintenanceCheck.setObjectName("maintenanceCheck")
        self.horizontalLayout.addWidget(self.maintenanceCheck)
        self.buildoutCheck = QtWidgets.QCheckBox(self.catBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.buildoutCheck.sizePolicy().hasHeightForWidth()
        )
        self.buildoutCheck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buildoutCheck.setFont(font)
        self.buildoutCheck.setObjectName("buildoutCheck")
        self.horizontalLayout.addWidget(self.buildoutCheck)
        self.equityCheck = QtWidgets.QCheckBox(self.catBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.equityCheck.sizePolicy().hasHeightForWidth())
        self.equityCheck.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.equityCheck.setFont(font)
        self.equityCheck.setObjectName("equityCheck")
        self.horizontalLayout.addWidget(self.equityCheck)
        self.verticalLayout_3.addWidget(self.catBox)
        self.questionBox = QtWidgets.QGroupBox(self.catAndQuestionFrame)
        self.questionBox.setFont(QtGui.QFont("Arial", 12))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.questionBox.sizePolicy().hasHeightForWidth())
        self.questionBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.questionBox.setPalette(palette)
        self.questionBox.setObjectName("questionBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.questionBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.questionCombo = QtWidgets.QComboBox(self.questionBox)
        self.questionCombo.activated.connect(self.updateQuestions)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.questionCombo.sizePolicy().hasHeightForWidth()
        )
        self.questionCombo.setSizePolicy(sizePolicy)
        self.questionCombo.setObjectName("questionCombo")
        self.verticalLayout_4.addWidget(self.questionCombo)
        self.questionCombo.setFont(QtGui.QFont("Arial", 15))

        # Stack
        self.stackedWidget = QtWidgets.QStackedWidget(self.questionBox)
        self.stackedWidget.setObjectName("stackedWidget")
        self.equityPage = QtWidgets.QWidget()
        self.equityPage.setObjectName("equityPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.equityPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.equityPage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.scrollArea_2.setPalette(palette)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollText_2 = QtWidgets.QWidget()
        self.scrollText_2.setGeometry(QtCore.QRect(0, 0, 507, 277))
        self.scrollText_2.setObjectName("scrollText_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.scrollText_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.selectAllEquity = QtWidgets.QCheckBox(self.scrollText_2)
        self.selectAllEquity.toggled.connect(self.checkAllEquity)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.selectAllEquity.sizePolicy().hasHeightForWidth()
        )
        self.selectAllEquity.setSizePolicy(sizePolicy)
        self.selectAllEquity.setObjectName("selectAllEquity")
        self.verticalLayout_12.addWidget(self.selectAllEquity)
        self.equityChecks = []
        # Create check boxes for each state
        for question in terms.equity:
            tempbox = QtWidgets.QCheckBox(question)
            tempbox.setFont(QtGui.QFont("Arial", 15))
            self.equityChecks.append(tempbox)
        # Add check boxes to layout
        for i, chkbox in enumerate(self.equityChecks):
            chkbox.setChecked(False)
            self.verticalLayout_12.addWidget(chkbox)

        self.scrollArea_2.setWidget(self.scrollText_2)
        self.verticalLayout_5.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.equityPage)
        self.buildoutPage = QtWidgets.QWidget()
        self.buildoutPage.setObjectName("buildoutPage")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.buildoutPage)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.buildoutPage)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.scrollArea_4.setPalette(palette)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollText_4 = QtWidgets.QWidget()
        self.scrollText_4.setGeometry(QtCore.QRect(0, 0, 295, 277))
        self.scrollText_4.setObjectName("scrollText_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.scrollText_4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.selectAllBuild = QtWidgets.QCheckBox(self.scrollText_4)
        self.selectAllBuild.toggled.connect(self.checkAllBuild)
        self.selectAllBuild.setObjectName("selectAllBuild")
        self.verticalLayout_13.addWidget(self.selectAllBuild)
        self.buildChecks = []
        # Create check boxes for each state
        for question in terms.buildout:
            tempbox = QtWidgets.QCheckBox(question)
            tempbox.setFont(QtGui.QFont("Arial", 15))
            self.buildChecks.append(tempbox)
        # Add check boxes to layout
        for i, chkbox in enumerate(self.buildChecks):
            chkbox.setChecked(False)
            self.verticalLayout_13.addWidget(chkbox)

        self.scrollArea_4.setWidget(self.scrollText_4)
        self.verticalLayout_11.addWidget(self.scrollArea_4)
        self.stackedWidget.addWidget(self.buildoutPage)
        self.maintenancePage = QtWidgets.QWidget()
        self.maintenancePage.setObjectName("maintenancePage")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.maintenancePage)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.maintenancePage)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollText_3 = QtWidgets.QWidget()
        self.scrollText_3.setGeometry(QtCore.QRect(0, 0, 721, 232))
        self.scrollText_3.setObjectName("scrollText_3")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scrollText_3)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.selectAllMain = QtWidgets.QCheckBox(self.scrollText_3)
        self.selectAllMain.toggled.connect(self.checkAllMain)
        self.selectAllMain.setObjectName("selectAllMain")
        self.verticalLayout_14.addWidget(self.selectAllMain)
        self.mainChecks = []
        # Create check boxes for each state
        for question in terms.maintenance:
            tempbox = QtWidgets.QCheckBox(question)
            tempbox.setFont(QtGui.QFont("Arial", 15))
            self.mainChecks.append(tempbox)

        # Add check boxes to layout
        for i, chkbox in enumerate(self.mainChecks):
            chkbox.setChecked(False)
            self.verticalLayout_14.addWidget(chkbox)
        self.scrollArea_3.setWidget(self.scrollText_3)
        self.verticalLayout_10.addWidget(self.scrollArea_3)
        self.stackedWidget.addWidget(self.maintenancePage)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_3.addWidget(self.questionBox)

        self.modeAndStateFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.modeAndStateFrame.sizePolicy().hasHeightForWidth()
        )
        self.modeAndStateFrame.setSizePolicy(sizePolicy)
        self.modeAndStateFrame.setMinimumSize(QtCore.QSize(450, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.modeAndStateFrame.setPalette(palette)
        self.modeAndStateFrame.setAutoFillBackground(True)
        self.modeAndStateFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modeAndStateFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modeAndStateFrame.setObjectName("modeAndStateFrame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.modeAndStateFrame)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.modeBox = QtWidgets.QGroupBox(self.modeAndStateFrame)
        self.modeBox.setFont(QtGui.QFont("Arial", 12))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeBox.sizePolicy().hasHeightForWidth())
        self.modeBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.modeBox.setPalette(palette)
        font = QtGui.QFont()
        font.setItalic(False)
        self.modeBox.setObjectName("modeBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.modeBox)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.customRadio = QtWidgets.QRadioButton(self.modeBox)
        self.customRadio.toggled.connect(self.customSelected)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customRadio.sizePolicy().hasHeightForWidth())
        self.customRadio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.customRadio.setFont(font)
        self.customRadio.setObjectName("customRadio")
        self.verticalLayout_8.addWidget(self.customRadio)
        self.presetRadio = QtWidgets.QRadioButton(self.modeBox)
        self.presetRadio.toggled.connect(self.presetSelected)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presetRadio.sizePolicy().hasHeightForWidth())
        self.presetRadio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.presetRadio.setFont(font)
        self.presetRadio.setObjectName("presetRadio")
        self.verticalLayout_8.addWidget(self.presetRadio)
        self.verticalLayout_7.addWidget(self.modeBox)
        self.stateBox = QtWidgets.QGroupBox(self.modeAndStateFrame)
        self.stateBox.setFont(QtGui.QFont("Arial", 12))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateBox.sizePolicy().hasHeightForWidth())
        self.stateBox.setSizePolicy(sizePolicy)
        self.stateBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.stateBox.setBaseSize(QtCore.QSize(0, 0))
        self.stateBox.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.stateBox.setObjectName("stateBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.stateBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.scrollArea = QtWidgets.QScrollArea(self.stateBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollText = QtWidgets.QWidget()
        self.scrollText.setGeometry(QtCore.QRect(0, 0, 158, 290))
        self.scrollText.setObjectName("scrollText")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollText)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.scrollText)
        self.checkBox.toggled.connect(self.checkAllStates)
        self.checkBox.setFont(QtGui.QFont("Arial", 15))

        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.scrollArea.setWidget(self.scrollText)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_7.addWidget(self.stateBox)

        self.verticalLayout.addWidget(self.frame)
        self.startButton = QtWidgets.QPushButton(self.frame_2)
        self.startButton.clicked.connect(self.startNPKS)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.gridLayout_3.addWidget(self.frame_2, 0, 2, 3, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Text Viewer
        self.textFrame = QtWidgets.QFrame(self.frame)
        self.textFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textFrame.setObjectName("textFrame")
        self.textViewerLayout = QtWidgets.QVBoxLayout(self.textFrame)
        self.textViewerLayout.setObjectName("textViewerLayout")
        self.currentStateLabel = QtWidgets.QLabel(self.textFrame)
        self.currentStateLabel.setFont(QtGui.QFont("Arial", 14))
        self.currentStateLabel.setObjectName("currentStateLabel")
        self.textViewerLayout.addWidget(
            self.currentStateLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.currentCategoryLabel = QtWidgets.QLabel(self.textFrame)
        self.currentCategoryLabel.setFont(QtGui.QFont("Arial", 14))
        self.currentCategoryLabel.setObjectName("currentCategoryLabel")
        self.textViewerLayout.addWidget(
            self.currentCategoryLabel,
            0,
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
        )
        self.currentQuestionLabel = QtWidgets.QLabel(self.textFrame)
        self.currentQuestionLabel.setFont(QtGui.QFont("Arial", 14))
        self.currentQuestionLabel.setObjectName("currentQuestionLabel")
        self.textViewerLayout.addWidget(
            self.currentQuestionLabel,
            0,
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter,
        )
        self.pageSwapFrame = QtWidgets.QFrame(self.textFrame)
        self.pageSwapFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pageSwapFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pageSwapFrame.setObjectName("pageSwapFrame")
        self.textViewerHLayout = QtWidgets.QHBoxLayout(self.pageSwapFrame)
        self.textViewerHLayout.setObjectName("textViewerHLayout")
        self.previousState = QtWidgets.QPushButton(self.pageSwapFrame)
        self.previousState.clicked.connect(self.prevStatePush)
        self.previousState.setObjectName("previousState")
        self.textViewerHLayout.addWidget(self.previousState)
        self.previousQuestion = QtWidgets.QPushButton(self.pageSwapFrame)
        self.previousQuestion.clicked.connect(self.prevQuestionPush)
        self.previousQuestion.setEnabled(True)
        self.previousQuestion.setObjectName("previousQuestion")
        self.textViewerHLayout.addWidget(self.previousQuestion)
        self.nextQuestion = QtWidgets.QPushButton(self.pageSwapFrame)
        self.nextQuestion.clicked.connect(self.nextQuestionPush)
        self.nextQuestion.setObjectName("nextQuestion")
        self.textViewerHLayout.addWidget(self.nextQuestion)
        self.nextState = QtWidgets.QPushButton(self.pageSwapFrame)
        self.nextState.clicked.connect(self.nextStatePush)
        self.nextState.setObjectName("nextState")
        self.textViewerHLayout.addWidget(self.nextState)
        self.textViewerLayout.addWidget(self.pageSwapFrame)
        self.textViewer = QtWidgets.QScrollArea(self.textFrame)
        self.textViewer.setWidgetResizable(True)
        self.textViewer.setObjectName("textViewer")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 440, 393))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalTextViewer = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalTextViewer.setObjectName("verticalTextViewer")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setFont(QtGui.QFont("Arial", 14))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.verticalTextViewer.addWidget(self.textEdit)
        self.textViewer.setWidget(self.scrollAreaWidgetContents)
        self.textViewerLayout.addWidget(self.textViewer)
        self.pageNumberLabel = QtWidgets.QLabel(self.textFrame)
        self.pageNumberLabel.setObjectName("pageNumberLabel")
        self.textViewerLayout.addWidget(
            self.pageNumberLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.textViewerFrame = QtWidgets.QFrame(self.textFrame)
        self.textViewerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textViewerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textViewerFrame.setObjectName("textViewerFrame")
        self.textViewerHLayout_2 = QtWidgets.QHBoxLayout(self.textViewerFrame)
        self.textViewerHLayout_2.setObjectName("textViewerHLayout_2")
        self.previousPage = QtWidgets.QPushButton(self.textViewerFrame)
        self.previousPage.clicked.connect(self.printPreviousPage)
        self.previousPage.setObjectName("previousPage")
        self.textViewerHLayout_2.addWidget(self.previousPage)
        self.nextPage = QtWidgets.QPushButton(self.textViewerFrame)
        self.nextPage.clicked.connect(self.printNextPage)
        self.nextPage.setObjectName("nextPage")
        self.textViewerHLayout_2.addWidget(self.nextPage)
        self.textViewerLayout.addWidget(self.textViewerFrame)
        self.exitButton = QtWidgets.QPushButton(self.textFrame)
        self.exitButton.clicked.connect(self.returnToMenu)
        self.exitButton.setObjectName("exitButton")
        self.textViewerLayout.addWidget(self.exitButton)
        self.verticalLayout.addWidget(self.textFrame)

        # Custom terms
        self.customGroupBox = QtWidgets.QGroupBox(self.frame)
        self.customGroupBox.setFont(QtGui.QFont("Arial", 12))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.customGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.customGroupBox.setSizePolicy(sizePolicy)
        self.customGroupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.customGroupBox.setObjectName("customGroupBox")
        self.customVertical_9 = QtWidgets.QVBoxLayout(self.customGroupBox)
        self.customVertical_9.setObjectName("customVertical_9")
        self.customInput = QtWidgets.QLineEdit(self.customGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customInput.sizePolicy().hasHeightForWidth())
        self.customInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.customInput.setFont(font)
        self.customInput.setObjectName("customInput")
        self.customVertical_9.addWidget(self.customInput)
        self.customTermFrame = QtWidgets.QFrame(self.customGroupBox)
        self.customTermFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.customTermFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.customTermFrame.setObjectName("customTermFrame")
        self.customHorizontal_2 = QtWidgets.QHBoxLayout(self.customTermFrame)
        self.customHorizontal_2.setObjectName("customHorizontal_2")
        self.addWordsButton = QtWidgets.QPushButton(self.customTermFrame)
        self.addWordsButton.clicked.connect(self.addTerm)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.addWordsButton.setFont(font)
        self.addWordsButton.setObjectName("addWordsButton")
        self.customHorizontal_2.addWidget(self.addWordsButton)
        self.removeWordsButton = QtWidgets.QPushButton(self.customTermFrame)
        self.removeWordsButton.clicked.connect(self.deleteTerm)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.removeWordsButton.setFont(font)
        self.removeWordsButton.setObjectName("removeWordsButton")
        self.customHorizontal_2.addWidget(self.removeWordsButton)
        self.clearWordsButton = QtWidgets.QPushButton(self.customTermFrame)
        self.clearWordsButton.clicked.connect(self.clearTerms)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.clearWordsButton.setFont(font)
        self.clearWordsButton.setObjectName("clearWordsButton")
        self.customHorizontal_2.addWidget(self.clearWordsButton)
        self.customVertical_9.addWidget(self.customTermFrame)
        self.customList = QtWidgets.QListWidget(self.customGroupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.customList.setFont(font)
        self.customList.setObjectName("customList")
        self.customVertical_9.addWidget(self.customList)

        self.mainWidgetLayout.addWidget(self.modeAndStateFrame)
        self.mainWidgetLayout.addWidget(self.customGroupBox)
        self.mainWidgetLayout.addWidget(self.catAndQuestionFrame)

        self.catAndQuestionFrame.hide()
        self.catBox.hide()
        self.textFrame.hide()
        self.customGroupBox.hide()

        # Category check boxes
        self.categoryChecks = []
        self.categoryChecks.append(self.maintenanceCheck)
        self.categoryChecks.append(self.buildoutCheck)
        self.categoryChecks.append(self.equityCheck)

        tempCategories = ["Equity", "Buildout", "Maintenance"]
        self.questionCombo.addItems(tempCategories)

        # States check boxes
        statesLayout = QtWidgets.QVBoxLayout()
        self.stateChecks = []
        self.stateChecks.append(self.checkBox)
        # Create check boxes for each state
        for state in terms.states:
            tempbox = QtWidgets.QCheckBox(terms.states[state])
            tempbox.setFont(QtGui.QFont("Arial", 15))
            self.stateChecks.append(tempbox)
        # Add check boxes to layout
        for i, chkbox in enumerate(self.stateChecks):
            chkbox.setChecked(False)
            statesLayout.addWidget(chkbox)
        statesLayout.addStretch(1)
        statesLayout.setContentsMargins(0, 0, 0, 0)
        statesLayout.setSpacing(0)
        # Create states widget
        stateWidget = QtWidgets.QWidget()
        stateWidget.setStyleSheet(
            """.QWidget {background-color: rgb(255, 255, 255);}"""
        )
        stateWidget.setLayout(statesLayout)
        self.scrollArea.setWidget(stateWidget)

        emptyWidget = QtWidgets.QWidget()
        self.stackedWidget.addWidget(emptyWidget)
        self.stackedWidget.addWidget(self.equityPage)
        self.stackedWidget.addWidget(self.buildoutPage)
        self.stackedWidget.addWidget(self.maintenancePage)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "State Plan Keyword Search"))
        self.label_3.setText(_translate("MainWindow", "State Plan Keyword Search"))
        self.catBox.setTitle(_translate("MainWindow", "Categories"))
        self.maintenanceCheck.setText(_translate("MainWindow", "Equity"))
        self.maintenanceCheck.setFont(QtGui.QFont("Arial", 15))
        self.buildoutCheck.setText(_translate("MainWindow", "Buildout"))
        self.buildoutCheck.setFont(QtGui.QFont("Arial", 15))
        self.equityCheck.setText(_translate("MainWindow", "Maintenance"))
        self.equityCheck.setFont(QtGui.QFont("Arial", 15))
        self.questionBox.setTitle(_translate("MainWindow", "Questions"))
        self.selectAllEquity.setText(_translate("MainWindow", "Select All"))
        self.selectAllEquity.setFont(QtGui.QFont("Arial", 15))
        self.selectAllBuild.setText(_translate("MainWindow", "Select All"))
        self.selectAllBuild.setFont(QtGui.QFont("Arial", 15))
        self.selectAllMain.setText(_translate("MainWindow", "Select All"))
        self.selectAllMain.setFont(QtGui.QFont("Arial", 15))
        self.modeBox.setTitle(_translate("MainWindow", "Mode"))
        self.customRadio.setText(_translate("MainWindow", "Custom Keywords"))
        self.customRadio.setFont(QtGui.QFont("Arial", 15))
        self.presetRadio.setText(_translate("MainWindow", "Preset Keywords"))
        self.presetRadio.setFont(QtGui.QFont("Arial", 15))
        self.stateBox.setTitle(_translate("MainWindow", "States"))
        self.checkBox.setText(_translate("MainWindow", "Select All"))
        self.startButton.setText(_translate("MainWindow", "START SEARCH"))

        self.currentStateLabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentCategoryLabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentQuestionLabel.setText(_translate("MainWindow", "TextLabel"))
        self.previousQuestion.setText(_translate("MainWindow", "Previous Question"))
        self.nextQuestion.setText(_translate("MainWindow", "Next Question"))
        self.previousPage.setText(_translate("MainWindow", "Previous Page"))
        self.nextPage.setText(_translate("MainWindow", "Next Page"))
        self.nextState.setText(_translate("MainWindow", "Next State"))
        self.previousState.setText(_translate("MainWindow", "Previous State"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.customGroupBox.setTitle(_translate("MainWindow", "Type Custom Words"))
        self.addWordsButton.setText(_translate("MainWindow", "Add Set"))
        self.removeWordsButton.setText(_translate("MainWindow", "Remove Set"))
        self.clearWordsButton.setText(_translate("MainWindow", "Clear Sets"))
        MainWindow.showMaximized()

    # RADIO BUTTONS FOR MODE SELECT
    def presetSelected(self, selected):
        global mode
        if selected:
            mode = "Preset"
            self.catAndQuestionFrame.show()
            self.customGroupBox.hide()

    def customSelected(self, selected):
        global mode
        if selected:
            mode = "Custom"
            self.catAndQuestionFrame.hide()
            self.customGroupBox.show()

    # CHECKBOXES FOR STATES
    def checkAllStates(self, state):
        for checkbox in self.stateChecks:
            checkbox.setCheckState(state)

    def checkAllEquity(self, state):
        for checkbox in self.equityChecks:
            checkbox.setCheckState(state)

    def checkAllBuild(self, state):
        for checkbox in self.buildChecks:
            checkbox.setCheckState(state)

    def checkAllMain(self, state):
        for checkbox in self.mainChecks:
            checkbox.setCheckState(state)

    # COMBOBOX FOR CATEGORIES AND QUESTIONS
    def updateQuestions(self):
        index = self.questionCombo.currentText()
        if index == "Equity":
            self.stackedWidget.setCurrentIndex(1)
        elif index == "Buildout":
            self.stackedWidget.setCurrentIndex(2)
        elif index == "Maintenance":
            self.stackedWidget.setCurrentIndex(3)
        else:
            self.stackedWidget.setCurrentIndex(0)

    # Signal when next question is pushed
    def nextQuestionPush(self):
        global buttonWasPushed
        global questionIndex
        if questionIndex + 1 < len(currentQuestions):
            questionIndex += 1
            if questionIndex == len(currentQuestions):
                self.nextQuestion.setDisabled(True)
            if questionIndex > 0:
                self.previousQuestion.setEnabled(True)
        buttonWasPushed = True

    # Signal when previous question button is pushed
    def prevQuestionPush(self):
        global buttonWasPushed
        global questionIndex
        if questionIndex - 1 >= 0:
            questionIndex = questionIndex - 1
            if questionIndex == 0:
                self.previousQuestion.setDisabled(True)
            if pageIndex < len(textList) - 1:
                self.nextQuestion.setEnabled(True)
        buttonWasPushed = True

    # Wait until previous/next question buttons are pressed
    def waitForAChange(self):
        global buttonWasPushed
        while buttonWasPushed != True:
            QtCore.QCoreApplication.processEvents()
        buttonWasPushed = False

    # Signal to break out of the while loop
    def nextStatePush(self):
        global buttonWasPushed
        global stateIndex
        if stateIndex + 1 < len(selectedStates):
            stateIndex += 1
            if stateIndex == len(selectedStates) - 1:
                self.nextState.setDisabled(True)
            if stateIndex > 0:
                self.previousState.setEnabled(True)
        buttonWasPushed = True

    def prevStatePush(self):
        global buttonWasPushed
        global stateIndex
        if stateIndex - 1 > -1:
            stateIndex -= 1
            if stateIndex == 0:
                self.previousState.setDisabled(True)
            if stateIndex < len(selectedStates) - 1:
                self.nextState.setEnabled(True)
        buttonWasPushed = True

    def showDialog(self, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setText(message)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    # Highlight the terms in the text
    def highlightText(self, text, terms, page):
        self.textEdit.setText(text)
        self.pageNumberLabel.setText("Current Page: " + str(int(page) + 1))
        cursor = self.textEdit.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("Yellow")))

        for term in terms:
            # Setup the regex engine
            if term == " ":
                continue
            regex = QtCore.QRegExp(term)
            regex.setCaseSensitivity(0)
            # Process the displayed document
            pos = 0
            index = regex.indexIn(self.textEdit.toPlainText(), pos)
            while index != -1:
                # Select the matched text and apply the desired format
                cursor.setPosition(index)
                cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
                cursor.mergeCharFormat(format)
                # Move to the next match
                pos = index + regex.matchedLength()
                index = regex.indexIn(self.textEdit.toPlainText(), pos)

    # Print the next page in the list
    def printNextPage(self):
        global pageIndex
        global textList
        global currentTerms
        if pageIndex + 1 < len(textList):
            pageIndex += 1
            self.highlightText(
                list(textList.values())[pageIndex],
                currentTerms,
                list(textList)[pageIndex],
            )
            if pageIndex == len(textList) - 1:
                self.nextPage.setDisabled(True)
            if pageIndex > 0:
                self.previousPage.setEnabled(True)

    # Print the previous page in the list
    def printPreviousPage(self):
        global pageIndex
        global textList
        if pageIndex - 1 >= 0:
            pageIndex = pageIndex - 1
            self.highlightText(
                list(textList.values())[pageIndex],
                currentTerms,
                list(textList)[pageIndex],
            )
            if pageIndex == 0:
                self.previousPage.setDisabled(True)
            if pageIndex < len(textList) - 1:
                self.nextPage.setEnabled(True)

    def returnToMenu(self):
        global lastMode
        # Show and hide
        self.currentCategoryLabel.show()
        self.currentQuestionLabel.show()
        self.currentStateLabel.show()
        self.catAndQuestionFrame.show()
        self.nextQuestion.show()
        self.previousQuestion.show()
        self.textFrame.hide()
        self.presetRadio.setChecked(False)
        self.customRadio.setChecked(False)

        self.frame.show()
        self.startButton.show()
        self.catAndQuestionFrame.hide()
        self.customGroupBox.hide()

        if lastMode == "Custom":
            self.customGroupBox.show()
        if lastMode == "Preset":
            self.catAndQuestionFrame.show()

    def addTerm(self):
        global customTerms
        item = self.customInput.text()
        itemList = item.split(", ")
        customTerms.append(itemList)
        self.customList.addItem(item)
        self.customInput.setText("")

    def deleteTerm(self):
        global customTerms
        getList = self.customList.currentItem().text().split(", ")
        customTerms.remove(getList)
        clicked = self.customList.currentRow()
        self.customList.takeItem(clicked)

    def clearTerms(self):
        global customTerms
        self.customList.clear()
        customTerms = []

    # Gets the selected states and converts to a dictionary
    def getStates(self) -> dict:
        # Global to store user selected states
        # Convert a list of states into a dictionary with abbreviation of state as key
        def makeDict(searchStates) -> dict:
            returnStates = {}
            for state in terms.states:
                # for each state input, if it matches a state abbreviation add it to a dictionary
                for checkStates in searchStates:
                    if checkStates == terms.states[state]:
                        returnStates[state] = checkStates
            if searchStates == ["All"]:
                returnStates = terms.states
            return returnStates

        # For each checked box, add the state to selected states dict
        inputStates = []
        for checkbox in self.stateChecks:
            if checkbox.isChecked():
                inputStates.append(checkbox.text())
        return makeDict(inputStates)

    # Get the questions from the checkboxes
    def getQuestions(self) -> dict:
        global selectedCategories
        retQuestions = {}
        tempDict = {}
        for question in self.equityChecks:
            if question.isChecked():
                tempDict[question.text()] = terms.equity[question.text()]
        if len(list(tempDict)) > 0:
            selectedCategories.append("Equity")
            retQuestions["Equity"] = tempDict
        tempDict = {}
        for question in self.buildChecks:
            if question.isChecked():
                tempDict[question.text()] = terms.buildout[question.text()]
        if len(list(tempDict)) > 0:
            selectedCategories.append("Buildout")
            retQuestions["Buildout"] = tempDict
        tempDict = {}
        for question in self.mainChecks:
            if question.isChecked():
                tempDict[question.text()] = terms.maintenance[question.text()]
        if len(list(tempDict)) > 0:
            selectedCategories.append("Maintenance")
            retQuestions["Maintenance"] = tempDict
        return retQuestions

    def startNPKS(self):
        global selectedStates
        global selectedCategories
        global categoryDictionary
        global mode
        global customTerms
        global questionIndex
        global lastMode

        # Print out the custom keywords
        def runCustom(self):
            global customTerms
            global selectedStates
            global stateIndex

            self.currentQuestionLabel.setText("")

            # Index through the states in a while loop to allow backwards indexing
            if len(selectedStates) == 1:
                self.nextState.setDisabled(True)
            else:
                self.nextState.setEnabled(True)
            self.previousState.setDisabled(True)
            stateIndex = 0
            while True:
                # get the state info from the index
                state = list(selectedStates)[stateIndex]
                self.currentStateLabel.setText("State: " + terms.states[state])

                # open the states plan and read the pdf
                plan = open("plans/" + state.lower() + "_nevi_plan.pdf", "rb")
                pdfReader = PyPDF2.PdfFileReader(plan, strict=False)

                # Create a dict to hold pages containing the words
                global textList
                textList = {}

                # For each page in the pdf
                for page in range(pdfReader.numPages):
                    # Extract the text
                    pageObj = pdfReader.getPage(page)
                    Text = pageObj.extractText()
                    # Check if all the terms are on the page
                    termCounter = 0
                    searchText = Text.strip(" ").strip().lower()
                    # For each list of terms
                    global currentTerms
                    currentTerms = []
                    for termList in customTerms:
                        currentTerms += termList
                        if (
                            any(term.lower() in searchText for term in termList)
                            and "............" not in Text
                        ):
                            termCounter += 1
                    if termCounter >= len(customTerms):
                        # If the page passes the test, then add its text to the list
                        textList[str(page)] = Text

                self.previousPage.setDisabled(True)
                self.nextPage.setEnabled(True)

                if len(list(textList)) < 1:
                    textList[0] = "Nothing found..."
                if len(list(textList)) <= 1:
                    self.nextPage.setDisabled(True)

                global pageIndex
                pageIndex = 0

                # Print the first page and then allow the user to navigate through the pages
                self.highlightText(
                    list(textList.values())[pageIndex],
                    currentTerms,
                    list(textList)[pageIndex],
                )

                # Loop until user move on to next state
                self.waitForAChange()

        # Print out keywords from the presets
        def runPreset(self):
            global selectedStates
            global categoryDictionary
            global stateIndex
            global categoryIndex
            global questionIndex
            global currentQuestions

            categoryIndex = 0
            self.previousState.setDisabled(True)
            stateIndex = 0
            self.previousQuestion.setDisabled(True)
            questionIndex = 0

            # continue until user exits
            while True:
                # get the state info from the index
                state = list(selectedStates)[stateIndex]
                self.currentStateLabel.setText("Current State: " + terms.states[state])
                plan = open("plans/" + state.lower() + "_nevi_plan.pdf", "rb")
                pdfReader = PyPDF2.PdfFileReader(plan, strict=False)

                # get the category info from index
                category = list(categoryDictionary)[categoryIndex]
                questions = categoryDictionary[category]
                currentQuestions = list(questions)
                self.currentCategoryLabel.setText("Category: " + category)

                # get question info from index
                question = list(questions)[questionIndex]
                questionTerms = categoryDictionary[category][question]
                self.currentQuestionLabel.setText("Question: " + question)

                # Check if number of questions is equal to one to disable the nextQuestion
                if len(currentQuestions) == 1:
                    self.nextQuestion.setDisabled(True)
                else:
                    self.nextQuestion.setEnabled(True)

                # Create list to store text
                global textList
                textList = {}

                # Check if number of pages is equal to one to disable the nextPage
                if len(textList) == 1:
                    self.nextPage.setDisabled(True)
                else:
                    self.nextPage.setEnabled(True)

                # Check if number of states is equal to one to disable nextState
                if len(selectedStates) == 1:
                    self.nextState.setDisabled(True)
                else:
                    self.nextState.setEnabled(True)

                # For each page in the pdf
                for page in range(pdfReader.numPages):

                    # Extract the text
                    pageObj = pdfReader.getPage(page)
                    Text = pageObj.extractText()

                    # Check if all the terms are on the page
                    termCounter = 0
                    searchText = Text.strip(" ").strip().lower()

                    # For each list of terms
                    global currentTerms
                    currentTerms = []
                    for termList in questionTerms:
                        currentTerms += termList
                        if (
                            any(term.lower() in searchText for term in termList)
                            and "............" not in Text
                        ):
                            termCounter += 1
                    if termCounter >= len(questionTerms):
                        # If the page passes the test, then add its text to the list
                        textList[str(page)] = Text

                global pageIndex
                pageIndex = 0

                if len(list(textList)) < 1:
                    textList[0] = "Nothing found..."
                if len(list(textList)) <= 1:
                    self.nextPage.setDisabled(True)

                # Highlight the first page
                self.previousPage.setDisabled(True)
                self.highlightText(
                    list(textList.values())[pageIndex],
                    currentTerms,
                    list(textList)[pageIndex],
                )

                self.waitForAChange()

        # Get the dict for states
        selectedStates = self.getStates()

        # Check states
        if len(selectedStates) == 0:
            self.showDialog("Select a state!")
            return

        # Check Modes
        if mode == "Custom":
            # Check custom terms
            if len(customTerms) < 1:
                self.showDialog("Input Terms!")
                return
            lastMode = "Custom"
            self.frame.hide()
            self.startButton.hide()
            self.nextQuestion.hide()
            self.previousQuestion.hide()
            self.currentCategoryLabel.hide()
            self.textFrame.show()
            runCustom(self)
        elif mode == "Preset":
            # Check for categories selected
            categoryDictionary = self.getQuestions()
            if len(selectedCategories) == 0:
                self.showDialog("Select a question!")
                return
            lastMode = "Preset"
            self.frame.hide()
            self.startButton.hide()
            self.textFrame.show()
            runPreset(self)
        else:
            self.showDialog("Select a mode!")
            return


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("wpiLogo.png"))
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle("State Plan Keyword Search")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
