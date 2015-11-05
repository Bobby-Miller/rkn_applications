# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rkn_log.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import datetime as dt
import pyodbc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 575)

        app_icon = QtGui.QIcon()
        app_icon.addFile('fypy_logo.ico', QtCore.QSize(256, 256))
        app.setWindowIcon(app_icon)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        # Build Menu & Status Bar
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        # Build main label and separating lines.
        self.app_label = QtGui.QLabel(self.centralwidget)
        self.app_label.setTextFormat(QtCore.Qt.AutoText)
        self.app_label.setScaledContents(False)
        self.app_label.setAlignment(QtCore.Qt.AlignCenter)
        self.app_label.setObjectName(_fromUtf8("app_label"))
        self.gridLayout.addWidget(self.app_label, 4, 3, 1, 1)

        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 8, 0, 2, 5)

        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 18, 0, 2, 5)

        # Build Label Objects

        # A - Cumbustion Air
        self.combustion_air_label = QtGui.QLabel(self.centralwidget)
        self.combustion_air_label.setObjectName(_fromUtf8("combustion_air_label"))
        self.gridLayout.addWidget(self.combustion_air_label, 9, 1, 1, 1)

        # B - Atomizing Air
        self.atomizing_air_label = QtGui.QLabel(self.centralwidget)
        self.atomizing_air_label.setObjectName(_fromUtf8("atomizing_air_label"))
        self.gridLayout.addWidget(self.atomizing_air_label, 12, 1, 1, 1)

        # C - Natural Gas
        self.nat_gas_label = QtGui.QLabel(self.centralwidget)
        self.nat_gas_label.setObjectName(_fromUtf8("nat_gas_label"))
        self.gridLayout.addWidget(self.nat_gas_label, 15, 1, 1, 1)

        # 1 - Temp Setpoint
        self.temp_sp_label = QtGui.QLabel(self.centralwidget)
        self.temp_sp_label.setObjectName(_fromUtf8("temp_sp_label"))
        self.gridLayout.addWidget(self.temp_sp_label, 5, 1, 1, 1)

        # 2 - Temp Actual
        self.temp_act_label = QtGui.QLabel(self.centralwidget)
        self.temp_act_label.setObjectName(_fromUtf8("temp_act_label"))
        self.gridLayout.addWidget(self.temp_act_label, 5, 3, 1, 1)

        # 3 - Combustion Air Valve Output
        self.ca_vlv_op_label = QtGui.QLabel(self.centralwidget)
        self.ca_vlv_op_label.setObjectName(_fromUtf8("ca_vlv_op_label"))
        self.gridLayout.addWidget(self.ca_vlv_op_label, 5, 4, 1, 1)

        # 4 - Left Combustion Air
        self.ca_left_label = QtGui.QLabel(self.centralwidget)
        self.ca_left_label.setObjectName(_fromUtf8("ca_left_label"))
        self.gridLayout.addWidget(self.ca_left_label, 10, 1, 1, 1)

        # 5 - Right Combustion Air
        self.ca_right_label = QtGui.QLabel(self.centralwidget)
        self.ca_right_label.setObjectName(_fromUtf8("ca_right_label"))
        self.gridLayout.addWidget(self.ca_right_label, 10, 3, 1, 1)

        # 6 - dP Combustion Air
        self.ca_dp_label = QtGui.QLabel(self.centralwidget)
        self.ca_dp_label.setObjectName(_fromUtf8("ca_dp_label"))
        self.gridLayout.addWidget(self.ca_dp_label, 10, 4, 1, 1)

        # 7 - Top Atomizing Air
        self.aa_top_label = QtGui.QLabel(self.centralwidget)
        self.aa_top_label.setObjectName(_fromUtf8("aa_top_label"))
        self.gridLayout.addWidget(self.aa_top_label, 13, 1, 1, 1)

        # 8 - Bottom Atomizing Air
        self.aa_bottom_label = QtGui.QLabel(self.centralwidget)
        self.aa_bottom_label.setObjectName(_fromUtf8("aa_bottom_label"))
        self.gridLayout.addWidget(self.aa_bottom_label, 13, 3, 1, 1)

        # 9 - dP Atomizing Air
        self.aa_dp_label = QtGui.QLabel(self.centralwidget)
        self.aa_dp_label.setObjectName(_fromUtf8("aa_dp_label"))
        self.gridLayout.addWidget(self.aa_dp_label, 13, 4, 1, 1)

        # 10 - Left Nat Gas
        self.ng_left_label = QtGui.QLabel(self.centralwidget)
        self.ng_left_label.setObjectName(_fromUtf8("ng_left_label"))
        self.gridLayout.addWidget(self.ng_left_label, 16, 1, 1, 1)

        # 11 - Right Nat Gas
        self.ng_right_label = QtGui.QLabel(self.centralwidget)
        self.ng_right_label.setObjectName(_fromUtf8("ng_right_label"))
        self.gridLayout.addWidget(self.ng_right_label, 16, 3, 1, 1)

        # 12 - dP Gas
        self.ng_dp_label = QtGui.QLabel(self.centralwidget)
        self.ng_dp_label.setObjectName(_fromUtf8("ng_dp_label"))
        self.gridLayout.addWidget(self.ng_dp_label, 16, 4, 1, 1)

        # 13 - Bleeder Impulse Pressure
        self.bleed_impulse_pres_label = QtGui.QLabel(self.centralwidget)
        self.bleed_impulse_pres_label.setObjectName(_fromUtf8("bleed_impulse_pres_label"))
        self.gridLayout.addWidget(self.bleed_impulse_pres_label, 19, 1, 1, 2)

        # 14 - West Wall Damper Setting
        self.ww_damper_label = QtGui.QLabel(self.centralwidget)
        self.ww_damper_label.setObjectName(_fromUtf8("ww_damper_label"))
        self.gridLayout.addWidget(self.ww_damper_label, 19, 3, 1, 1)

        # 15 - Prab Temp
        self.prab_temp_label = QtGui.QLabel(self.centralwidget)
        self.prab_temp_label.setObjectName(_fromUtf8("prab_temp_label"))
        self.gridLayout.addWidget(self.prab_temp_label, 19, 4, 1, 1)

        # Build Input Field Objects

        # 1 - Temp Setpoint
        self.temp_sp_input = QtGui.QLineEdit(self.centralwidget)
        self.temp_sp_input.setObjectName(_fromUtf8("temp_sp_input"))
        self.gridLayout.addWidget(self.temp_sp_input, 7, 1, 1, 2)

        # 2 - Temp Actual
        self.temp_act_input = QtGui.QLineEdit(self.centralwidget)
        self.temp_act_input.setObjectName(_fromUtf8("temp_act_input"))
        self.gridLayout.addWidget(self.temp_act_input, 7, 3, 1, 1)

        # 3 - Combustion Air Valve Output
        self.ca_vlv_op_input = QtGui.QLineEdit(self.centralwidget)
        self.ca_vlv_op_input.setObjectName(_fromUtf8("ca_vlv_op_input"))
        self.gridLayout.addWidget(self.ca_vlv_op_input, 7, 4, 1, 1)

        # 4 - Left Combustion Air
        self.ca_left_input = QtGui.QLineEdit(self.centralwidget)
        self.ca_left_input.setObjectName(_fromUtf8("ca_left_input"))
        self.gridLayout.addWidget(self.ca_left_input, 11, 1, 1, 2)

        # 5 - Right Combustion Air
        self.ca_right_input = QtGui.QLineEdit(self.centralwidget)
        self.ca_right_input.setObjectName(_fromUtf8("ca_right_input"))
        self.gridLayout.addWidget(self.ca_right_input, 11, 3, 1, 1)

        # 6 - dP Combustion Air
        self.ca_dp_input = QtGui.QLineEdit(self.centralwidget)
        self.ca_dp_input.setObjectName(_fromUtf8("ca_dp_input"))
        self.gridLayout.addWidget(self.ca_dp_input, 11, 4, 1, 1)

        # 7 - Top Atomizing Air
        self.aa_top_input = QtGui.QLineEdit(self.centralwidget)
        self.aa_top_input.setObjectName(_fromUtf8("aa_top_input"))
        self.gridLayout.addWidget(self.aa_top_input, 14, 1, 1, 2)

        # 8 - Bottom Atomizing Air
        self.aa_bot_input = QtGui.QLineEdit(self.centralwidget)
        self.aa_bot_input.setObjectName(_fromUtf8("aa_bot_input"))
        self.gridLayout.addWidget(self.aa_bot_input, 14, 3, 1, 1)

        # 9 - dP Atomizing Air
        self.aa_dp_input = QtGui.QLineEdit(self.centralwidget)
        self.aa_dp_input.setObjectName(_fromUtf8("aa_dp_input"))
        self.gridLayout.addWidget(self.aa_dp_input, 14, 4, 1, 1)

        # 10 - Left Nat Gat
        self.ng_left_input = QtGui.QLineEdit(self.centralwidget)
        self.ng_left_input.setObjectName(_fromUtf8("ng_left_input"))
        self.gridLayout.addWidget(self.ng_left_input, 17, 1, 1, 2)

        # 11 - Right Nat Gas
        self.ng_right_input = QtGui.QLineEdit(self.centralwidget)
        self.ng_right_input.setObjectName(_fromUtf8("ng_right_input"))
        self.gridLayout.addWidget(self.ng_right_input, 17, 3, 1, 1)

        # 12 - dP Nat Gas
        self.ng_dp_input = QtGui.QLineEdit(self.centralwidget)
        self.ng_dp_input.setObjectName(_fromUtf8("ng_dp_input"))
        self.gridLayout.addWidget(self.ng_dp_input, 17, 4, 1, 1)

        # 13 - Bleeder Impulse Pressure
        self.bleed_impulse_pres_input = QtGui.QLineEdit(self.centralwidget)
        self.bleed_impulse_pres_input.setObjectName(_fromUtf8("bleed_impulse_pres_input"))
        self.gridLayout.addWidget(self.bleed_impulse_pres_input, 20, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        # 14 - West Wall Damper Setting
        self.ww_damper_input = QtGui.QLineEdit(self.centralwidget)
        self.ww_damper_input.setObjectName(_fromUtf8("ww_damper_input"))
        self.gridLayout.addWidget(self.ww_damper_input, 20, 3, 1, 1)

        # 15 - Prab Temp
        self.prab_temp_input = QtGui.QLineEdit(self.centralwidget)
        self.prab_temp_input.setObjectName(_fromUtf8("prab_temp_input"))
        self.gridLayout.addWidget(self.prab_temp_input, 20, 4, 1, 1)

        # Build Submit Button
        self.submit_button = QtGui.QPushButton(self.centralwidget)
        self.submit_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.submit_button.setObjectName(_fromUtf8("submit_button"))
        self.gridLayout.addWidget(self.submit_button, 21, 2, 1, 2)
        self.submit_button.clicked.connect(self.submit_click)

        # Run function to label fields
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set Tab Order
        MainWindow.setTabOrder(self.temp_sp_input, self.temp_act_input)
        MainWindow.setTabOrder(self.temp_act_input, self.ca_vlv_op_input)
        MainWindow.setTabOrder(self.ca_vlv_op_input, self.ca_left_input)
        MainWindow.setTabOrder(self.ca_left_input, self.ca_right_input)
        MainWindow.setTabOrder(self.ca_right_input, self.ca_dp_input)
        MainWindow.setTabOrder(self.ca_dp_input, self.aa_top_input)
        MainWindow.setTabOrder(self.aa_top_input, self.aa_bot_input)
        MainWindow.setTabOrder(self.aa_bot_input, self.aa_dp_input)
        MainWindow.setTabOrder(self.aa_dp_input, self.ng_left_input)
        MainWindow.setTabOrder(self.ng_left_input, self.ng_right_input)
        MainWindow.setTabOrder(self.ng_right_input, self.ng_dp_input)
        MainWindow.setTabOrder(self.ng_dp_input, self.bleed_impulse_pres_input)
        MainWindow.setTabOrder(self.bleed_impulse_pres_input, self.ww_damper_input)
        MainWindow.setTabOrder(self.ww_damper_input, self.prab_temp_input)

    def retranslateUi(self, MainWindow):
        """
        Set labels to display on GUI.
        :param MainWindow:
        :return:
        """

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.submit_button.setText(_translate("MainWindow", "Submit", None))
        self.prab_temp_label.setText(_translate("MainWindow", "Prab Temperature", None))
        self.ww_damper_label.setText(_translate("MainWindow", "West Wall Damper Setting", None))
        self.aa_bottom_label.setText(_translate("MainWindow", "Bottom", None))
        self.bleed_impulse_pres_label.setText(_translate("MainWindow", "Bleeder Impulse Pressure", None))
        self.temp_sp_label.setText(_translate("MainWindow", "Temp Setpoint", None))
        self.aa_top_label.setText(_translate("MainWindow", "Top", None))
        self.temp_act_label.setText(_translate("MainWindow", "Temp Actual", None))
        self.ca_vlv_op_label.setText(_translate("MainWindow", "Comb. Air Valve output", None))
        self.aa_dp_label.setText(_translate("MainWindow", "dP", None))
        self.nat_gas_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Natural Gas</span></p></body></html>", None))
        self.ng_right_label.setText(_translate("MainWindow", "Right", None))
        self.app_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Rotary Kiln Log</span></p></body></html>", None))
        self.combustion_air_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Combustion Air</span></p></body></html>", None))
        self.atomizing_air_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Atomizing Air</span></p></body></html>", None))
        self.ca_dp_label.setText(_translate("MainWindow", "dP", None))
        self.ng_left_label.setText(_translate("MainWindow", "Left", None))
        self.ca_left_label.setText(_translate("MainWindow", "Left", None))
        self.ca_right_label.setText(_translate("MainWindow", "Right", None))
        self.ng_dp_label.setText(_translate("MainWindow", "dP", None))

    def submit_click(self):
        log_list = (dt.datetime.now(),
                    self.temp_sp_input.text(),
                    self.temp_act_input.text(),
                    self.ca_left_input.text(),
                    self.ca_right_input.text(),
                    self.ng_left_input.text(),
                    self.ng_right_input.text(),
                    self.aa_top_input.text(),
                    self.aa_bot_input.text(),
                    self.ca_dp_input.text(),
                    self.aa_dp_input.text(),
                    self.ng_dp_input.text(),
                    self.bleed_impulse_pres_input.text(),
                    self.ww_damper_input.text(),
                    self.prab_temp_input.text()
                    )
        send_log(log_list)

def send_log(rkn_log):
    # Parameters
    server = 'ZIRSYSPRO'
    db = 'ZIRTST2'

    # Create the connection
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
    cursor = conn.cursor()
    cursor.execute("""INSERT into KilnLog(LogDateTime, TempSP, TempAct, CALeftPressure, CARightPressure, GasLeftPressure,
                   GasRightPressure, AATopPressure, AABottomPressure, CAdP, AAdP, GasdP, BleederImpulsePressure,
                   WWDamperSetting, PrabTemp) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", rkn_log)
    conn.commit()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


