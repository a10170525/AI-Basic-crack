# cracked by Savage. 
# bitget only
global fibo_Minus0382  # inserted
global fibo_0100  # inserted
global fibo_error  # inserted
global oneway_protect  # inserted
global TP_excute  # inserted
global fibo_0800  # inserted
global stop_autotrade  # inserted
global fibo_0850  # inserted
global Trade_Level  # inserted
global chart_tail  # inserted
global height  # inserted
global fibo_0618  # inserted
global fibo_0200  # inserted
global fibo_error2  # inserted
global is_SL  # inserted
global SL_price  # inserted
global fibo_1000  # inserted
global autotrade_type  # inserted
global fibo_0000  # inserted
global fibo_0150  # inserted
global fibo_0050  # inserted
global is_trading_active  # inserted
global extension  # inserted
global fibo_Minus0500  # inserted
global fibo_value  # inserted
global excute_only_short  # inserted
global fibo_1236  # inserted
global is_task_running  # inserted
global trading_error  # inserted
global fibo_0900  # inserted
global tail_strategy  # inserted
global entry_price  # inserted
global scheduler  # inserted
global fibo_0130  # inserted
global fibo_0236  # inserted
global fibo_0970  # inserted
global excute_risk_management  # inserted
global fibo_0382  # inserted
global fibo_Minus013  # inserted
global order_flag  # inserted
global fibo_Minus0236  # inserted
global SL_price_ex  # inserted
global USDT_bal  # inserted
global diverence_request  # inserted
global fibo_0180  # inserted
global fibo_1130  # inserted
global bitget  # inserted
global TP_price_ex  # inserted
global fibo_0764  # inserted
global div  # inserted
global short_rsi_value  # inserted
global PRO  # inserted
global fibo_1618  # inserted
global autotrade_thread  # inserted
global fibo_0500  # inserted
global fibo_0030  # inserted
global fibo_0820  # inserted
global TP_price  # inserted
global job_running  # inserted
global fibo_0950  # inserted
global fibo_1500  # inserted
global excute_only_long  # inserted
global fibo_0870  # inserted
global fibo_Minus0618  # inserted
global long_rsi_value  # inserted
global width  # inserted
global bitget_symbol  # inserted
global scale_factor  # inserted
global fibo_1382  # inserted
global leave_bus  # inserted
import sys
import os
import signal
import pandas as pd
import pandas_ta as ta
import pytz
from datetime import datetime
import json
import schedule
import time
import numpy as np
from pybitget import Client
from pybitget.utils import random_string
from pybitget.enums import *
from PyQt5.QtWidgets import QTextBrowser, QApplication, QLabel, QSlider, QDialog, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QScrollArea, QMessageBox, QHBoxLayout, QCheckBox, QButtonGroup, QComboBox
from PyQt5.QtGui import QPixmap, QPalette, QColor, QIcon, QCursor, QBrush
from PyQt5.QtCore import QMetaObject, Qt, Q_ARG, QUrl, QTimer
from PyQt5.QtGui import QTextCursor, QFont
import threading
import logging
import ctypes
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import os
import webbrowser
from dotenv import load_dotenv
import requests
from os import environ
import traceback
width = 0
height = 0
logging.getLogger('apscheduler').setLevel(logging.ERROR)

def suppress_qt_warnings(app):
    global width  # inserted
    global height  # inserted
    screen = app.desktop().screenGeometry()
    width, height = (screen.width(), screen.height())
PRO = False
bitget_symbol = 'BTCUSDT_UMCBL'
symbol_name = 'BTCUSDT_UMCBL'
scheduler = None
order_flag = True
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), 'URL.env'))
Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
fibo_0000 = 0
fibo_0130 = 0
fibo_0236 = 0
fibo_0382 = 0
fibo_0500 = 0
fibo_0618 = 0
fibo_0764 = 0
fibo_0870 = 0
fibo_1000 = 0
fibo_Minus013 = 0
fibo_Minus0236 = 0
fibo_Minus0382 = 0
fibo_Minus0500 = 0
fibo_Minus0618 = 0
fibo_1130 = 0
fibo_0030 = 0
fibo_0050 = 0
fibo_0100 = 0
fibo_0150 = 0
fibo_0180 = 0
fibo_0200 = 0
fibo_0970 = 0
fibo_0950 = 0
fibo_0900 = 0
fibo_0850 = 0
fibo_0820 = 0
fibo_0800 = 0
fibo_1130 = 0
fibo_1236 = 0
fibo_1382 = 0
fibo_1500 = 0
fibo_1618 = 0
SAFE_VERSION = 0
fibo_error2 = 0
entry_price = 0
TP_price = 0
SL_price = 0
TP_price_ex = 0
SL_price_ex = 0
TP_excute = True
trading_error = 0
scale_factor = 0.5
fibo_high = 0
low = 0
leave_bus = False
fibo_error = 0
is_task_running = False
long_rsi_value = 50
short_rsi_value = 50
is_trading_active = False
stop_autotrade = False
autotrade_thread = None
USDT_bal = 0
is_SL = False
excute_only_long = False
excute_only_short = False
excute_risk_management = True
elite_strategy = True
chart_tail = 0
tail_strategy = True
autotrade_type = ''
div = False
diverence_request = False
oneway_protect = False
job_running = False
fibo_value = 0
bitget = None
extension = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

def terminate_thread(thread):
    """스레드 강제 종료"""  # inserted
    if not thread.is_alive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError('스레드가 존재하지 않습니다.')
    if res!= 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError('스레드 종료에 실패했습니다.')

def update_gui_log(window, advice):
    QMetaObject.invokeMethod(window.log_output, 'append', Qt.BlockingQueuedConnection, Q_ARG(str, advice))

def log_message(window, message):
    window.log_output.append(message)

class BasicProWindow(QDialog):
    def __init__(self):
        super().__init__()
        icon_path = resource_path('IMG/ExitAntlogo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('탈개미 AI PRO 사용을 권장드립니다')
        self.label = QLabel(self)
        self.pixmap = QPixmap('IMG/BasicPro_img.png')
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.label.setGeometry(0, 0, self.pixmap.width(), self.pixmap.height())
        self.label.setAlignment(Qt.AlignCenter)
        self.label.lower()
        self.label.mousePressEvent = self.handle_click
        self.label.setMouseTracking(True)
        self.label.mouseMoveEvent = self.handle_mouse_move

    def handle_click(self, event):
        if event.button() == Qt.LeftButton and 542 <= event.x() <= 860 and (862 <= event.y() <= 950):
            self.open_url()

    def handle_mouse_move(self, event):
        if 542 <= event.x() <= 860 and 862 <= event.y() <= 950:
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:  # inserted
            self.setCursor(QCursor(Qt.ArrowCursor))

    def open_url(self):
        file_path = 'URLs/url4.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def resizeEvent(self, event):
        window_width = self.width()
        window_height = self.height()
        scaled_pixmap = self.pixmap.scaled(window_width, window_height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.label.setGeometry(0, 0, window_width, window_height)
        super().resizeEvent(event)

class ApiKeyInputWindow(QDialog):
    def __init__(self):
        super().__init__()
        icon_path = resource_path('IMG/ExitAntlogo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle('탈개미 AI Bitget API 인증')
        if PRO:
            background_path = resource_path('IMG/login_img_pro.png')
        else:  # inserted
            background_path = resource_path('IMG/login_img.png')
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap(background_path)
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, self.background_pixmap.width(), self.background_pixmap.height())
        self.background_label.lower()
        self.bitget_input = QLineEdit(self)
        self.bitget_input.setStyleSheet('background-color: black; color: white;')
        self.bitget_input.setEchoMode(QLineEdit.Password)
        self.bitget_input.setGeometry(45, 313, 410, 31)
        self.secret_input = QLineEdit(self)
        self.secret_input.setStyleSheet('background-color: black; color: white;')
        self.secret_input.setEchoMode(QLineEdit.Password)
        self.secret_input.setGeometry(45, 378, 192, 26)
        self.passphrase_input = QLineEdit(self)
        self.passphrase_input.setStyleSheet('background-color: black; color: white;')
        self.passphrase_input.setEchoMode(QLineEdit.Password)
        self.passphrase_input.setGeometry(263, 378, 192, 26)
        self.background_label.mousePressEvent = self.handle_click
        self.background_label.setMouseTracking(True)
        self.background_label.mouseMoveEvent = self.handle_mouse_move

    def handle_click(self, event):
        if event.button() == Qt.LeftButton:
            if 335 <= event.x() <= 475 and 447 <= event.y() <= 475:
                self.open_url()
            else:  # inserted
                if 400 <= event.x() <= 500 and 0 <= event.y() <= 120:
                    self.open_url_telegram()
                else:  # inserted
                    if 25 <= event.x() <= 163 and 447 <= event.y() <= 475:
                        self.open_url_AI_ID()
                    else:  # inserted
                        if 173 <= event.x() <= 325 and 434 <= event.y() <= 485:
                            self.validate_keys()

    def handle_mouse_move(self, event):
        if 335 <= event.x() <= 475 or 400 <= event.y() <= 475 or (447 <= event.y() <= 325) or (434 <= event.y() <= 485) or (<mask_16> <= event.y() <= <Code38 code object log_message at 0x7f50fdd9b610, file autotrade.py>, line 172) or (<mask_18> <= event.y() <= <Code38 code object BasicProWindow at 0x7f50fdd9a8d0, file autotrade.py>, line 177) or (<mask_20> <= event.y() <= <Code38 code object ApiKeyInputWindow at 0x7f50fdd9ab10, file autotrade.py>, line 248) or (<mask_22> <= event.y() <= <Code38 code object MainWindow at 0x7f50fdd9ab50, file autotrade.py>, line 414) or (<mask_24> <= event.y() <= <Code38 code object validate_keys at 0x7f50fddabb90, file autotrade.py>, line 1973) or (<mask_26> <= event.y() <= <Code38 code object get_current_status at 0x7f50fddabc90, file autotrade.py>, line 1993) or (<mask_28> <= event.y() <= <Code38 code object fetch_and_prepare_data at 0x7f50fddabd90, file autotrade.py>, line 2016) or (<mask_30> <= event.y() <= <Code38 code object add_indicators_extension at 0x7f50fddabf90, file autotrade.py>, line 2553) or (<mask_32> <= event.y() <= <Code38 code object analyze_data at 0x7f50fddcc0d0, file autotrade.py>, line 2828) or (<mask_34> <= event.y() <= <Code38 code object open_long at 0x7f50fddcc1d0, file autotrade.py>, line 2885) or (<mask_36> <= event.y() <= <Code38 code object open_long_extension at 0x7f50fddcc2d0, file autotrade.py>, line 3286) or (<mask_38> <= event.y() <= <Code38 code object close_long at 0x7f50fddcc3d0, file autotrade.py>, line 3623) or <mask_40> <= event.y()
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:  # inserted
            self.setCursor(QCursor(Qt.ArrowCursor))

    def validate_keys(self):
        global bitget  # inserted
        api_key = self.bitget_input.text()
        secret_key = self.secret_input.text()
        passphrase = self.passphrase_input.text()
        bitget = self.validate_keys_logic(api_key, secret_key, passphrase)
        if bitget:
            QMessageBox.information(self, '성공', 'API 키가 유효합니다.\n해상도 2560x1600에서 진행하시는 것을 추천드립니다.')
            self.accept()
            bitget_client = bitget
        else:  # inserted
            QMessageBox.warning(self, '오류', 'API 키가 유효하지 않습니다. 다시 시도해주세요.')

    def validate_keys_logic(self, api_key, secret_key, passphrase):
        global bitget  # inserted
        uid = ''
        try:
            Channel_list = ['Titan', 'cfv5', '7hm7', 'Kyungsoo', 'STEADY', 'MinGyu', '2TAN', 'choking', '무닌', '제니님', '2SIN', 'Trader-K', 'Blog partner', '1yzv']
            bitget = Client(api_key, secret_key, passphrase)
            VaildUid = bitget.spot_get_ApiKeyInfo()
            uid = VaildUid['data']['user_id']
            if VaildUid['data']['channel'] in Channel_list:
                QMessageBox.information(self, '인증 성공', f'탈개미대학교 학생 신원확인 완료\nUID:{uid}0님 환영합니다.')
                account_info = bitget.mix_get_accounts(productType='umcbl')
                if account_info['data']:
                    return bitget
                return None
            QMessageBox.critical(self, '인증 실패', '채널 인증 실패. 탈개미대학교 학생이 아닙니다.')
            return
        except Exception as e:
            QMessageBox.critical(self, '오류', f'유효성 검사 중 오류 발생: {str(e)}')
            return

    def open_url(self):
        file_path = 'URLs/url1.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def open_url_telegram(self):
        file_path = 'URLs/url.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def open_url_AI_ID(self):
        file_path = 'URLs/url5.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api_key_window = ApiKeyInputWindow()
        if self.api_key_window.exec_() == QDialog.Accepted:
            self.init_ui()
        else:  # inserted
            os.kill(os.getpid(), signal.SIGTERM)

    def init_ui(self):
        global TP_excute  # inserted
        global scale_factor  # inserted
        screen = QApplication.primaryScreen()
        screen.geometryChanged.connect(self.handle_resolution_change)
        font = QFont('Arial', 16)
        QApplication.instance().setFont(font)
        if PRO:
            self.setWindowTitle('탈개미 트레이딩 PRO')
        else:  # inserted
            self.setWindowTitle('탈개미 트레이딩 Lite')
        self.setGeometry(100, 100, 1600, 1350)
        TP_excute = True
        icon_path = resource_path('IMG/ExitAntlogo.png')
        self.setWindowIcon(QIcon(icon_path))
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.main_widget = QWidget()
        self.scroll_area.setWidget(self.main_widget)
        self.setCentralWidget(self.scroll_area)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.right_layout = QHBoxLayout()
        self.target_layout = QHBoxLayout()
        if PRO:
            background_path = resource_path('IMG/ExitAnt_foreground2.png')
        else:  # inserted
            background_path = resource_path('IMG/ExitAnt_foreground.png')
        window_width = self.width()
        window_height = self.height()
        self.background_label = QLabel(self.main_widget)
        self.background_label.setGeometry(0, 0, window_width, window_height)
        background_pixmap = QPixmap(background_path)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background_pixmap))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        transparent_palette = QPalette()
        transparent_palette.setColor(QPalette.Window, Qt.transparent)
        label_style = 'color: white;'
        self.stop_button = QPushButton('자동매매 중지', self.main_widget)
        self.stop_button.setFixedSize(300, 60)
        self.stop_button.clicked.connect(self.stop_autotrade)
        self.trade_size_label = QLabel('포지션 진입 규모 / ※ 수량 단위 : USDT', self.main_widget)
        self.trade_size_label.setStyleSheet(label_style)
        self.trade_size_input = QLineEdit(self.main_widget)
        self.explanation_button = QPushButton('Bitget 시드 입금', self.main_widget)
        self.explanation_button.setFixedSize(200, 30)
        self.explanation_button.clicked.connect(self.connect_explanation)
        self.trade_size_input.setFixedSize(400, 40)
        self.trade_size_input.setStyleSheet('background-color: black; color: white;')
        self.leverage_size_label = QLabel('레버리지 배율 설정 / ※ 숫자만 입력', self.main_widget)
        self.leverage_size_label.setStyleSheet(label_style)
        self.leverage_size_input = QLineEdit(self.main_widget)
        self.leverage_size_input.setStyleSheet('background-color: black; color: white;')
        self.leverage_size_input.setFixedSize(400, 40)
        if PRO:
            self.program_help_button1 = QPushButton('AI PRO 설명서', self.main_widget)
            self.program_help_button1.setFixedSize(300, 60)
            self.program_help_button1.clicked.connect(self.open_url3)
            button_style_pro = 'background-color: gold; color: black;font-weight: bold;'
            self.program_help_button1.setStyleSheet(button_style_pro)
        else:  # inserted
            self.program_help_button1 = QPushButton('AI Basic 설명서', self.main_widget)
            self.program_help_button1.setFixedSize(300, 60)
            self.program_help_button1.clicked.connect(self.open_url3)
            button_style_pro = 'background-color: gold; color: black;font-weight: bold;'
            self.program_help_button1.setStyleSheet(button_style_pro)
        self.program_help_button3 = QPushButton('AI 데이터 공유방', self.main_widget)
        self.program_help_button3.setFixedSize(300, 60)
        self.program_help_button3.clicked.connect(self.open_url)
        button_style_pro2 = 'background-color: skyblue; color: black;font-weight: bold;'
        self.program_help_button3.setStyleSheet(button_style_pro2)
        self.program_help_button = QPushButton('추세확장/전환 전략 변경', self.main_widget)
        self.program_help_button.setFixedSize(400, 60)
        self.program_help_button.clicked.connect(self.toggle_extension_checkbox)
        self.program_help_button2 = QPushButton('오류 해결 가이드', self.main_widget)
        self.program_help_button2.setFixedSize(300, 60)
        self.program_help_button2.clicked.connect(self.open_url2)
        self.right_layout.addWidget(self.program_help_button, alignment=Qt.AlignCenter)
        self.right_layout.addWidget(self.program_help_button1, alignment=Qt.AlignCenter)
        self.right_layout.addWidget(self.program_help_button3, alignment=Qt.AlignCenter)
        self.right_layout.addWidget(self.program_help_button2, alignment=Qt.AlignCenter)
        self.slide_layout = QVBoxLayout()
        self.trade_error_label = QLabel(f'피보나치 포지션 오차 : {trading_error}0')
        self.trade_error_label.setStyleSheet('color: white;')
        self.slide_layout.addWidget(self.trade_error_label)
        self.trading_error_slider = QSlider(Qt.Horizontal)
        self.trading_error_slider.setMinimum((-20))
        self.trading_error_slider.setMaximum(20)
        self.trading_error_slider.setValue(trading_error)
        self.trading_error_slider.setTickInterval(1)
        self.trading_error_slider.setFixedWidth(300)
        self.trading_error_slider.valueChanged.connect(self.update_trading_error)
        self.slide_layout.addWidget(self.trading_error_slider)
        self.long_checkbox = QCheckBox('롱 포지션만 진입', self.main_widget)
        self.long_checkbox.setChecked(False)
        self.long_checkbox.setStyleSheet('\n            color: white;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.long_checkbox.stateChanged.connect(self.toggle_long_checkbox)
        self.short_checkbox = QCheckBox('숏 포지션만 진입', self.main_widget)
        self.short_checkbox.setChecked(False)
        self.short_checkbox.setStyleSheet('\n            color: white;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.short_checkbox.stateChanged.connect(self.toggle_short_checkbox)
        self.diverence_checkbox = QCheckBox('PRO 다이버전스 전략 적용', self.main_widget)
        self.diverence_checkbox.setChecked(False)
        self.diverence_checkbox.setStyleSheet('\n            color: yellow;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.diverence_checkbox.stateChanged.connect(self.toggle_diverence_checkbox)
        self.bollinger_checkbox = QCheckBox('PRO 원웨이 방어 전략 적용', self.main_widget)
        self.bollinger_checkbox.setChecked(False)
        self.bollinger_checkbox.setStyleSheet('\n            color: yellow;\n            QCheckBox::indicator {\n                width: 40px;\n                height: 40px;\n            }\n        ')
        self.bollinger_checkbox.stateChanged.connect(self.toggle_bollinger_checkbox)
        self.tail_label = QLabel('윗/밑 꼬리 단계', self)
        self.tail_label.setStyleSheet('color: yellow;')
        self.tail_slider = QSlider(Qt.Horizontal)
        self.tail_slider.setMinimum(0)
        self.tail_slider.setMaximum(5)
        self.tail_slider.setValue(chart_tail)
        self.tail_slider.setTickInterval(1)
        self.tail_slider.setFixedWidth(300)
        self.tail_slider.valueChanged.connect(self.update_chart_tail)
        self.slide_layout.addWidget(self.tail_label)
        self.slide_layout.addWidget(self.tail_slider)
        self.slide_layout.setSpacing(0)
        self.slide_layout.setContentsMargins(50, 0, 0, 0)
        button_text = ['자동매매 시작']
        buttonA = QPushButton(button_text[0], self.main_widget)
        buttonA.setFixedSize(300, 60)
        buttonA.clicked.connect(self.start_autotrade)
        button_style_a = 'background-color: skyblue; color: black;'
        button_style_c = 'background-color: gray; color: white; font-size: 20px;'
        button_style = 'background-color: gray; color: white;'
        button_style4 = 'background-color: orange; color: black; font-weight: bold;'
        button_style3 = 'background-color: skyblue; color: black; font-weight: bold;'
        self.stop_button.setStyleSheet(button_style)
        self.explanation_button.setStyleSheet(button_style_c)
        bttn_image_path = 'IMG/start_bttn.png'
        stopbttn_image_path = 'IMG/stop_bttn.png'
        buttonA.setStyleSheet(button_style3)
        self.stop_button.setStyleSheet(button_style)
        button_style_2 = 'background-color: pink; color: black; font-size: 30px; font-weight: bold;'
        self.program_help_button.setStyleSheet(button_style_2)
        self.program_help_button2.setStyleSheet(button_style4)
        self.check_box_layout = QVBoxLayout()
        self.check_box_layout.addWidget(self.long_checkbox)
        self.check_box_layout.addWidget(self.short_checkbox)
        self.check_box_layout.addWidget(self.diverence_checkbox)
        self.check_box_layout.addWidget(self.bollinger_checkbox)
        self.check_box_layout.setContentsMargins(50, 0, 0, 0)
        self.slide_checkbox_layout = QHBoxLayout()
        self.slide_checkbox_layout.addLayout(self.slide_layout)
        self.slide_checkbox_layout.addLayout(self.check_box_layout)
        self.bttn_layout = QVBoxLayout()
        self.bttn_layout.addWidget(buttonA)
        self.bttn_layout.addWidget(self.stop_button)
        self.bttn_layout.setContentsMargins(50, 30, 100, 0)
        self.bttn_layout.setSpacing(0)
        if not extension:
            self.combobox_layout = QVBoxLayout()
            self.label1 = QLabel('진입 가격', self)
            self.label1.setStyleSheet('color: white;')
            self.combobox1 = QComboBox(self)
            self.combobox1.addItems(['피보나치 0.13(위험)', '피보나치 0.236(추천)'])
            self.combobox1.currentIndexChanged.connect(self.update_fibo)
            self.label2 = QLabel('익절 가격', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['피보나치 0.5', '피보나치 0.618'])
            self.combobox2.currentIndexChanged.connect(self.update_TP)
            self.label3 = QLabel('손절 가격', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['피보나치 0', '피보나치 -0.13'])
            self.combobox3.currentIndexChanged.connect(self.update_SL)
        else:  # inserted
            self.label2 = QLabel('추세 확장 익절 가격', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['피보나치 1.13', '피보나치 1.236(추천)', '피보나치 1.5'])
            self.combobox2.currentIndexChanged.connect(self.update_TP_extension)
            self.combobox_layout.addWidget(self.label2)
            self.combobox_layout.addWidget(self.combobox2)
            self.label3 = QLabel('추세 확장 손절 가격', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['피보나치 0.618', '피보나치 0.5', '피보나치 0.382'])
            self.combobox3.currentIndexChanged.connect(self.update_SL_extension)
            self.combobox_layout.addWidget(self.label3)
            self.combobox_layout.addWidget(self.combobox3)
        self.combobox_layout.addWidget(self.label1)
        self.combobox_layout.addWidget(self.combobox1)
        self.combobox_layout.addWidget(self.label2)
        self.combobox_layout.addWidget(self.combobox2)
        self.combobox_layout.addWidget(self.label3)
        self.combobox_layout.addWidget(self.combobox3)
        self.combobox_layout.setContentsMargins(50, 0, 0, 0)
        self.combobox_layout.setSpacing(0)
        self.USDT_layout = QHBoxLayout()
        self.api_layout = QVBoxLayout()
        self.USDT_layout.addWidget(self.trade_size_label)
        self.USDT_layout.addWidget(self.explanation_button)
        self.api_layout.addLayout(self.USDT_layout)
        self.api_layout.addWidget(self.trade_size_input)
        self.api_layout.addWidget(self.leverage_size_label)
        self.api_layout.addWidget(self.leverage_size_input)
        self.image_layout = QVBoxLayout()
        self.low_bttn_layout = QHBoxLayout()
        self.stratgy_label = QLabel('↓↓ 꼬리전략 적용 예시 : ', self.main_widget)
        self.stratgy_label2 = QLabel('↑↑ 매매타입 적용 예시', self.main_widget)
        self.stratgy_label.setStyleSheet('color: white;')
        self.stratgy_label2.setStyleSheet('color: white;')
        if not PRO:
            self.ANT_button = QPushButton('탈개미 PRO 다운 방법', self.main_widget)
            self.ANT_button.setStyleSheet('background-color: red; color: white;')
            self.ANT_button.clicked.connect(self.connect_pro)
            self.glo_button = QPushButton('해외 거래소가 처음이라면?', self.main_widget)
            self.glo_button.setStyleSheet('background-color: black; color: white;')
            self.glo_button.clicked.connect(self.connect_glo)
        else:  # inserted
            self.ANT_button = QPushButton('황금비율 알고리즘 공부하기', self.main_widget)
            self.ANT_button.setStyleSheet('background-color: red; color: white;')
            self.ANT_button.clicked.connect(self.connect_pro2)
            self.glo_button = QPushButton('해외 거래소가 처음이라면?', self.main_widget)
            self.glo_button.setStyleSheet('background-color: black; color: white;')
            self.glo_button.clicked.connect(self.connect_glo)
        self.ANT_button.setFixedSize(500, 60)
        self.glo_button.setFixedSize(500, 60)
        self.low_bttn_layout.addWidget(self.ANT_button)
        self.low_bttn_layout.addWidget(self.glo_button)
        self.tail_image_label = QLabel(self)
        self.tail_image_label.setFixedSize(1000, 1000)
        self.tail_image_label.setStyleSheet('border: 2px solid white; color: white;')
        tail_image_path = 'IMG/Tale/level1.png'
        self.tail_image_pixmap = QPixmap(tail_image_path)
        if not self.tail_image_pixmap.isNull():
            self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(self.tail_image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.tail_image_label.resize(self.tail_image_pixmap.size())
        self.update_chart_tail(chart_tail)
        self.image_label = QLabel(self)
        self.image_label.setFixedSize(1000, 1000)
        self.image_label.setStyleSheet('border: 2px solid white; color: white;')
        if extension:
            image_path = 'IMG/extension_trade_type.png'
        else:  # inserted
            image_path = 'IMG/trade_type.png'
        self.image_pixmap = QPixmap(image_path)
        if not self.image_pixmap.isNull():
            self.image_label.setPixmap(self.image_pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.resize(self.image_pixmap.size())
        self.update_image()
        self.image_label.setMouseTracking(True)
        self.tail_image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.handle_mouse_move
        self.image_label.mousePressEvent = self.handle_mouse_click
        self.tail_image_label.mouseMoveEvent = self.handle_mouse_move
        self.tail_image_label.mousePressEvent = self.handle_mouse_click
        self.tail_image_label.setFixedSize(600, 500)
        self.image_label.setFixedSize(600, 500)
        self.image_layout.addWidget(self.stratgy_label)
        self.image_layout.addWidget(self.tail_image_label)
        self.image_layout.addWidget(self.image_label)
        self.image_layout.addWidget(self.stratgy_label2)
        self.image_layout.addLayout(self.low_bttn_layout)
        self.image_layout.setContentsMargins(0, 0, 0, 0)
        self.option_layout = QHBoxLayout()
        self.option_layout.addLayout(self.slide_checkbox_layout)
        self.option_layout.addLayout(self.combobox_layout)
        self.option_layout.setSpacing(0)
        self.log_layout = QVBoxLayout()
        self.log_label = QLabel('로그 출력: ', self.main_widget)
        self.log_label.setStyleSheet('color: white;')
        self.log_output = QTextEdit(self.main_widget)
        self.log_output.setReadOnly(True)
        if PRO:
            img = 'IMG/ExitAnt_logBack2.png'
        else:  # inserted
            img = 'IMG/ExitAnt_logBack.png'
        if img == None:
            img = '탈개미 AI 모델 1 최종본/IMG/ExitAnt_logBack.png'
        self.log_output.setStyleSheet(f'\n            background-image: url({img}0{');\n            background-repeat: repeat-y;\n            color: yellow;\n            font-size: 14pt;\n        ')
        self.log_layout.addWidget(self.log_label)
        self.log_layout.addWidget(self.log_output)
        self.low_layout = QHBoxLayout()
        self.low_layout.addLayout(self.log_layout)
        self.low_layout.addLayout(self.image_layout)
        self.clear_log_button = QPushButton('로그 초기화', self.main_widget)
        self.clear_log_button.setFixedSize(300, 60)
        self.clear_log_button.clicked.connect(self.clear_log_output)
        self.clear_log_button.setStyleSheet(button_style)
        self.warning_label = QLabel('(주의)자동매매로 인한 손실은 탈개미 측이 아닌 프로그램을 실행한 개인의 책임임을 알려드립니다.', self.main_widget)
        self.warning_label.setStyleSheet('color: white;')
        self.log_layout.addWidget(self.clear_log_button)
        self.log_layout.addWidget(self.warning_label)
        self.target_layout.addLayout(self.api_layout)
        self.target_layout.addLayout(self.option_layout)
        self.target_layout.addLayout(self.bttn_layout)
        self.target_layout.setContentsMargins(10, 0, 0, 0)
        self.main_layout.addLayout(self.right_layout)
        self.main_layout.addLayout(self.target_layout)
        self.main_layout.addLayout(self.low_layout)
        sys.stdout = self.RedirectText(self.log_output, self.clear_log_output)
        if width == 1920 and height == 1080:
            scale_factor = 0.85
            self.resize(int(self.width() * scale_factor), int(self.height() * scale_factor))
            for widget in self.findChildren(QWidget):
                if isinstance(widget, QComboBox):
                    continue
                original_size = widget.size()
                widget.resize(int(original_size.width() * scale_factor), int(original_size.height() * scale_factor))
                original_font = widget.font()
                original_font.setPointSize(int(original_font.pointSize() * scale_factor))
                widget.setFont(original_font)
            for layout in self.findChildren(QHBoxLayout):
                layout.setSpacing(int(layout.spacing() * scale_factor))
                margins = layout.contentsMargins()
                layout.setContentsMargins(int(margins.left() * 1), int(margins.top() * scale_factor), int(margins.right() * 1), int(margins.bottom() * scale_factor))
            for layout in self.findChildren(QVBoxLayout):
                layout.setSpacing(int(layout.spacing() * scale_factor))
                margins = layout.contentsMargins()
                layout.setContentsMargins(int(margins.left()), int(margins.top() * scale_factor), int(margins.right()), int(margins.bottom() * scale_factor))
            self.log_output.setStyleSheet(f'\n            background-image: url({img}0{');\n            background-repeat: repeat-y;\n            color: yellow;\n            font-size: 14pt;\n        ')

    def toggle_extension_checkbox(self, state):
        global extension  # inserted
        if is_trading_active:
            QMessageBox.warning(self, '경고', '현재 실행중인 자동매매를 중지한 뒤 변경해주세요')
            return
        extension = not extension
        self.setup_comboboxes()
        self.update_visibility(extension)

    def update_visibility(self, ex):
        """\n        extension 변수에 따라 특정 체크박스와 라벨의 가시성을 업데이트합니다.\n        """  # inserted
        self.diverence_checkbox.setVisible(not ex)
        self.bollinger_checkbox.setVisible(not ex)
        self.tail_label.setVisible(not ex)
        self.tail_slider.setVisible(not ex)

    def setup_comboboxes(self):
        if extension:
            if extension:
                tail_image_path = 'IMG/Tale/level1.png'
                self.tail_image_pixmap = QPixmap(tail_image_path)
                img = 'IMG/extension.png'
                self.log_output.setStyleSheet(f'\n                    background-image: url({img}0{');\n                    background-repeat: repeat-y;\n                    color: yellow;\n                    font-size: 14pt;\n                ')
                image_path = 'IMG/extension_trade_type.png'
                self.image_pixmap = QPixmap(image_path)
                if not self.image_pixmap.isNull():
                    self.image_label.setPixmap(self.image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    self.image_label.resize(self.tail_image_pixmap.size())
                tail_image_path = 'IMG/Tale/noTale.png'
                self.tail_image_pixmap = QPixmap(tail_image_path)
                if not self.tail_image_pixmap.isNull():
                    self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    self.tail_image_label.resize(self.tail_image_pixmap.size())
        else:  # inserted
            self.update_image()
            self.update_chart_tail(chart_tail)
            if PRO:
                img = 'IMG/ExitAnt_logBack2.png'
            else:  # inserted
                img = 'IMG/ExitAnt_logBack.png'
            if img == None:
                img = '탈개미 AI 모델 1 최종본/IMG/ExitAnt_logBack.png'
            self.log_output.setStyleSheet(f'\n                background-image: url({img}0{');\n                background-repeat: repeat-y;\n                color: yellow;\n                font-size: 14pt;\n            ')
        for i in reversed(range(self.combobox_layout.count())):
            widget = self.combobox_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        if not extension:
            self.label1 = QLabel('진입 가격', self)
            self.label1.setStyleSheet('color: white;')
            self.combobox1 = QComboBox(self)
            self.combobox1.addItems(['피보나치 0.13(위험)', '피보나치 0.236(추천)'])
            self.combobox1.currentIndexChanged.connect(self.update_fibo)
            self.combobox_layout.addWidget(self.label1)
            self.combobox_layout.addWidget(self.combobox1)
            self.label2 = QLabel('익절 가격', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['피보나치 0.5', '피보나치 0.618'])
            self.combobox2.currentIndexChanged.connect(self.update_TP)
            self.combobox_layout.addWidget(self.label2)
            self.combobox_layout.addWidget(self.combobox2)
            self.label3 = QLabel('손절 가격', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['피보나치 0', '피보나치 -0.13'])
            self.combobox3.currentIndexChanged.connect(self.update_SL)
            self.combobox_layout.addWidget(self.label3)
            self.combobox_layout.addWidget(self.combobox3)
        else:  # inserted
            self.label2 = QLabel('추세 확장 익절 가격', self)
            self.label2.setStyleSheet('color: white;')
            self.combobox2 = QComboBox(self)
            self.combobox2.addItems(['피보나치 1.13', '피보나치 1.236(추천)', '피보나치 1.5'])
            self.combobox2.currentIndexChanged.connect(self.update_TP_extension)
            self.combobox_layout.addWidget(self.label2)
            self.combobox_layout.addWidget(self.combobox2)
            self.label3 = QLabel('추세 확장 손절 가격', self)
            self.label3.setStyleSheet('color: white;')
            self.combobox3 = QComboBox(self)
            self.combobox3.addItems(['피보나치 0.618', '피보나치 0.5', '피보나치 0.382'])
            self.combobox3.currentIndexChanged.connect(self.update_SL_extension)
            self.combobox_layout.addWidget(self.label3)
            self.combobox_layout.addWidget(self.combobox3)

    def resizeEvent(self, event):
        window_width = self.width()
        window_height = self.height()
        scaled_pixmap = self.pixmap.scaled(window_width, window_height, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)
        self.label.setGeometry(0, 0, window_width, window_height)
        super().resizeEvent(event)

    def connect_pro(self):
        if not PRO:
            self.BasicPro_window = BasicProWindow()
            self.BasicPro_window.exec_()

    def connect_pro2(self):
        file_path = 'URLs/url4.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def connect_glo(self):
        file_path = 'URLs/url7.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def clear_log_output(self):
        self.log_output.clear()

    def handle_resolution_change(self):
        screen = QApplication.primaryScreen()
        screen_size = screen.size()
        screen_width, screen_height = (screen_size.width(), screen_size.height())
        self.resize(int(screen_width * 0.8), int(screen_height * 0.8))
        font_size = int(screen_height * 0.03)
        self.label.setFont(QFont('Arial', font_size))

    def update_image(self):
        global Trade_Level  # inserted
        global autotrade_type  # inserted
        if extension:
            image_path = 'IMG/trade_blur.png'
        else:  # inserted
            if entry_price == 1 and TP_price == 0 and (SL_price == 0):
                if PRO:
                    image_path = 'IMG/PRO/tradeA.png'
                else:  # inserted
                    image_path = 'IMG/trade_blur.png'
                Trade_Level = {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
                autotrade_type = 'A'
            else:  # inserted
                if entry_price == 1 and TP_price == 1 and (SL_price == 0):
                    if PRO:
                        image_path = 'IMG/PRO/tradeB.png'
                    else:  # inserted
                        image_path = 'IMG/trade_blur.png'
                    Trade_Level = {'A': 0, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
                    autotrade_type = 'B'
                else:  # inserted
                    if entry_price == 1 and TP_price == 0 and (SL_price == 1):
                        if PRO:
                            image_path = 'IMG/PRO/tradeC.png'
                        else:  # inserted
                            image_path = 'IMG/trade_blur.png'
                        Trade_Level = {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
                        autotrade_type = 'C'
                    else:  # inserted
                        if entry_price == 1 and TP_price == 1 and (SL_price == 1):
                            if PRO:
                                image_path = 'IMG/PRO/tradeD.png'
                            else:  # inserted
                                image_path = 'IMG/trade_blur.png'
                            Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0}
                            autotrade_type = 'D'
                        else:  # inserted
                            if entry_price == 0 and TP_price == 0 and (SL_price == 0):
                                if PRO:
                                    image_path = 'IMG/PRO/tradeE.png'
                                else:  # inserted
                                    image_path = 'IMG/trade_blur.png'
                                Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 0}
                                autotrade_type = 'E'
                            else:  # inserted
                                if entry_price == 0 and TP_price == 1 and (SL_price == 0):
                                    if PRO:
                                        image_path = 'IMG/PRO/tradeF.png'
                                    else:  # inserted
                                        image_path = 'IMG/trade_blur.png'
                                    Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 1, 'G': 0, 'H': 0}
                                    autotrade_type = 'F'
                                else:  # inserted
                                    if entry_price == 0 and TP_price == 0 and (SL_price == 1):
                                        if PRO:
                                            image_path = 'IMG/PRO/tradeG.png'
                                        else:  # inserted
                                            image_path = 'IMG/trade_blur.png'
                                        Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 0}
                                        autotrade_type = 'G'
                                    else:  # inserted
                                        if entry_price == 0 and TP_price == 1 and (SL_price == 1):
                                            if PRO:
                                                image_path = 'IMG/PRO/tradeH.png'
                                            else:  # inserted
                                                image_path = 'IMG/trade_blur.png'
                                            Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1}
                                            autotrade_type = 'H'
                                        else:  # inserted
                                            return None
        self.update_state(autotrade_type)
        self.image_pixmap = QPixmap(image_path)
        if not self.image_pixmap.isNull():
            self.image_label.setPixmap(self.image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.resize(self.tail_image_pixmap.size())

    def update_image_extension(self):
        global Trade_Level  # inserted
        global autotrade_type  # inserted
        if TP_price_ex == 0 and SL_price == 0:
            image_path = 'IMG/extension_trade_type.png'
            Trade_Level = {'A': 1, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
            autotrade_type = 'A'
        else:  # inserted
            if TP_price == 0 and SL_price == 1:
                image_path = 'IMG/extension_trade_type.png'
                Trade_Level = {'A': 0, 'B': 1, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                autotrade_type = 'B'
            else:  # inserted
                if TP_price == 0 and SL_price == 2:
                    image_path = 'IMG/extension_trade_type.png'
                    Trade_Level = {'A': 0, 'B': 0, 'C': 1, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                    autotrade_type = 'C'
                else:  # inserted
                    if TP_price == 1 and SL_price == 0:
                        image_path = 'IMG/extension_trade_type.png'
                        Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                        autotrade_type = 'D'
                    else:  # inserted
                        if TP_price == 1 and SL_price == 1:
                            image_path = 'IMG/extension_trade_type.png'
                            Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 1, 'F': 0, 'G': 0, 'H': 0, 'I': 0}
                            autotrade_type = 'E'
                        else:  # inserted
                            if TP_price == 1 and SL_price == 2:
                                image_path = 'IMG/extension_trade_type.png'
                                Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 1, 'G': 0, 'H': 0, 'I': 0}
                                autotrade_type = 'F'
                            else:  # inserted
                                if TP_price == 2 and SL_price == 0:
                                    image_path = 'IMG/extension_trade_type.png'
                                    Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 1, 'H': 0, 'I': 0}
                                    autotrade_type = 'G'
                                else:  # inserted
                                    if TP_price == 2 and SL_price == 1:
                                        image_path = 'IMG/extension_trade_type.png'
                                        Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 1, 'I': 0}
                                        autotrade_type = 'H'
                                    else:  # inserted
                                        if TP_price == 2 and SL_price == 2:
                                            image_path = 'IMG/extension_trade_type.png'
                                            Trade_Level = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 1}
                                            autotrade_type = 'I'
                                        else:  # inserted
                                            return None
        self.update_state(autotrade_type)
        self.image_pixmap = QPixmap(image_path)
        if not self.image_pixmap.isNull():
            self.image_label.setPixmap(self.image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image_label.resize(self.tail_image_pixmap.size())

    def handle_mouse_move(self, event):
        if not PRO:
            if 0 <= event.x() <= self.image_label.width() and 0 <= event.y() <= self.image_label.height():
                self.setCursor(QCursor(Qt.PointingHandCursor))
            else:  # inserted
                self.setCursor(QCursor(Qt.ArrowCursor))

    def handle_mouse_click(self, event):
        if not PRO and event.button() == Qt.LeftButton:
            self.BasicPro_window = BasicProWindow()
            self.BasicPro_window.exec_()

    def update_fibo(self, index):
        global entry_price  # inserted
        if index == 0:
            entry_price = 0
        else:  # inserted
            entry_price = 1
        self.update_image()

    def update_TP(self, index):
        global TP_price  # inserted
        if index == 0:
            TP_price = 0
        else:  # inserted
            TP_price = 1
        self.update_image()

    def update_SL(self, index):
        global SL_price  # inserted
        if index == 0:
            SL_price = 0
        else:  # inserted
            SL_price = 1
        self.update_image()

    def update_TP_extension(self, index):
        global TP_price_ex  # inserted
        if index == 0:
            TP_price_ex = 0
        else:  # inserted
            if index == 1:
                TP_price_ex = 1
            else:  # inserted
                TP_price_ex = 2
        self.update_image_extension()

    def update_SL_extension(self, index):
        global SL_price_ex  # inserted
        if index == 0:
            SL_price_ex = 0
        else:  # inserted
            if index == 1:
                SL_price_ex = 1
            else:  # inserted
                SL_price_ex = 2
        self.update_image_extension()

    def update_bitget_symbol(self):
        global bitget_symbol  # inserted
        selected_symbol = self.combo_box.currentText()
        bitget_symbol = symbol_df[symbol_df['symbolDisplayName'] == selected_symbol]['symbol'].values[0]
        self.select_symbol_label.setText(f'선택된 심볼: {selected_symbol} (Symbol: {bitget_symbol})')

    def toggle_long_checkbox(self, state):
        global excute_only_long  # inserted
        if state == Qt.Checked:
            excute_only_long = True
        else:  # inserted
            excute_only_long = False

    def toggle_short_checkbox(self, state):
        global excute_only_short  # inserted
        if state == Qt.Checked:
            excute_only_short = True
        else:  # inserted
            excute_only_short = False

    def diverence_reset_prevent_toggle(self):
        self.diverence_prevent_toggle = False

    def toggle_diverence_checkbox(self, state):
        global diverence_request  # inserted
        if state == Qt.Checked:
            if PRO:
                diverence_request = True
            else:  # inserted
                self.BasicPro_window = BasicProWindow()
                self.BasicPro_window.exec_()
                diverence_request = False
                self.diverence_prevent_toggle = True
                self.diverence_checkbox.setChecked(False)
                self.diverence_checkbox.setEnabled(False)
                QTimer.singleShot(1000, self.diverence_reset_prevent_toggle)
        else:  # inserted
            diverence_request = False
            self.diverence_checkbox.setChecked(False)

    def bollinger_reset_prevent_toggle(self):
        self.bollinger_prevent_toggle = False

    def toggle_bollinger_checkbox(self, state):
        global oneway_protect  # inserted
        if state == Qt.Checked:
            if PRO:
                oneway_protect = True
            else:  # inserted
                self.BasicPro_window = BasicProWindow()
                self.BasicPro_window.exec_()
                oneway_protect = False
                self.bollinger_prevent_toggle = True
                self.bollinger_checkbox.setChecked(False)
                self.bollinger_checkbox.setEnabled(False)
                QTimer.singleShot(1000, self.bollinger_reset_prevent_toggle)
        else:  # inserted
            oneway_protect = False
            self.bollinger_checkbox.setChecked(False)

    def toggle_lowtail_checkbox(self, state):
        global tail_strategy  # inserted
        if state == Qt.Checked:
            tail_strategy = True
        else:  # inserted
            tail_strategy = False

    def update_trading_error(self, value):
        global trading_error  # inserted
        trading_error = value
        self.trade_error_label.setText(f'피보나치 포지션 오차 : {value}0')

    def update_long_rsi(self, value):
        """롱 RSI 슬라이더 값이 변경될 때 호출"""  # inserted
        global long_rsi_value  # inserted
        long_rsi_value = value
        self.long_rsi_label.setText(f'롱 RSI: {value}0{' 이하 포지션 진입')

    def update_short_rsi(self, value):
        """숏 RSI 슬라이더 값이 변경될 때 호출"""  # inserted
        global short_rsi_value  # inserted
        short_rsi_value = value
        self.short_rsi_label.setText(f'숏 RSI: {value}0{' 이상 포지션 진입')

    def update_chart_tail(self, value):
        global chart_tail  # inserted
        global fibo_value  # inserted
        if extension:
            tail_image_path = 'IMG/Tale/level1.png'
        if PRO:
            chart_tail = value
            if chart_tail == 0:
                tail_image_path = 'IMG/Tale/level1.png'
                fibo_value = 0
            else:  # inserted
                if chart_tail == 1:
                    tail_image_path = 'IMG/Tale/level2.png'
                    fibo_value = 0.03
                else:  # inserted
                    if chart_tail == 2:
                        tail_image_path = 'IMG/Tale/level3.png'
                        fibo_value = 0.05
                    else:  # inserted
                        if chart_tail == 3:
                            tail_image_path = 'IMG/Tale/level4.png'
                            fibo_value = 0.1
                        else:  # inserted
                            if chart_tail == 4:
                                tail_image_path = 'IMG/Tale/level5.png'
                                fibo_value = 0.13
                            else:  # inserted
                                if chart_tail == 5:
                                    tail_image_path = 'IMG/Tale/level6.png'
                                    fibo_value = 0.15
                                else:  # inserted
                                    if chart_tail == 6:
                                        tail_image_path = 'IMG/Tale/level7.png'
                                        fibo_value = 0.18
                                    else:  # inserted
                                        if chart_tail == 7:
                                            tail_image_path = 'IMG/Tale/level8.png'
                                            fibo_value = 0.2
                                        else:  # inserted
                                            if chart_tail == 8:
                                                tail_image_path = 'IMG/Tale/level9.png'
                                                fibo_value = 0.236
                                            else:  # inserted
                                                fibo_value = 0.236
            self.tail_label.setText(f'PRO 윗/밑꼬리 단계(피보) : {value} ({fibo_value})')
            self.tail_label
        else:  # inserted
            chart_tail = value
            if chart_tail == 0:
                tail_image_path = 'IMG/basictale/basiclevel1.png'
                fibo_value = 0
            else:  # inserted
                if chart_tail == 1:
                    tail_image_path = 'IMG/basictale/basiclevel2.png'
                    fibo_value = 0.03
                else:  # inserted
                    if chart_tail == 2:
                        tail_image_path = 'IMG/basictale/basiclevel3.png'
                        fibo_value = 0.05
                    else:  # inserted
                        if chart_tail == 3:
                            tail_image_path = 'IMG/basictale/basiclevel4.png'
                            fibo_value = 0.1
                        else:  # inserted
                            if chart_tail == 4:
                                tail_image_path = 'IMG/basictale/basiclevel5.png'
                                fibo_value = 0.13
                            else:  # inserted
                                if chart_tail == 5:
                                    tail_image_path = 'IMG/basictale/basiclevel6.png'
                                    fibo_value = 0.15
                                else:  # inserted
                                    if chart_tail == 6:
                                        tail_image_path = 'IMG/basictale/basiclevel7.png'
                                        fibo_value = 0.18
                                    else:  # inserted
                                        if chart_tail == 7:
                                            tail_image_path = 'IMG/basictale/basiclevel8.png'
                                            fibo_value = 0.2
                                        else:  # inserted
                                            if chart_tail == 8:
                                                tail_image_path = 'IMG/basictale/basiclevel9.png'
                                                fibo_value = 0.236
                                            else:  # inserted
                                                fibo_value = 0.236
            chart_tail = 0
            fibo_value = 0
            self.tail_label.setText('PRO 윗/밑꼬리 단계(피보) : X')
            self.tail_label.setStyleSheet('color: yellow;')
        self.tail_image_pixmap = QPixmap(tail_image_path)
        if not self.tail_image_pixmap.isNull():
            self.tail_image_label.setPixmap(self.tail_image_pixmap.scaled(600, 600, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.tail_image_label.resize(self.tail_image_pixmap.size())

    def update_state(self, value):
        global autotrade_type  # inserted
        autotrade_type = value

    def show_trading_explanation(self):
        explanation_text = '\n\n        트레이딩 설명:\n        \n        자동매매 a : 피보나치 0.13:진입, 0:손절, 0.5:익절\n\n        자동매매 b : 피보나치 0.13:진입, 0:손절, 0.618:익절\n\n        자동매매 A : 피보나치 0.236:진입, 0:손절, 0.5:익절\n         \n        자동매매 B : 피보나치 0.236:진입, 0:손절, 0.618:익절\n\n        자동매매 c : 피보나치 0.13:진입, -0.13:손절, 0.5:익절\n\n        자동매매 d : 피보나치 0.13:진입, -0.13:손절, 0.618:익절\n        \n        자동매매 C : 피보나치 0.236:진입, -0.13:손절, 0.5:익절\n        \n        자동매매 D : 피보나치 0.236:진입, -0.13:손절, 0.618:익절\n    \n        -------------------------------------------------\n        \n        롱 RSI/숏 RSI는 슬라이드 바를 통해 설정할 수 있습니다.\n        예시)\n        롱 RSI 20에 설정 : RSI 20 이하이고 피보나치 진입 조건 만족시 포지션 진입\n        숏 RSI 70에 설정 : RSI 70 이상이고 피보나치 진입 조건 만족시 포지션 진입\n        \n        (Tip) 롱 RSI가 높을수록, 숏 RSI 낮을수록 포지션 진입 확률이 높습니다\n        \n        -------------------------------------------------\n        \n        리스크 관리\n\n        설명:피보나치 (0)과 피보나치 (1) \n        차이가 5%이상 나면 포지션을 잡지 않습니다.\n\n        EX)비트코인 가격:60000$(0), 63000$(1)일 때.\n        둘의 값의 범위 차이가 5%이상이므로 \n        포지션을 잡지 않습니다.\n\n        이유:\n        1)피보나치 격차가 커진다는 것은\n        추세가 강하다는 것.\n        *승률 저하\n\n        2)피보나치 격차가 커질 수록,\n        손절 시 손실 금액이 커짐.\n        \n        -------------------------------------------------\n        \n        개미 페닉셀 (윗/밑꼬리) 전략\n\n        설명:차트의 꼬리는 개미들의 페닉셀 시\n        나타나는 경우가 많습니다.\n        특히 차트의 꼬리는 길 수록,차트의 되돌림이\n        힘이 강하다는 것을 의미합니다.\n\n        EX)\n        탈개미 AI (윗/밑꼬리) 전략 300 설정 시.\n\n        1)차트가 볼린저밴드를 뚫었을때.\n        피보나치 고점(1)이 꼬리를 300$이상 형성 시에만\n        탈개미 AI가 매수주문을 합니다.\n\n        즉,피보나치 1(고점) 차트 봉의 꼬리의 길이를\n        설정해서 진입할 수 있는 겁니다.\n\n        만약 100으로 설정 시.\n        1)피보나치 1(고점) 차트 봉의 꼬리가 100이하면\n        포지션 진입(X)\n        2)피보나치 1(고점) 차트 봉의 꼬리가 100이상면\n        포지션 진입(O)\n\n        *만약 이해가 안간다면,AI 백테스트 방에 질문 주시기 바랍니다.\n        \n        \n        '
        dialog = QDialog(self)
        dialog.setWindowTitle('트레이딩 설명')
        layout = QVBoxLayout()
        text_edit = QPlainTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setPlainText(explanation_text)
        text_edit.setFixedSize(800, 600)
        layout.addWidget(text_edit)
        dialog.setLayout(layout)
        dialog.exec_()

    def resizeEvent(self, event):
        new_size = event.size()
        super(MainWindow, self).resizeEvent(event)

    def open_url2(self):
        file_path = 'URLs/url2.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def connect_explanation(self):
        file_path = 'URLs/url6.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def open_url(self):
        file_path = 'URLs/url.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def open_url3(self):
        file_path = 'URLs/url3.txt'
        try:
            with open(file_path, 'r') as file:
                url = file.readline().strip()
        except FileNotFoundError:
            print(f'{file_path}0 파일을 찾을 수 없습니다.')
            return
        if url:
            webbrowser.open(url)
        else:  # inserted
            print('URL을 찾을 수 없습니다.')

    def stop_autotrade(self):
        global stop_autotrade  # inserted
        global autotrade_thread  # inserted
        global autotrade_type  # inserted
        global is_trading_active  # inserted
        autotrade_type = ''
        if not is_trading_active:
            QMessageBox.warning(self, '경고', '현재 실행 중인 자동매매가 없습니다.')
            return
        stop_autotrade = True
        if autotrade_thread is not None or autotrade_thread.is_alive():
            terminate_thread(autotrade_thread)
            autotrade_thread = None
            is_trading_active = False
            print('자동매매를 중지하는 중입니다. 잠시 기다려 주세요...')
        else:  # inserted
            print('자동매매 중지중입니다... 잠시 기다려주세요')
            print('계속 이 메시지가 뜬다면 프로그램을 완전히 종료해주세요')

    def USDT2BTC(self, bitget, leverage, trade_size):
        market_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
        btc_amount = 0
        btc_amount = float(trade_size) * float(leverage) / market_price
        return str(round(btc_amount, 3))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '프로그램 종료', '프로그램을 종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.kill(os.getpid(), signal.SIGTERM)
        else:  # inserted
            event.ignore()

    class RedirectText:
        def __init__(self, text_widget, clear_log_callback):
            self.text_widget = text_widget
            self.clear_log_callback = clear_log_callback

        def write(self, string):
            self.text_widget.append(string)
            time.sleep(0.2)
            self.text_widget.moveCursor(QTextCursor.End)

        def flush(self):
            return

        def clear_log(self):
            self.clear_log_callback()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.background_label.resize(self.size())

    def start_autotrade(self):
        global stop_autotrade  # inserted
        global autotrade_thread  # inserted
        global is_trading_active  # inserted
        try:
            trade_size = 0
            if is_trading_active:
                QMessageBox.warning(self, '경고', '자동매매가 이미 실행 중입니다.')
                return
            self.update_state(autotrade_type)
            print('차트가 조건이 맞을때까지 기다리는 중입니다... 포지션 진입시 로그에 표시됩니다')
            trade_size = self.trade_size_input.text()
            leverage = self.leverage_size_input.text()
            if not bitget:
                QMessageBox.critical(self, '오류', 'API 키가 잘못되었습니다. 다시 입력해주세요.')
                return
            bitget.mix_adjust_leverage(symbol=bitget_symbol, marginCoin='USDT', leverage=leverage, holdSide=None)
            trade_size = self.USDT2BTC(bitget, leverage, trade_size)
            print('포지션 진입 금액(BTC) : ', trade_size)
            if not bitget:
                QMessageBox.critical(self, '오류', 'API 키가 잘못되었습니다. 다시 입력해주세요.')
                return
            balances = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
            print('주문 가능한 USDT : ', balances)
            QMessageBox.information(self, '알림', '로그 창이 표시될 때까지 잠시 기다려주세요.')
            stop_autotrade = False
            is_trading_active = True
            autotrade_thread = threading.Thread(target=schedule_autotrade, args=(bitget, trade_size, self))
            autotrade_thread.start()
        except Exception as e:
            print(f'자동매매 실행 중 오류 발생: {e}0')

def validate_keys(self, api_key, secret_key, passphrase):
    try:
        Channel_list = ['Titan', 'cfv5', '7hm7', 'Kyungsoo', 'STEADY', 'MinGyu', '2TAN', 'choking', '무닌', '제니님', '2SIN', 'Trader-K', 'Blog partner']
        bitget = Client(api_key, secret_key, passphrase)
        VaildUid = bitget.spot_get_ApiKeyInfo()
        if VaildUid['data']['channel'] in Channel_list:
            QMessageBox.information(self, '인증 성공', '탈개미대학교 학생 신원확인 완료')
            account_info = bitget.mix_get_accounts(productType='umcbl')
            if account_info['data']:
                return bitget
            return None
        QMessageBox.critical(self, '인증 실패', '탈개미 대학교 학생이 아닙니다.\n(탈개미에 인증된 Bitget 계정이 아닙니다.)')
        return
    except Exception as e:
        print(f'API 키 유효성 검증 중 오류 발생: {e}0')
        print('API KEY를 올바르게 입력하였는지, 인증된 계정이 맞는지 확인해주세요')
        return

def get_current_status(bitget):
    try:
        balances = bitget.mix_get_accounts(productType='umcbl')['data']
        BTC_balance = 0
        for b in balances:
            if b['marginCoin'] == 'BTC':
                BTC_balance = float(b['available'])
            if b['marginCoin'] == 'USDT':
                USDT_balance = float(b['available'])
        positions = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        current_status = {'USDT Balance': USDT_balance, 'positions': positions}
    except Exception as e:
        print(f'현재 잔고 불러오기 오류 발생: {e}0')
    return current_status

def fetch_and_prepare_data(bitget):
    try:
        end_time = int(time.time()) * 1000
        start_time_daily = end_time - 45000000
        fiftymin_data = bitget.mix_get_candles(symbol=bitget_symbol, granularity='15m', startTime=start_time_daily, endTime=end_time)
        df_fiftymin = pd.DataFrame(fiftymin_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'ignore'])
        df_fiftymin = df_fiftymin.apply(pd.to_numeric, errors='coerce')
    except Exception as e:
        print(f'15분봉 차트 데이터 불러오기 실패: {e}0')

    def add_indicators(df):
        global leave_bus  # inserted
        global fibo_0870  # inserted
        global fibo_0950  # inserted
        global fibo_0820  # inserted
        global fibo_0500  # inserted
        global fibo_0030  # inserted
        global div  # inserted
        global fibo_0764  # inserted
        global fibo_1130  # inserted
        global fibo_0180  # inserted
        global fibo_Minus013  # inserted
        global fibo_0382  # inserted
        global fibo_0236  # inserted
        global fibo_0130  # inserted
        global fibo_0970  # inserted
        global fibo_0013  # inserted
        global fibo_0900  # inserted
        global fibo_0050  # inserted
        global fibo_0150  # inserted
        global fibo_0000  # inserted
        global fibo_1000  # inserted
        global fibo_error2  # inserted
        global fibo_0618  # inserted
        global fibo_0200  # inserted
        global fibo_0850  # inserted
        global fibo_0800  # inserted
        global fibo_error  # inserted
        global fibo_0100  # inserted
        try:
            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            fibo_0030 = fibo_0050 = fibo_0100 = fibo_0013 = fibo_0150 = fibo_0180 = fibo_0200 = 0
            fibo_0970 = fibo_0950 = fibo_0900 = fibo_0850 = fibo_0820 = fibo_0800 = 0
            if stop_autotrade:
                return (0, 0, 0)
            if extension:
                return (0, 0, 0)
            upper_high = 0
            lower_low = 0
            up_first = False
            low_first = False
            lower_idx = (-1)
            upper_idx = (-1)
            risk_up_idx = []
            risk_down_idx = []
            elite_up_idx = []
            elite_low_idx = []
            post_lower_df = []
            post_upper_df = []
            up_tail = [0, 0]
            low_tail = [0, 0]
            up_tail_per = 0
            low_tail_per = 0
            chart_fibo_per = False
            diverence_rsi_last = (-1)
            diverence_rsi_first = (-1)
            first_price = (-1)
            tail = 0
            previous_upper_df = pd.DataFrame()
            previous_lower_df = pd.DataFrame()
            recent_lower_df = pd.DataFrame()
            recent_upper_df = pd.DataFrame()
            df['RSI_14'] = ta.rsi(df['close'], length=16)
            df['Middle_Band'] = df['close'].rolling(window=20).mean()
            std_dev = df['close'].rolling(window=20).std()
            df['Upper_Band'] = round(df['Middle_Band'] + std_dev * 2, 1)
            df['Lower_Band'] = round(df['Middle_Band'] - std_dev * 2, 1)
            df['PlusTrue/MinusFalse'] = df['open'] < df['close']
            df['Candle_break_Upperband'] = df['high'] > df['Upper_Band']
            df['Candle_break_Lowerband'] = df['low'] < df['Lower_Band']
            df['Upperband_group'] = (df['Candle_break_Upperband']!= df['Candle_break_Upperband'].shift(1)).cumsum() * df['Candle_break_Upperband']
            df['Lowerband_group'] = (df['Candle_break_Lowerband']!= df['Candle_break_Lowerband'].shift(1)).cumsum() * df['Candle_break_Lowerband']
            upperband_groups = df[df['Upperband_group'] > 0]['Upperband_group'].unique()
            lowerband_groups = df[df['Lowerband_group'] > 0]['Lowerband_group'].unique()
            upperband_first_idx = df[df['Candle_break_Upperband'] == True].index.max() if not df[df['Candle_break_Upperband']].empty else None
            lowerband_first_idx = df[df['Candle_break_Lowerband'] == True].index.max() if not df[df['Candle_break_Lowerband']].empty else None
            if upperband_first_idx is not None and (lowerband_first_idx is None or upperband_first_idx > lowerband_first_idx):
                up_first = True
                if len(upperband_groups) > 0:
                    recent_upper_group = upperband_groups[(-1)]
                    recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                    if not recent_upper_df.empty:
                        upper_high = recent_upper_df['high'].max()
                        diverence_rsi_last = recent_upper_df['RSI_14'].max()
                    if len(upperband_groups) > 1:
                        previous_upper_group = upperband_groups[(-2)]
                        if previous_upper_group is not None:
                            previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                            if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                                combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                                if not combined_upper_df.empty:
                                    upper_high = combined_upper_df['high'].max()
                        diverence_rsi_first = previous_upper_df['RSI_14'].max()
                        if not previous_upper_df.empty:
                            first_price = previous_upper_df['high'].max()
                if len(lowerband_groups) > 0:
                    recent_lower_group = lowerband_groups[(-1)]
                    recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                    if not recent_lower_df.empty:
                        lower_low = recent_lower_df['low'].min()
                    if len(lowerband_groups) > 1:
                        previous_lower_group = lowerband_groups[(-2)]
                        if previous_lower_group is not None:
                            previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                            if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                                combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                                if not combined_lower_df.empty:
                                    lower_low = combined_lower_df['low'].min()
                else:  # inserted
                    lower_low = df['low'].min()
            else:  # inserted
                if lowerband_first_idx is not None and (upperband_first_idx is None or lowerband_first_idx > upperband_first_idx):
                    low_first = True
                    if len(lowerband_groups) > 0:
                        recent_lower_group = lowerband_groups[(-1)]
                        recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                        if not recent_lower_df.empty:
                            lower_low = recent_lower_df['low'].min()
                        diverence_rsi_last = recent_lower_df['RSI_14'].min()
                        if len(lowerband_groups) > 1:
                            previous_lower_group = lowerband_groups[(-2)]
                            if previous_lower_group is not None:
                                previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                                if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                                    combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                                    if not combined_lower_df.empty:
                                        lower_low = combined_lower_df['low'].min()
                            diverence_rsi_first = previous_lower_df['RSI_14'].min()
                            if not previous_upper_df.empty:
                                first_price = previous_upper_df['low'].min()
                    if len(upperband_groups) > 0:
                        recent_upper_group = upperband_groups[(-1)]
                        recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                        if not recent_upper_df.empty:
                            upper_high = recent_upper_df['high'].max()
                        if len(upperband_groups) > 1:
                            previous_upper_group = upperband_groups[(-2)]
                            if previous_upper_group is not None:
                                previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                                if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                                    combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                                    if not combined_upper_df.empty:
                                        upper_high = combined_upper_df['high'].max()
                    else:  # inserted
                        upper_high = df['high'].max()
            if upper_high > lower_low:
                fibo_0000 = round(lower_low, 1) + trading_error
                fibo_0130 = round(lower_low + 0.138 * (upper_high - lower_low), 1) + trading_error
                fibo_0236 = round(lower_low + 0.236 * (upper_high - lower_low), 1) + trading_error
                fibo_0382 = round(lower_low + 0.382 * (upper_high - lower_low), 1) + trading_error
                fibo_0500 = round(lower_low + 0.5 * (upper_high - lower_low), 1) + trading_error
                fibo_0618 = round(lower_low + 0.618 * (upper_high - lower_low), 1) + trading_error
                fibo_0764 = round(lower_low + 0.764 * (upper_high - lower_low), 1) + trading_error
                fibo_0870 = round(lower_low + 0.87 * (upper_high - lower_low), 1) + trading_error
                fibo_1000 = round(upper_high, 1) + trading_error
                fibo_Minus013 = round(lower_low + (-0.135) * (upper_high - lower_low), 1) + trading_error
                fibo_1130 = round(lower_low + 1.135 * (upper_high - lower_low), 1) + trading_error
                if PRO:
                    fibo_0030 = round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error
                    fibo_0050 = round(lower_low + 0.05 * (upper_high - lower_low), 1) + trading_error
                    fibo_0100 = round(lower_low + 0.1 * (upper_high - lower_low), 1) + trading_error
                    fibo_0015 = round(lower_low + 0.15 * (upper_high - lower_low), 1) + trading_error
                    fibo_0180 = round(lower_low + 0.18 * (upper_high - lower_low), 1) + trading_error
                    fibo_0200 = round(lower_low + 0.2 * (upper_high - lower_low), 1) + trading_error
                    fibo_0970 = round(lower_low + 0.97 * (upper_high - lower_low), 1) + trading_error
                    fibo_0950 = round(lower_low + 0.95 * (upper_high - lower_low), 1) + trading_error
                    fibo_0900 = round(lower_low + 0.9 * (upper_high - lower_low), 1) + trading_error
                    fibo_0850 = round(lower_low + 0.85 * (upper_high - lower_low), 1) + trading_error
                    fibo_0820 = round(lower_low + 0.82 * (upper_high - lower_low), 1) + trading_error
                    fibo_0800 = round(lower_low + 0.8 * (upper_high - lower_low), 1) + trading_error
                percentage_change = (fibo_1000 - fibo_0000) / fibo_0000 * 100
                if abs(percentage_change) >= 5:
                    chart_fibo_per = True
                else:  # inserted
                    chart_fibo_per = False
            fib_gap = fibo_1000 - fibo_0000
            upper_idx = df[df['high'] == upper_high].index
            lower_idx = df[df['low'] == lower_low].index
            if up_first == True:
                if diverence_request == True and len(upper_idx) > 0:
                    if diverence_rsi_last - diverence_rsi_first > 0 and fibo_1000 - first_price < 0:
                        div = True
                    else:  # inserted
                        if diverence_rsi_last - diverence_rsi_first < 0 and fibo_1000 - first_price > 0:
                            div = True
                        else:  # inserted
                            div = False
                if len(upper_idx) > 0:
                    post_upper_df = df.loc[upper_idx[0]:]
                if diverence_request == True:
                    if div == True:
                        pass
                    else:  # inserted
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if oneway_protect == True and len(df) > 0 and (fibo_0500!= 0):
                    latest_lower_band = df.loc[df.index[(-1)], 'Lower_Band']
                    if fibo_0500 < latest_lower_band:
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if tail_strategy == True and len(lower_idx) > 0:
                    if df.loc[lower_idx[0], 'Candle_break_Lowerband'] == True:
                        pass
                    else:  # inserted
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if len(upper_idx) > 0:
                    if fibo_value == 0:
                        tail = df.loc[upper_idx[0], 'high'] - fibo_1000
                    else:  # inserted
                        if fibo_value == 0.03:
                            tail = df.loc[upper_idx[0], 'high'] - fibo_0970
                        else:  # inserted
                            if fibo_value == 0.05:
                                tail = df.loc[upper_idx[0], 'high'] - fibo_0950
                            else:  # inserted
                                if fibo_value == 0.1:
                                    tail = df.loc[upper_idx[0], 'high'] - fibo_0900
                                else:  # inserted
                                    if fibo_value == 0.13:
                                        tail = df.loc[upper_idx[0], 'high'] - fibo_0870
                                    else:  # inserted
                                        if fibo_value == 0.15:
                                            tail = df.loc[upper_idx[0], 'high'] - fibo_0850
                                        else:  # inserted
                                            if fibo_value == 0.18:
                                                tail = df.loc[upper_idx[0], 'high'] - fibo_0820
                                            else:  # inserted
                                                if fibo_value == 0.2:
                                                    tail = df.loc[upper_idx[0], 'high'] - fibo_0800
                                                else:  # inserted
                                                    if fibo_value == 0.236:
                                                        tail = df.loc[upper_idx[0], 'high'] - fibo_0764
                    if df.loc[upper_idx[0], 'PlusTrue/MinusFalse'] == True:
                        if df.loc[upper_idx[0], 'high'] - df.loc[upper_idx[0], 'close'] >= tail:
                            pass
                        else:  # inserted
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    else:  # inserted
                        if df.loc[upper_idx[0], 'high'] - df.loc[upper_idx[0], 'open'] >= tail:
                            pass
                        else:  # inserted
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if post_upper_df.empty or (post_upper_df['low'] <= fibo_0618).any() and (not post_upper_df.empty) and (post_upper_df['high'].iloc[(-1)] == fibo_1000 and post_upper_df['low'].iloc[(-1)] <= fibo_0618) and (df['PlusTrue/MinusFalse'].iloc[(-1)] == True):
                    if (post_upper_df['low'] <= fibo_0618).any():
                        if post_upper_df['high'].iloc[(-1)] == fibo_1000 and post_upper_df['low'].iloc[(-1)] <= fibo_0618 and (df['PlusTrue/MinusFalse'].iloc[(-1)] == True):
                            pass
                        else:  # inserted
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                        pass
                else:  # inserted
                    fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                    fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                    fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                if not post_upper_df.empty and (post_upper_df['high'] > fibo_1000).any():
                    fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                    fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                    fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            else:  # inserted
                if low_first == True:
                    if len(lower_idx) > 0:
                        post_lower_df = df.loc[lower_idx[0]:]
                    if not diverence_request == True or not len(upper_idx) > 0 or (diverence_rsi_last - diverence_rsi_first > 0 and fibo_0000 - first_price < 0):
                        div = True
                    else:  # inserted
                        if diverence_rsi_last - diverence_rsi_first < 0 and fibo_0000 - first_price > 0:
                            div = True
                        else:  # inserted
                            div = False
                    if not diverence_request == True or div == True:
                        pass
                    else:  # inserted
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if oneway_protect == True and len(df) > 0 and (fibo_0500!= 0):
                        latest_upper_band = df.loc[df.index[(-1)], 'Upper_Band']
                        if fibo_0500 > latest_upper_band:
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if tail_strategy and len(upper_idx) > 0:
                        if df.loc[upper_idx[0], 'Candle_break_Upperband']:
                            pass
                        else:  # inserted
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if len(lower_idx) > 0:
                        if fibo_value == 0:
                            tail = fibo_0000 - df.loc[lower_idx[0], 'low']
                        else:  # inserted
                            if fibo_value == 0.03:
                                tail = fibo_0030 - df.loc[lower_idx[0], 'low']
                            else:  # inserted
                                if fibo_value == 0.05:
                                    tail = fibo_0050 - df.loc[lower_idx[0], 'low']
                                else:  # inserted
                                    if fibo_value == 0.1:
                                        tail = fibo_0100 - df.loc[lower_idx[0], 'low']
                                    else:  # inserted
                                        if fibo_value == 0.13:
                                            tail = fibo_0130 - df.loc[lower_idx[0], 'low']
                                        else:  # inserted
                                            if fibo_value == 0.15:
                                                tail = fibo_0150 - df.loc[lower_idx[0], 'low']
                                            else:  # inserted
                                                if fibo_value == 0.18:
                                                    tail = fibo_0180 - df.loc[lower_idx[0], 'low']
                                                else:  # inserted
                                                    if fibo_value == 0.2:
                                                        tail = fibo_0200 - df.loc[lower_idx[0], 'low']
                                                    else:  # inserted
                                                        if fibo_value == 0.236:
                                                            tail = fibo_0236 - df.loc[lower_idx[0], 'low']
                        if df.loc[lower_idx[0], 'PlusTrue/MinusFalse'] == True:
                            if df.loc[lower_idx[0], 'open'] - df.loc[lower_idx[0], 'low'] >= tail:
                                pass
                            else:  # inserted
                                fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                                fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                                fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                        else:  # inserted
                            if df.loc[lower_idx[0], 'close'] - df.loc[lower_idx[0], 'low'] >= tail:
                                pass
                            else:  # inserted
                                fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                                fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                                fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if post_lower_df.empty or not (post_lower_df['high'] >= fibo_0382).any() or (post_lower_df['low'].iloc[(-1)] == fibo_0000 and post_lower_df['high'].iloc[(-1)] >= fibo_0382 and (df['PlusTrue/MinusFalse'].iloc[(-1)] == False)):
                        if not (post_lower_df['high'] >= fibo_0382).any() or (post_lower_df['high'].iloc[(-1)] >= fibo_0382 and df['PlusTrue/MinusFalse'].iloc[(-1)] == False):
                            pass
                        else:  # inserted
                            fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                            fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                            fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                            pass
                    else:  # inserted
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if not post_lower_df.empty and (post_lower_df['low'] < fibo_0000).any():
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            if chart_fibo_per:
                fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                fibo_1000 = fibo_Minus013 = fibo_1130 = 0
            fibo_error = abs(round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
            fibo_error2 = abs(round(lower_low + 0.01 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
            recent_df = df.tail(10)
            recent_high = recent_df['high'].max()
            recent_low = recent_df['low'].min()
            if fibo_0000 > recent_low or fibo_1000 < recent_high:
                leave_bus = True
            else:  # inserted
                leave_bus = False
        except Exception as e:
            print('차트 데이터 보류 (조건이 아님)', e)
            traceback.print_exc()
        return (df, up_first, low_first)
    if not extension:
        df_fif, up, low = add_indicators(df_fiftymin)
    else:  # inserted
        df_fif, up, low = add_indicators_extension(df_fiftymin)
    df_recent_10 = df_fif.tail(20)
    return (df_fiftymin, df_recent_10, up, low)

def add_indicators_extension(df):
    global fibo_1382  # inserted
    global fibo_Minus0618  # inserted
    global fibo_0870  # inserted
    global fibo_1500  # inserted
    global fibo_0950  # inserted
    global fibo_0820  # inserted
    global fibo_0500  # inserted
    global fibo_0030  # inserted
    global fibo_1618  # inserted
    global fibo_0764  # inserted
    global fibo_1130  # inserted
    global fibo_0180  # inserted
    global fibo_Minus0236  # inserted
    global fibo_Minus013  # inserted
    global fibo_0382  # inserted
    global fibo_0236  # inserted
    global fibo_0130  # inserted
    global fibo_0970  # inserted
    global fibo_0013  # inserted
    global fibo_0900  # inserted
    global fibo_1236  # inserted
    global fibo_Minus0500  # inserted
    global fibo_0050  # inserted
    global fibo_0150  # inserted
    global fibo_0000  # inserted
    global fibo_1000  # inserted
    global fibo_error2  # inserted
    global fibo_0618  # inserted
    global fibo_0200  # inserted
    global fibo_0850  # inserted
    global fibo_0800  # inserted
    global fibo_error  # inserted
    global fibo_Minus0382  # inserted
    global fibo_0100  # inserted
    try:
        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = fibo_1000 = fibo_Minus013 = fibo_1130 = 0
        fibo_0030 = fibo_0050 = fibo_0100 = fibo_0013 = fibo_0150 = fibo_0180 = fibo_0200 = 0
        fibo_0970 = fibo_0950 = fibo_0900 = fibo_0850 = fibo_0820 = fibo_0800 = 0
        fibo_Minus0236 = fibo_Minus0382 = fibo_Minus0500 = fibo_Minus0618 = 0
        if stop_autotrade:
            return (0, 0, 0)
        upper_high = 0
        lower_low = 0
        up_first = False
        low_first = False
        lower_idx = (-1)
        upper_idx = (-1)
        risk_up_idx = []
        risk_down_idx = []
        elite_up_idx = []
        elite_low_idx = []
        post_lower_df = []
        post_upper_df = []
        up_tail = [0, 0]
        low_tail = [0, 0]
        up_tail_per = 0
        low_tail_per = 0
        chart_fibo_per = False
        diverence_rsi_last = (-1)
        diverence_rsi_first = (-1)
        first_price = (-1)
        tail = 0
        previous_upper_df = pd.DataFrame()
        previous_lower_df = pd.DataFrame()
        recent_lower_df = pd.DataFrame()
        recent_upper_df = pd.DataFrame()
        df['RSI_14'] = ta.rsi(df['close'], length=16)
        df['Middle_Band'] = df['close'].rolling(window=20).mean()
        std_dev = df['close'].rolling(window=20).std()
        df['Upper_Band'] = round(df['Middle_Band'] + std_dev * 2, 1)
        df['Lower_Band'] = round(df['Middle_Band'] - std_dev * 2, 1)
        df['PlusTrue/MinusFalse'] = df['open'] < df['close']
        df['Candle_break_Upperband'] = df['high'] > df['Upper_Band']
        df['Candle_break_Lowerband'] = df['low'] < df['Lower_Band']
        df['Upperband_group'] = (df['Candle_break_Upperband']!= df['Candle_break_Upperband'].shift(1)).cumsum() * df['Candle_break_Upperband']
        df['Lowerband_group'] = (df['Candle_break_Lowerband']!= df['Candle_break_Lowerband'].shift(1)).cumsum() * df['Candle_break_Lowerband']
        upperband_groups = df[df['Upperband_group'] > 0]['Upperband_group'].unique()
        lowerband_groups = df[df['Lowerband_group'] > 0]['Lowerband_group'].unique()
        upperband_first_idx = df[df['Candle_break_Upperband'] == True].index.max() if not df[df['Candle_break_Upperband']].empty else None
        lowerband_first_idx = df[df['Candle_break_Lowerband'] == True].index.max() if not df[df['Candle_break_Lowerband']].empty else None
        if upperband_first_idx is not None and (lowerband_first_idx is None or upperband_first_idx > lowerband_first_idx):
            up_first = True
            if len(upperband_groups) > 0:
                recent_upper_group = upperband_groups[(-1)]
                recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                if not recent_upper_df.empty:
                    upper_high = recent_upper_df['high'].max()
                    diverence_rsi_last = recent_upper_df['RSI_14'].max()
                if len(upperband_groups) > 1:
                    previous_upper_group = upperband_groups[(-2)]
                    if previous_upper_group is not None:
                        previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                        if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                            combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                            if not combined_upper_df.empty:
                                upper_high = combined_upper_df['high'].max()
                    diverence_rsi_first = previous_upper_df['RSI_14'].max()
                    if not previous_upper_df.empty:
                        first_price = previous_upper_df['high'].max()
            if len(lowerband_groups) > 0:
                recent_lower_group = lowerband_groups[(-1)]
                recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                if not recent_lower_df.empty:
                    lower_low = recent_lower_df['low'].min()
                if len(lowerband_groups) > 1:
                    previous_lower_group = lowerband_groups[(-2)]
                    if previous_lower_group is not None:
                        previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                        if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                            combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                            if not combined_lower_df.empty:
                                lower_low = combined_lower_df['low'].min()
            else:  # inserted
                lower_low = df['low'].min()
        else:  # inserted
            if lowerband_first_idx is not None:
                if upperband_first_idx is None or lowerband_first_idx > upperband_first_idx:
                    low_first = True
                    if len(lowerband_groups) > 0:
                        recent_lower_group = lowerband_groups[(-1)]
                        recent_lower_df = df[df['Lowerband_group'] == recent_lower_group]
                        if not recent_lower_df.empty:
                            lower_low = recent_lower_df['low'].min()
                        diverence_rsi_last = recent_lower_df['RSI_14'].min()
                        if len(lowerband_groups) > 1:
                            previous_lower_group = lowerband_groups[(-2)]
                            if previous_lower_group is not None:
                                previous_lower_df = df[df['Lowerband_group'] == previous_lower_group]
                                if not previous_lower_df.empty and abs(recent_lower_df.index[0] - previous_lower_df.index[(-1)]) <= 5:
                                    combined_lower_df = pd.concat([recent_lower_df, previous_lower_df])
                                    if not combined_lower_df.empty:
                                        lower_low = combined_lower_df['low'].min()
                            diverence_rsi_first = previous_lower_df['RSI_14'].min()
                            if not previous_upper_df.empty:
                                first_price = previous_upper_df['low'].min()
                    if len(upperband_groups) > 0:
                        recent_upper_group = upperband_groups[(-1)]
                        recent_upper_df = df[df['Upperband_group'] == recent_upper_group]
                        if not recent_upper_df.empty:
                            upper_high = recent_upper_df['high'].max()
                        if len(upperband_groups) > 1:
                            previous_upper_group = upperband_groups[(-2)]
                            if previous_upper_group is not None:
                                previous_upper_df = df[df['Upperband_group'] == previous_upper_group]
                                if not previous_upper_df.empty and abs(recent_upper_df.index[0] - previous_upper_df.index[(-1)]) <= 5:
                                    combined_upper_df = pd.concat([recent_upper_df, previous_upper_df])
                                    if not combined_upper_df.empty:
                                        upper_high = combined_upper_df['high'].max()
                    else:  # inserted
                        upper_high = df['high'].max()
        if upper_high > lower_low:
            fibo_0000 = round(lower_low, 1) + trading_error
            fibo_0130 = round(lower_low + 0.138 * (upper_high - lower_low), 1) + trading_error
            fibo_0236 = round(lower_low + 0.236 * (upper_high - lower_low), 1) + trading_error
            fibo_0382 = round(lower_low + 0.382 * (upper_high - lower_low), 1) + trading_error
            fibo_0500 = round(lower_low + 0.5 * (upper_high - lower_low), 1) + trading_error
            fibo_0618 = round(lower_low + 0.618 * (upper_high - lower_low), 1) + trading_error
            fibo_0764 = round(lower_low + 0.764 * (upper_high - lower_low), 1) + trading_error
            fibo_0870 = round(lower_low + 0.87 * (upper_high - lower_low), 1) + trading_error
            fibo_1000 = round(upper_high, 1) + trading_error
            fibo_Minus013 = round(lower_low + (-0.135) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0236 = round(lower_low + (-0.236) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0382 = round(lower_low + (-0.382) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0500 = round(lower_low + (-0.5) * (upper_high - lower_low), 1) + trading_error
            fibo_Minus0618 = round(lower_low + (-0.618) * (upper_high - lower_low), 1) + trading_error
            fibo_1130 = round(lower_low + 1.135 * (upper_high - lower_low), 1) + trading_error
            fibo_1236 = round(lower_low + 1.1236 * (upper_high - lower_low), 1) + trading_error
            fibo_1382 = round(lower_low + 1.1382 * (upper_high - lower_low), 1) + trading_error
            fibo_1500 = round(lower_low + 1.15 * (upper_high - lower_low), 1) + trading_error
            fibo_1618 = round(lower_low + 1.1618 * (upper_high - lower_low), 1) + trading_error
            if PRO:
                fibo_0030 = round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error
                fibo_0050 = round(lower_low + 0.05 * (upper_high - lower_low), 1) + trading_error
                fibo_0100 = round(lower_low + 0.1 * (upper_high - lower_low), 1) + trading_error
                fibo_0015 = round(lower_low + 0.15 * (upper_high - lower_low), 1) + trading_error
                fibo_0180 = round(lower_low + 0.18 * (upper_high - lower_low), 1) + trading_error
                fibo_0200 = round(lower_low + 0.2 * (upper_high - lower_low), 1) + trading_error
                fibo_0970 = round(lower_low + 0.97 * (upper_high - lower_low), 1) + trading_error
                fibo_0950 = round(lower_low + 0.95 * (upper_high - lower_low), 1) + trading_error
                fibo_0900 = round(lower_low + 0.9 * (upper_high - lower_low), 1) + trading_error
                fibo_0850 = round(lower_low + 0.85 * (upper_high - lower_low), 1) + trading_error
                fibo_0820 = round(lower_low + 0.82 * (upper_high - lower_low), 1) + trading_error
                fibo_0800 = round(lower_low + 0.8 * (upper_high - lower_low), 1) + trading_error
            percentage_change = (fibo_1000 - fibo_0000) / fibo_0000 * 100
            chart_fibo_per = False
        fib_gap = fibo_1000 - fibo_0000
        upper_idx = df[df['high'] == upper_high].index
        lower_idx = df[df['low'] == lower_low].index
        if up_first:
            if len(upper_idx) > 0:
                post_upper_df = df.loc[upper_idx[0]:]
                if not post_upper_df.empty:
                    if (post_upper_df['low'] <= fibo_0764).any() and (post_upper_df['low'] > fibo_0382).all() and (post_upper_df['low'] > post_upper_df['Lower_Band']).all():
                        pass
                    else:  # inserted
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if df.loc[upper_idx[0], 'low'] <= fibo_0618:
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
        else:  # inserted
            if low_first and len(lower_idx) > 0:
                post_lower_df = df.loc[lower_idx[0]:]
                if post_lower_df.empty or ((post_lower_df['high'] >= fibo_0236).any() and (post_lower_df['high'] < fibo_0618).all() and (post_lower_df['high'] < post_lower_df['Upper_Band']).all()):
                    pass
                else:  # inserted
                    fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                    fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                    fibo_1000 = fibo_Minus013 = fibo_1130 = 0
                    if df.loc[lower_idx[0], 'high'] >= fibo_0382:
                        fibo_0000 = fibo_0130 = fibo_0236 = fibo_0382 = 0
                        fibo_0500 = fibo_0618 = fibo_0764 = fibo_0870 = 0
                        fibo_1000 = fibo_Minus013 = fibo_1130 = 0
        fibo_error = abs(round(lower_low + 0.03 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
        fibo_error2 = abs(round(lower_low + 0.01 * (upper_high - lower_low), 1) + trading_error - fibo_0000)
        recent_df = df.tail(10)
        recent_high = recent_df['high'].max()
        recent_low = recent_df['low'].min()
    except Exception as e:
        print('차트 데이터 보류 (조건이 아님)', e)
        traceback.print_exc()
    return (df, up_first, low_first)

def analyze_data(bitget, data, up, low):
    try:
        recent_RSI = 0
        positions = []
        positions = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if stop_autotrade:
            res = '아직 주문 없음'
            return res
        if isinstance(positions, list) and len(positions) > 0 and isinstance(positions[0], dict):
            if 'holdSide' in positions[0]:
                if positions[0]['holdSide'] == 'long' or positions[0]['holdSide'] == 'short':
                    res = '탈개미 AI : 현재 포지션이 진행중입니다. 포지션 종료 후 판단 진행 예정'
                    return res
            print('포지션 데이터 없음')
        recent_RSI = data['RSI_14'].iloc[(-1)]
        if not extension:
            if up == True and recent_RSI >= short_rsi_value:
                res = 'open short'
                return res
            if low == True and recent_RSI <= long_rsi_value:
                res = 'open long'
                return res
            res = 'stay'
            return res
        if up == True:
            res = 'open long extension'
            return res
        if low == True:
            res = 'open short extension'
            return res
        res = 'stay'
        return res
        return res
    except Exception as e:
        print('포지션 판단 보류', e)

def open_long(bitget, trade_size):
    global order_flag  # inserted
    start_time = 0
    formatted_time = 0
    result = '아직 주문 없음'
    if stop_autotrade:
        return
    position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
    try:
        if not isinstance(position_data, list) and leave_bus == True:
            pass
        else:  # inserted
            if order_flag:
                order_flag = False
                USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
                if USDT_balance > 67:
                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                    if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0) or (fibo_0382 <= current_price):
                        pass
                    else:  # inserted
                        if fibo_0500 >= current_price:
                            if Trade_Level['E'] == 1:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                start_time = int(time.time())
                                print('탈개미 AI 0.13% 진입 준비중입니다....')
                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if stop_autotrade:
                                        return
                                    if elapsed_time > 900:
                                        print('재판단')
                                        break
                                else:  # inserted
                                    print('주문 진행 중...')
                                    print('『황금비율』 롱 포지션 예상 진입 구간(0.13%): ' + str(fibo_0130))
                                    print('『황금비율』 롱 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                    print('『황금비율』 롱 포지션 예상 손절 구간(0%): ' + str(fibo_0000))
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_0000)
                                    else:  # inserted
                                        print('익절 적용 X')
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                            else:  # inserted
                                if Trade_Level['F'] == 1:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    print('탈개미 AI 0.13% 진입 준비중입니다....')
                                    start_time = time.time()
                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = int(time.time()) - start_time
                                        if stop_autotrade:
                                            return
                                        if elapsed_time > 900:
                                            break
                                    else:  # inserted
                                        print('주문 진행 중...')
                                        print('『황금비율』 롱 포지션 예상 진입 구간(0.13%): ' + str(fibo_0130))
                                        print('『황금비율』 롱 포지션 예상 익절 구간(0.618%): ' + str(fibo_0618))
                                        print('『황금비율』 롱 포지션 예상 손절 구간(0%): ' + str(fibo_0000))
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_0000)
                                        else:  # inserted
                                            print('익절 적용 X')
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                                else:  # inserted
                                    if Trade_Level['A'] == 1:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        print('탈개미 AI 0.236% 진입 준비중입니다....')
                                        start_time = int(time.time())
                                        while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = time.time() - start_time
                                            if stop_autotrade:
                                                return
                                            if elapsed_time > 900:
                                                print('재판단')
                                                break
                                        else:  # inserted
                                            print('주문 진행 중...')
                                            print('『황금비율』 롱 포지션 예상 진입 구간(0.236%): ' + str(fibo_0236))
                                            print('『황금비율』 롱 포지션 50% 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                            print('『황금비율』 롱 포지션 예상 손절 구간(0%): ' + str(fibo_0000))
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_0000)
                                            else:  # inserted
                                                print('익절 적용 X')
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                                    else:  # inserted
                                        if Trade_Level['B'] == 1:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            print('탈개미 AI 0.236% 진입 준비중입니다....')
                                            start_time = int(time.time())
                                            while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if stop_autotrade:
                                                    return
                                                if elapsed_time > 900:
                                                    print('재판단')
                                                    break
                                            else:  # inserted
                                                print('주문 진행 중...')
                                                print('『황금비율』 롱 포지션 예상 진입 구간(0.236%): ' + str(fibo_0236))
                                                print('『황금비율』 롱 포지션 예상 익절 구간(0.618%): ' + str(fibo_0618))
                                                print('『황금비율』 롱 포지션 예상 손절 구간(0%): ' + str(fibo_0000))
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_0000)
                                                else:  # inserted
                                                    print('익절 적용 X')
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_0000)
                                        else:  # inserted
                                            if Trade_Level['G'] == 1:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                print('탈개미 AI 0.13% 진입 준비중입니다....')
                                                start_time = int(time.time())
                                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if stop_autotrade:
                                                        return
                                                    if elapsed_time > 900:
                                                        print('재판단')
                                                        break
                                                else:  # inserted
                                                    print('주문 진행 중...')
                                                    print('『황금비율』 롱 포지션 예상 진입 구간(0.13%): ' + str(fibo_0130))
                                                    print('『황금비율』 롱 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                                    print('『황금비율』 롱 포지션 예상 손절 구간(-0.13%): ' + str(fibo_Minus013))
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_Minus013)
                                                    else:  # inserted
                                                        print('익절 적용 X')
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                                            else:  # inserted
                                                if Trade_Level['H'] == 1:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    print('탈개미 AI 0.13% 진입 준비중입니다....')
                                                    start_time = int(time.time())
                                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if stop_autotrade:
                                                            return
                                                        if elapsed_time > 900:
                                                            print('재판단')
                                                            break
                                                    else:  # inserted
                                                        print('주문 진행 중...')
                                                        print('『황금비율』 롱 포지션 예상 진입 구간(0.13%): ' + str(fibo_0130))
                                                        print('『황금비율』 롱 포지션 예상 익절 구간(0.618%): ' + str(fibo_0618))
                                                        print('『황금비율』 롱 포지션 예상 손절 구간(-0.13%): ' + str(fibo_Minus013))
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_Minus013)
                                                        else:  # inserted
                                                            print('익절 적용 X')
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                                                else:  # inserted
                                                    if Trade_Level['C'] == 1:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        print('탈개미 AI 0.236% 진입 준비중입니다....')
                                                        start_time = time.time()
                                                        while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = time.time() - start_time
                                                            if stop_autotrade:
                                                                return
                                                            if elapsed_time > 900:
                                                                print('재판단')
                                                                break
                                                        else:  # inserted
                                                            print('주문 진행 중...')
                                                            print('『황금비율』 롱 포지션 예상 진입 구간(0.236%): ' + str(fibo_0236))
                                                            print('『황금비율』 롱 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                                            print('『황금비율』 롱 포지션 예상 손절 구간(-0.13%): ' + str(fibo_Minus013))
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_Minus013)
                                                            else:  # inserted
                                                                print('익절 적용 X')
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                                                    else:  # inserted
                                                        if Trade_Level['D'] == 1:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            print('탈개미 AI 0.236% 진입 준비중입니다....')
                                                            start_time = time.time()
                                                            while current_price > fibo_0236 + fibo_error or current_price < fibo_0236 - fibo_error2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = time.time() - start_time
                                                                if stop_autotrade:
                                                                    return
                                                                finally:  # inserted
                                                                    order_flag = True
                                                                    order_flag = True
                                                                if elapsed_time > 900:
                                                                    print('재판단')
                                                                    break
                                                            else:  # inserted
                                                                print('주문 진행 중...')
                                                                print('『황금비율』 롱 포지션 예상 진입 구간(0.236%): ' + str(fibo_0236))
                                                                print('『황금비율』 롱 포지션 예상 익절 구간(0.618%): ' + str(fibo_0618))
                                                                print('『황금비율』 롱 포지션 예상 손절 구간(-0.13%): ' + str(fibo_Minus013))
                                                                if TP_excute == True:
                                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0618, presetStopLossPrice=fibo_Minus013)
                                                                else:  # inserted
                                                                    print('익절 적용 X')
                                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0236, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_Minus013)
                            if result!= '아직 주문 없음':
                                print(f'주문 결과: {result}0')
                                timestamp = time.time()
                                kst_timezone = pytz.timezone('Asia/Seoul')
                                kst_time = datetime.fromtimestamp(timestamp, kst_timezone)
                                formatted_time = kst_time.strftime('%Y-%m-%d %H:%M:%S')
                                print(f'주문 요청 시간 (한국 시각): {formatted_time}0')
                            pass
                else:  # inserted
                    print('USDT 잔액 부족')
                    print('주문 가능한 금액(USDT) : ', USDT_balance)
                    print('주문 가능한 금액이 0.001BTC를 만족하는 지 확인해 주세요')
    except Exception as e:
        if '40762' in str(e):
            print('주문 금액이 잔액을 초과합니다. 잔액을 확인하고 주문 금액을 조정하세요.')
        print(f'구매 주문 실행 실패: {e}0')

def open_long_extension(bitget, trade_size):
    global order_flag  # inserted
    start_time = 0
    formatted_time = 0
    result = '아직 주문 없음'
    position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
    if stop_autotrade:
        return
    try:
        if not isinstance(position_data, list) or leave_bus == True:
            pass
        else:  # inserted
            if order_flag:
                order_flag = False
                USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
                if USDT_balance > 67:
                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                    if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0):
                        pass
                    else:  # inserted
                        if not fibo_0618 < current_price or Trade_Level['A'] == 1:
                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                            start_time = int(time.time())
                            while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                elapsed_time = int(time.time()) - start_time
                                if stop_autotrade:
                                    return
                                if elapsed_time > 60:
                                    break
                            else:  # inserted
                                print('주문 진행 중...')
                                print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                print('『황금비율』 롱 포지션 예상 익절 구간(1.13%): ' + str(fibo_1130))
                                print('『황금비율』 롱 포지션 예상 손절 구간(0.618%): ' + str(fibo_0618))
                                if TP_excute == True:
                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1130, presetStopLossPrice=fibo_0618)
                        else:  # inserted
                            if Trade_Level['B'] == 1:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                start_time = time.time()
                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if stop_autotrade:
                                        return
                                    if elapsed_time > 60:
                                        break
                                else:  # inserted
                                    print('주문 진행 중...')
                                    print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                    print('『황금비율』 롱 포지션 예상 익절 구간(1.13%): ' + str(fibo_1130))
                                    print('『황금비율』 롱 포지션 예상 손절 구간(0.5%): ' + str(fibo_0500))
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1130, presetStopLossPrice=fibo_0500)
                            else:  # inserted
                                if Trade_Level['C'] == 1:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    start_time = int(time.time())
                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = time.time() - start_time
                                        if stop_autotrade:
                                            return
                                        if elapsed_time > 60:
                                            break
                                    else:  # inserted
                                        print('주문 진행 중...')
                                        print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                        print('『황금비율』 롱 포지션 예상 익절 구간(1.13%): ' + str(fibo_1130))
                                        print('『황금비율』 롱 포지션 예상 손절 구간(0.382%): ' + str(fibo_0382))
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1130, presetStopLossPrice=fibo_0382)
                                else:  # inserted
                                    if Trade_Level['D'] == 1:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        start_time = int(time.time())
                                        while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if stop_autotrade:
                                                return
                                            if elapsed_time > 60:
                                                break
                                        else:  # inserted
                                            print('주문 진행 중...')
                                            print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                            print('『황금비율』 롱 포지션 예상 익절 구간(1.236%): ' + str(fibo_1236))
                                            print('『황금비율』 롱 포지션 예상 손절 구간(0.618%): ' + str(fibo_0618))
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1236, presetStopLossPrice=fibo_0618)
                                    else:  # inserted
                                        if Trade_Level['E'] == 1:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            start_time = int(time.time())
                                            while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if stop_autotrade:
                                                    return
                                                if elapsed_time > 60:
                                                    break
                                            else:  # inserted
                                                print('주문 진행 중...')
                                                print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                                print('『황금비율』 롱 포지션 예상 익절 구간(1.236%): ' + str(fibo_1236))
                                                print('『황금비율』 롱 포지션 예상 손절 구간(0.5%): ' + str(fibo_0500))
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1236, presetStopLossPrice=fibo_0500)
                                        else:  # inserted
                                            if Trade_Level['F'] == 1:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                start_time = int(time.time())
                                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if stop_autotrade:
                                                        return
                                                    if elapsed_time > 60:
                                                        break
                                                else:  # inserted
                                                    print('주문 진행 중...')
                                                    print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                                    print('『황금비율』 롱 포지션 예상 익절 구간(1.236%): ' + str(fibo_1236))
                                                    print('『황금비율』 롱 포지션 예상 손절 구간(0.382%): ' + str(fibo_0382))
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1236, presetStopLossPrice=fibo_0382)
                                            else:  # inserted
                                                if Trade_Level['G'] == 1:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    start_time = int(time.time())
                                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if stop_autotrade:
                                                            return
                                                        if elapsed_time > 60:
                                                            break
                                                    else:  # inserted
                                                        print('주문 진행 중...')
                                                        print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                                        print('『황금비율』 롱 포지션 예상 익절 구간(1.5%): ' + str(fibo_1500))
                                                        print('『황금비율』 롱 포지션 예상 손절 구간(0.618%): ' + str(fibo_0618))
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1500, presetStopLossPrice=fibo_0618)
                                                else:  # inserted
                                                    if Trade_Level['H'] == 1:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        start_time = int(time.time())
                                                        while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = int(time.time()) - start_time
                                                            if stop_autotrade:
                                                                return
                                                            if elapsed_time > 60:
                                                                break
                                                        else:  # inserted
                                                            print('주문 진행 중...')
                                                            print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                                            print('『황금비율』 롱 포지션 예상 익절 구간(1.5%): ' + str(fibo_1500))
                                                            print('『황금비율』 롱 포지션 예상 손절 구간(0.5%): ' + str(fibo_0500))
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1500, presetStopLossPrice=fibo_0500)
                                                    else:  # inserted
                                                        if Trade_Level['I'] == 1:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            start_time = int(time.time())
                                                            while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = int(time.time()) - start_time
                                                                if stop_autotrade:
                                                                    return
                                                                if elapsed_time > 60:
                                                                    break
                                                            else:  # inserted
                                                                print('주문 진행 중...')
                                                                print('『황금비율』 롱 포지션 예상 진입 구간(0.87%): ' + str(fibo_0870))
                                                                print('『황금비율』 롱 포지션 예상 익절 구간(1.5%): ' + str(fibo_1500))
                                                                print('『황금비율』 롱 포지션 예상 손절 구간(0.382%): ' + str(fibo_0382))
                                                                if TP_excute == True:
                                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_long', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_1500, presetStopLossPrice=fibo_0382)
                        if result!= '아직 주문 없음':
                            print(f'주문 결과: {result}0')
                            timestamp = time.time()
                            kst_timezone = pytz.timezone('Asia/Seoul')
                            kst_time = datetime.fromtimestamp(timestamp, kst_timezone)
                            formatted_time = kst_time.strftime('%Y-%m-%d %H:%M:%S')
                            print(f'주문 요청 시간 (한국 시각): {formatted_time}0')
                        pass
                else:  # inserted
                    print('USDT 잔액 부족')
                    print('주문 가능한 금액(USDT) : ', USDT_balance)
                    print('주문 가능한 금액이 0.001BTC를 만족하는 지 확인해 주세요')
    except Exception as e:
        if '40762' in str(e):
            print('주문 금액이 잔액을 초과합니다. 잔액을 확인하고 주문 금액을 조정하세요.')
        print(f'구매 주문 실행 실패: {e}0')
    finally:  # inserted
        pass  # postinserted
    order_flay = True
    order_flay = True
    order_flay = True
    order_flay = True

def close_long(bitget, trade_size):
    print('BTC 판매 시도 중...')
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        print(f'포지션 데이터 구조: {position_data}0')
        if isinstance(position_data, list) and position_data and (position_data[0]['holdSide'] == 'long'):
            print('주문 진행 중...')
            result = bitget.mix_place_order(symbol=bitget_symbol, side='close_long', orderType='market', size=trade_size, marginCoin='USDT', clientOrderId=random_string('sell'))
            print(f'판매 주문 성공: {result}0')
        else:  # inserted
            print('닫을 롱 포지션이 없습니다')
    except Exception as e:
        print(f'판매 주문 실행 실패: {e}0')

def open_short(bitget, trade_size):
    global order_flag  # inserted
    start_time = 0
    result = '아직 주문 없음'
    formatted_time = 0
    if stop_autotrade:
        return
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if not isinstance(position_data, list) or leave_bus == True:
            pass
        else:  # inserted
            if order_flag:
                order_flag = False
                USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
                if USDT_balance > 67:
                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                    if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0) or (fibo_0764 >= current_price):
                        pass
                    else:  # inserted
                        if current_price > fibo_0764 and current_price < fibo_1000:
                            if Trade_Level['E'] == 1:
                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                start_time = int(time.time())
                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    elapsed_time = int(time.time()) - start_time
                                    if stop_autotrade:
                                        return
                                    if elapsed_time > 60:
                                        break
                                else:  # inserted
                                    print('주문 진행 중...')
                                    print('『황금비율』 숏 포지션 예상 진입 구간(0.13%): ' + str(fibo_0870))
                                    print('『황금비율』 숏 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                    print('『황금비율』 숏 포지션 예상 손절 구간(0%): ' + str(fibo_1000))
                                    if TP_excute == True:
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1000)
                                    else:  # inserted
                                        print('익절 설정 X')
                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                            else:  # inserted
                                if Trade_Level['F'] == 1:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    start_time = int(time.time())
                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = int(time.time()) - start_time
                                        if stop_autotrade:
                                            return
                                        if elapsed_time > 60:
                                            break
                                    else:  # inserted
                                        print('주문 진행 중...')
                                        print('『황금비율』 숏 포지션 예상 진입 구간(0.13%): ' + str(fibo_0870))
                                        print('『황금비율』 숏 포지션 예상 익절 구간(0.618%): ' + str(fibo_0382))
                                        print('『황금비율』 숏 포지션 예상 손절 구간(0%): ' + str(fibo_1000))
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1000)
                                        else:  # inserted
                                            print('익절 적용 X')
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                                else:  # inserted
                                    if Trade_Level['A'] == 1:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        start_time = int(time.time())
                                        while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if stop_autotrade:
                                                return
                                            if elapsed_time > 60:
                                                print('재판단')
                                                break
                                        else:  # inserted
                                            print('주문 진행 중...')
                                            print('『황금비율』 숏 포지션 예상 진입 구간(0.236%): ' + str(fibo_0764))
                                            print('『황금비율』 숏 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                            print('『황금비율』 숏 포지션 예상 손절 구간(0%): ' + str(fibo_1000))
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1000)
                                            else:  # inserted
                                                print('익절 적용 X')
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                                    else:  # inserted
                                        if Trade_Level['B'] == 1:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            start_time = int(time.time())
                                            while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if stop_autotrade:
                                                    return
                                                if elapsed_time > 60:
                                                    print('재판단')
                                                    break
                                            else:  # inserted
                                                print('주문 진행 중...')
                                                print('『황금비율』 숏 포지션 예상 진입 구간(0.236%): ' + str(fibo_0764))
                                                print('『황금비율』 숏 포지션 예상 익절 구간(0.618%): ' + str(fibo_0382))
                                                print('『황금비율』 숏 포지션 예상 손절 구간(0%): ' + str(fibo_1000))
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1000)
                                                else:  # inserted
                                                    print('익절 적용 X')
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1000)
                                        else:  # inserted
                                            if Trade_Level['G'] == 1:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                start_time = int(time.time())
                                                while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if stop_autotrade:
                                                        return
                                                    if elapsed_time > 60:
                                                        print('재판단')
                                                        break
                                                else:  # inserted
                                                    print('주문 진행 중...')
                                                    print('『황금비율』 숏 포지션 예상 진입 구간(0.13%): ' + str(fibo_0870))
                                                    print('『황금비율』 숏 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                                    print('『황금비율』 숏 포지션 예상 손절 구간(-0.13%): ' + str(fibo_1130))
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1130)
                                                    else:  # inserted
                                                        print('익절 적용 X')
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                                            else:  # inserted
                                                if Trade_Level['H'] == 1:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    start_time = int(time.time())
                                                    while current_price > fibo_0870 + fibo_error or current_price < fibo_0870 - fibo_error2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if stop_autotrade:
                                                            return
                                                        if elapsed_time > 60:
                                                            print('재판단')
                                                            break
                                                    else:  # inserted
                                                        print('주문 진행 중...')
                                                        print('『황금비율』 숏 포지션 예상 진입 구간(0.13%): ' + str(fibo_0870))
                                                        print('『황금비율』 숏 포지션 예상 익절 구간1(0.618%): ' + str(fibo_0382))
                                                        print('『황금비율』 숏 포지션 예상 손절 구간(-0.13%): ' + str(fibo_1130))
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1130)
                                                        else:  # inserted
                                                            print('익절 적용 X')
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0870, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                                                else:  # inserted
                                                    if Trade_Level['C'] == 1:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        start_time = int(time.time())
                                                        while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = int(time.time()) - start_time
                                                            if stop_autotrade:
                                                                return
                                                            if elapsed_time > 60:
                                                                print('재판단')
                                                                break
                                                        else:  # inserted
                                                            print('주문 진행 중...')
                                                            print('『황금비율』 숏 포지션 예상 진입 구간(0.236%): ' + str(fibo_0764))
                                                            print('『황금비율』 숏 포지션 예상 익절 구간(0.5%): ' + str(fibo_0500))
                                                            print('『황금비율』 숏 포지션 예상 손절 구간(-0.13%): ' + str(fibo_1130))
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0500, presetStopLossPrice=fibo_1130)
                                                            else:  # inserted
                                                                print('익절 적용 X')
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                                                    else:  # inserted
                                                        if Trade_Level['D'] == 1:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            start_time = int(time.time())
                                                            while current_price > fibo_0764 + fibo_error or current_price < fibo_0764 - fibo_error2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = int(time.time()) - start_time
                                                                if stop_autotrade:
                                                                    return
                                                                if elapsed_time > 60:
                                                                    print('재판단')
                                                                    break
                                                            else:  # inserted
                                                                print('주문 진행 중...')
                                                                print('『황금비율』 숏 포지션 예상 진입 구간(0.236%): ' + str(fibo_0764))
                                                                print('『황금비율』 숏 포지션 예상 익절 구간(0.618%): ' + str(fibo_0382))
                                                                print('『황금비율』 숏 포지션 예상 손절 구간(-0.13%): ' + str(fibo_1130))
                                                                if TP_excute == True:
                                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_0382, presetStopLossPrice=fibo_1130)
                                                                else:  # inserted
                                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0764, marginCoin='USDT', clientOrderId=random_string('buy'), presetStopLossPrice=fibo_1130)
                            if result!= '아직 주문 없음':
                                print(f'주문 결과 : {result}0')
                                timestamp = time.time()
                                kst_timezone = pytz.timezone('Asia/Seoul')
                                kst_time = datetime.fromtimestamp(timestamp, kst_timezone)
                                formatted_time = kst_time.strftime('%Y-%m-%d %H:%M:%S')
                                print(f'주문 요청 시간 (한국 시각): {formatted_time}0')
                        else:  # inserted
                            print('버스 떠남')
                else:  # inserted
                    print('USDT 잔액 부족')
                    print('주문 가능한 금액(USDT) : ', USDT_balance)
                    print('주문 가능한 금액이 0.001BTC를 만족하는 지 확인해 주세요')
    except Exception as e:
        if '40762' in str(e):
            print('주문 금액이 잔액을 초과합니다. 잔액을 확인하고 주문 금액을 조정하세요.')
        print(f'주문 실행 실패: {e}0')
        print(f'숏 주문 실행 실패: {e}0')
    finally:  # inserted
        pass  # postinserted
    order_flag = True
    order_flag = True
    order_flag = True
    order_flag = True

def open_short_extension(bitget, trade_size):
    global order_flag  # inserted
    start_time = 0
    result = '아직 주문 없음'
    formatted_time = 0
    if stop_autotrade:
        return
    try:
        try:
            position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
            if not isinstance(position_data, list) or leave_bus == True:
                pass
            else:  # inserted
                if order_flag:
                    order_flag = False
                    USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
                    if USDT_balance > 67:
                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                        if fibo_0000 == 0 or fibo_0130 == 0 or fibo_0236 == 0 or (fibo_0382 == 0) or (fibo_0500 == 0) or (fibo_0618 == 0):
                            pass
                        else:  # inserted
                            if current_price < fibo_0382:
                                if Trade_Level['A'] == 1:
                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                    start_time = int(time.time())
                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        elapsed_time = int(time.time()) - start_time
                                        if stop_autotrade:
                                            return
                                        if elapsed_time > 60:
                                            break
                                    else:  # inserted
                                        print('주문 진행 중...')
                                        print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                        print('『황금비율』 숏 포지션 예상 익절 구간(1.13%): ' + str(fibo_Minus013))
                                        print('『황금비율』 숏 포지션 예상 손절 구간(0.618%): ' + str(fibo_0382))
                                        if TP_excute == True:
                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus013, presetStopLossPrice=fibo_0382)
                                else:  # inserted
                                    if Trade_Level['B'] == 1:
                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                        start_time = int(time.time())
                                        while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            elapsed_time = int(time.time()) - start_time
                                            if stop_autotrade:
                                                return
                                            if elapsed_time > 60:
                                                break
                                        else:  # inserted
                                            print('주문 진행 중...')
                                            print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                            print('『황금비율』 숏 포지션 예상 익절 구간(1.13%): ' + str(fibo_Minus013))
                                            print('『황금비율』 숏 포지션 예상 손절 구간(0.5%): ' + str(fibo_0500))
                                            if TP_excute == True:
                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus013, presetStopLossPrice=fibo_0500)
                                    else:  # inserted
                                        if Trade_Level['C'] == 1:
                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                            start_time = int(time.time())
                                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                elapsed_time = int(time.time()) - start_time
                                                if stop_autotrade:
                                                    return
                                                if elapsed_time > 60:
                                                    break
                                            else:  # inserted
                                                print('주문 진행 중...')
                                                print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                print('『황금비율』 숏 포지션 예상 익절 구간(1.3%): ' + str(fibo_Minus013))
                                                print('『황금비율』 숏 포지션 예상 손절 구간(0.382%): ' + str(fibo_0618))
                                                if TP_excute == True:
                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus013, presetStopLossPrice=fibo_0618)
                                        else:  # inserted
                                            if Trade_Level['D'] == 1:
                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                start_time = int(time.time())
                                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    elapsed_time = int(time.time()) - start_time
                                                    if stop_autotrade:
                                                        return
                                                    if elapsed_time > 60:
                                                        break
                                                else:  # inserted
                                                    print('주문 진행 중...')
                                                    print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                    print('『황금비율』 숏 포지션 예상 익절 구간(1.236%): ' + str(fibo_Minus0236))
                                                    print('『황금비율』 숏 포지션 예상 손절 구간(0.618%): ' + str(fibo_0382))
                                                    if TP_excute == True:
                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0236, presetStopLossPrice=fibo_0382)
                                            else:  # inserted
                                                if Trade_Level['E'] == 1:
                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                    start_time = int(time.time())
                                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        elapsed_time = int(time.time()) - start_time
                                                        if stop_autotrade:
                                                            return
                                                        if elapsed_time > 60:
                                                            break
                                                    else:  # inserted
                                                        print('주문 진행 중...')
                                                        print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                        print('『황금비율』 숏 포지션 예상 익절 구간(1.236%): ' + str(fibo_Minus0236))
                                                        print('『황금비율』 숏 포지션 예상 손절 구간(0.5%): ' + str(fibo_0500))
                                                        if TP_excute == True:
                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0236, presetStopLossPrice=fibo_0500)
                                                else:  # inserted
                                                    if Trade_Level['F'] == 1:
                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                        start_time = int(time.time())
                                                        while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            elapsed_time = int(time.time()) - start_time
                                                            if stop_autotrade:
                                                                return
                                                            if elapsed_time > 60:
                                                                break
                                                        else:  # inserted
                                                            print('주문 진행 중...')
                                                            print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                            print('『황금비율』 숏 포지션 예상 익절 구간(1.236%): ' + str(fibo_Minus0236))
                                                            print('『황금비율』 숏 포지션 예상 손절 구간(0.382%): ' + str(fibo_0618))
                                                            if TP_excute == True:
                                                                result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0236, presetStopLossPrice=fibo_0618)
                                                    else:  # inserted
                                                        if Trade_Level['G'] == 1:
                                                            current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                            start_time = int(time.time())
                                                            while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                elapsed_time = int(time.time()) - start_time
                                                                if stop_autotrade:
                                                                    return
                                                                if elapsed_time > 60:
                                                                    break
                                                            else:  # inserted
                                                                print('주문 진행 중...')
                                                                print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                                print('『황금비율』 숏 포지션 예상 익절 구간(1.5%): ' + str(fibo_Minus0500))
                                                                print('『황금비율』 숏 포지션 예상 손절 구간(0.618%): ' + str(fibo_0382))
                                                                if TP_excute == True:
                                                                    result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0500, presetStopLossPrice=fibo_0382)
                                                        else:  # inserted
                                                            if Trade_Level['H'] == 1:
                                                                current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                start_time = int(time.time())
                                                                while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                    elapsed_time = int(time.time()) - start_time
                                                                    if stop_autotrade:
                                                                        return
                                                                    if elapsed_time > 60:
                                                                        break
                                                                else:  # inserted
                                                                    print('주문 진행 중...')
                                                                    print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                                    print('『황금비율』 숏 포지션 예상 익절 구간(1.5%): ' + str(fibo_Minus0500))
                                                                    print('『황금비율』 숏 포지션 예상 손절 구간(0.5%): ' + str(fibo_0500))
                                                                    if TP_excute == True:
                                                                        result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0500, presetStopLossPrice=fibo_0500)
                                                            else:  # inserted
                                                                if Trade_Level['I'] == 1:
                                                                    current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                    start_time = int(time.time())
                                                                    while current_price > fibo_0130 + fibo_error or current_price < fibo_0130 - fibo_error * 2:
                                                                        current_price = float(bitget.mix_get_market_price(symbol=bitget_symbol)['data']['markPrice'])
                                                                        elapsed_time = int(time.time()) - start_time
                                                                        if stop_autotrade:
                                                                            return
                                                                        if elapsed_time > 60:
                                                                            break
                                                                    else:  # inserted
                                                                        print('주문 진행 중...')
                                                                        print('『황금비율』 숏 포지션 예상 진입 구간(0.87%): ' + str(fibo_0130))
                                                                        print('『황금비율』 숏 포지션 예상 익절 구간(1.5%): ' + str(fibo_Minus0500))
                                                                        print('『황금비율』 숏 포지션 예상 손절 구간(0.382%): ' + str(fibo_0618))
                                                                        if TP_excute == True:
                                                                            result = bitget.mix_place_order(symbol=bitget_symbol, side='open_short', orderType='market', size=trade_size, price=fibo_0130, marginCoin='USDT', clientOrderId=random_string('buy'), presetTakeProfitPrice=fibo_Minus0500, presetStopLossPrice=fibo_0618)
                                if result!= '아직 주문 없음':
                                    print(f'주문 결과 : {result}0')
                                    timestamp = time.time()
                                    kst_timezone = pytz.timezone('Asia/Seoul')
                                    kst_time = datetime.fromtimestamp(timestamp, kst_timezone)
                                    formatted_time = kst_time.strftime('%Y-%m-%d %H:%M:%S')
                                    print(f'주문 요청 시간 (한국 시각): {formatted_time}0')
                                pass
                    else:  # inserted
                        print('USDT 잔액 부족')
                        print('주문 가능한 금액(USDT) : ', USDT_balance)
                        print('주문 가능한 금액이 0.001BTC를 만족하는 지 확인해 주세요')
        except Exception as e:
            if '40762' in str(e):
                print('주문 금액이 잔액을 초과합니다. 잔액을 확인하고 주문 금액을 조정하세요.')
            print(f'숏 주문 실행 실패: {e}0')
    finally:  # inserted
        order_flag = True
        order_flag = True
        order_flag = True
        order_flag = True
        order_flag = True

def close_short(bitget, trade_size):
    print('BTC 숏 포지션 커버 시도 중...')
    try:
        position_data = bitget.mix_get_single_position(symbol=bitget_symbol, marginCoin='USDT')['data']
        if isinstance(position_data, list):
            if position_data and position_data[0]['holdSide'] == 'short':
                result = bitget.mix_place_order(symbol=bitget_symbol, side='close_short', orderType='market', size=trade_size, marginCoin='USDT', clientOrderId=random_string('cover'))
                print(f'커버 주문 성공: {result}0')
        print('닫을 숏 포지션이 없습니다')
    except Exception as e:
        print(f'커버 주문 실행 실패: {e}0')

def make_decision_and_execute(bitget, trade_size, window):
    global is_task_running  # inserted
    if stop_autotrade:
        print('프로그램 중지 중...')
        scheduler.remove_all_jobs()
        print('프로그램 중지 완료')
    if is_task_running:
        return
    is_task_running = True
    try:
        data_pd, _, up, low = fetch_and_prepare_data(bitget)
        advice = analyze_data(bitget, data_pd, up, low)
        USDT_balance = float(bitget.mix_get_accounts(productType='umcbl')['data'][0]['available'])
        if not extension:
            if advice == 'open long':
                if excute_only_short == True:
                    break
                if USDT_balance > 67:
                    open_long(bitget, trade_size)
                else:  # inserted
                    print('USDT 잔액 부족')
            else:  # inserted
                if advice == 'close long':
                    close_long(bitget, trade_size)
                else:  # inserted
                    if advice == 'open short':
                        if excute_only_long == True:
                            break
                        if USDT_balance > 67:
                            open_short(bitget, trade_size)
                        else:  # inserted
                            print('USDT 잔액 부족')
                    else:  # inserted
                        if advice == 'close short':
                            close_short(bitget, trade_size)
        else:  # inserted
            if extension:
                if advice == 'open long extension':
                    if excute_only_short == True:
                        pass
                    else:  # inserted
                        if USDT_balance > 67:
                            open_long_extension(bitget, trade_size)
                        else:  # inserted
                            print('USDT 잔액 부족')
                else:  # inserted
                    if advice == 'open short extension':
                        if excute_only_long == True:
                            pass
                        else:  # inserted
                            if USDT_balance > 67:
                                open_short_extension(bitget, trade_size)
                            else:  # inserted
                                print('USDT 잔액 부족')
        pass
    except Exception as e:
        print('포지션 결정 보류')
    finally:  # inserted
        is_task_running = False

def show_error_message(error_message):
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle('오류 발생')
    msg_box.setText('예기치 못한 오류로 프로그램이 종료되었습니다.')
    msg_box.setInformativeText(error_message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

def schedule_autotrade(bitget, trade_size, window):
    global excute_only_long  # inserted
    global excute_only_short  # inserted
    global scheduler  # inserted
    scheduler = BackgroundScheduler()
    if scheduler is None:
        scheduler = BackgroundScheduler()
    if not scheduler.running:
        if excute_only_long and excute_only_short:
            excute_only_long = False
            excute_only_short = False
        try:
            if len(scheduler.get_jobs()) >= 5:
                scheduler.remove_all_jobs()
                print('대기 중인 작업이 많아 모든 작업을 제거했습니다.')
            if not scheduler.get_jobs() and (not stop_autotrade):
                scheduler.add_job(make_decision_and_execute, 'interval', seconds=5, args=[bitget, trade_size, window], max_instances=1, replace_existing=False)
            if stop_autotrade:
                scheduler.remove_all_jobs()
            scheduler.start()
            while not stop_autotrade:
                time.sleep(1)
            scheduler.shutdown(wait=False)
            print('자동매매가 중지되었습니다.')
        except Exception as e:
            error_message = f'자동 매매 스케줄링 실패: {e}0'
            show_error_message(error_message)
            logging.error(f'자동 매매 스케줄링 실패: {e}\n{traceback.format_exc()}0')

def main():
    try:
        app = QApplication(sys.argv)
        suppress_qt_warnings(app)
        window = MainWindow()
        window.show()
        app.exec_()
    except Exception as e:
        logging.error('Error occurred', exc_info=True)
if __name__ == '__main__':
    main()