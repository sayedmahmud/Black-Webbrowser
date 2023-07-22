#!/usr/bin/python3
# Made By Sina Meysami (Black-Software)
# Black-Webbrowser v2.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from colorama import Fore,Back,Style
import sys,platform,os,datetime,webbrowser
black_webbrowser_version = "Black-Webbrowser v2.0"
help_arg = """
Black-Webbrowser v2.0 Argument:
    
    --help = help
    --url <URL> = Open Website
    --version = Version
    --start = start

"""
css_code = """
"""
banner = f"""{Fore.GREEN}  ____  _            _     __          __  _     _                                     
 |  _ \| |          | |    \ \        / / | |   | |                                     {Fore.RED}v2.0{Fore.GREEN}
 | |_) | | __ _  ___| | __  \ \  /\  / /__| |__ | |__  _ __ _____      _____  ___ _ __ 
 |  _ <| |/ _` |/ __| |/ /   \ \/  \/ / _ \ '_ \| '_ \| '__/ _ \ \ /\ / / __|/ _ \ '__|
 | |_) | | (_| | (__|   <     \  /\  /  __/ |_) | |_) | | | (_) \ V  V /\__ \  __/ |   
 |____/|_|\__,_|\___|_|\_\     \/  \/ \___|_.__/|_.__/|_|  \___/ \_/\_/ |___/\___|_|   
                                                                                    {Fore.WHITE}                                                                                      
"""
width = 1200
height = 700
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.start_banner()
        self.Main()
    def start_banner(self):
        self.title()
        self.cls()
        time = datetime.datetime.now()
        time = time.strftime("%Y/%m/%d %H:%M:%S")
        print(banner)
        print(f"{Fore.GREEN}Start Black-Webbrowser v2.0{Fore.WHITE}\n")
        print(f"{Fore.WHITE}Start At: {Fore.GREEN}{time}{Fore.WHITE}\n\n")
    def title(self):
        if platform.system() == "Windows":
            os.system("title Black-Webbrowser")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("xtitle Black-Webbrowser")
        else:
            sys.exit()
    def cls(self):
        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            os.system("clear")
        else:
            sys.exit()
    def Main(self):
        self.home_url = open("./Data/home_page.txt","r").read()
        self.setStyleSheet(css_code)
        self.setWindowTitle("Black-Webbrowser")
        self.setWindowIcon(QIcon("./Icon/black-webbrowser-icon.ico"))
        self.setGeometry(500,150,width,height)
        #self.setFixedSize(width,height)
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.home_url))
        self.browser.urlChanged.connect(self.url_change)
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        
        menu = QMenuBar(self)
        self.menu_file = menu.addMenu("&Menu")
        self.menu_file.addAction("New Window",self.new_window)
        self.menu_file.addSeparator()
        self.menu_file.addAction("History",self.history)
        #self.history_menu = self.menu_file.addMenu("History")
        self.menu_file.addAction("Downloads",self.downloads)
        self.menu_file.addAction("Bookmarks",self.bookmark)
        self.menu_file.addSeparator()
        self.help_menu = self.menu_file.addMenu("Help")
        self.menu_file.addSeparator()

        self.setting_menu = self.menu_file.addMenu("Setting")
        self.menu_file.addSeparator()
        self.menu_file.addAction("Quit",self.close)
        self.theme_menu = self.setting_menu.addMenu("Theme")
        self.theme_menu.addAction("Light",self.light)
        self.theme_menu.addAction("Dark",self.dark)
        self.theme_menu.addAction("Matrix",self.matrix)
        self.window_size = self.setting_menu.addMenu("Window")
        self.window_size.addAction("Fullscreen",self.showFullScreen)
        self.window_size.addAction("Normal",self.showNormal)
        self.window_size.addAction("Minimize",self.showMinimized)
        self.setting_menu.addAction("Setting",self.setting)
        self.help_menu.addAction("Help",self.help_)
        self.help_menu.addAction("About",self.about)
        self.help_menu.addSeparator()
        self.help_menu.addAction("License",self.license_)
        self.help_menu.addAction("Send Feedback",self.send_feedback)
        
        self.setMenuBar(menu)
        
        toolbar = QToolBar("Menu")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        back_action = QAction("Back",self)
        back_action.setToolTip("Back Page")
        back_action.triggered.connect(self.browser.back)
        toolbar.addAction(back_action)
        forward_action = QAction("Forward",self)
        forward_action.setToolTip("Forward Page")
        forward_action.triggered.connect(self.browser.forward)
        toolbar.addAction(forward_action)
        reload_action = QAction("Reload",self)
        reload_action.setToolTip("Reload Page")
        reload_action.triggered.connect(self.browser.reload)
        toolbar.addAction(reload_action)
        home_action = QAction("Home",self)
        home_action.setToolTip("Home Page")
        home_action.triggered.connect(self.home)
        toolbar.addAction(home_action)
        
        
        self.line = QLineEdit(self)
        self.line.setPlaceholderText("Search Or Type URL...")
        self.line.setClearButtonEnabled(True)
        self.line.setDragEnabled(True)
        self.line.setStyleSheet("""
QLineEdit {
    border: 3px solid lightgray;
    border-radius: 5px;    
}
QLineEdit:hover {
    border-color: #3333ff;    
}
""")
        self.line.returnPressed.connect(self.search_link)
        toolbar.addWidget(self.line)
        stop_action = QAction("Stop",self)
        stop_action.triggered.connect(self.browser.stop)
        stop_action.setToolTip("Stop")
        toolbar.addAction(stop_action)
        star_action = QAction("Star",self)
        star_action.setToolTip("Star")
        star_action.triggered.connect(self.star)
        
        toolbar.addAction(star_action)
        
        #self.get_history()
        self.key_shortcut()
        
        self.set_status()
        theme_f = open("./Data/theme.txt","r").read()
        if theme_f == "light":
            self.light()
        elif theme_f == "dark":
            self.dark()
        elif theme_f == "matrix":
            self.matrix()
        print(f"Theme: {theme_f}")
    def star(self):
        
        star_ = self.line.text()
        print(star_)
        f = open("./Data/bookmark.txt","a")
        f.write(f"{str(star_)}\n\n")
        f.close()
        
        """
        f_ = open("./Data/bookmark.txt","r")
        for i in f_.readlines():          
            self.star_menu.addAction(i,lambda: self.search(i))
        f_.close()
        """
    def print_page(self):
        pass
    """
    def get_history(self):
        
        history_file = open("./Data/history.txt","r")
        for i in range(10):
            for self.link in history_file.readlines():
                print(self.link)
                self.history_menu.addAction(self.link,lambda: self.search_history(self.link))
                
    def search_history(self,link):
        print(link)
        #self.browser.setUrl(QUrl(str(self.link)))"""
    def light(self):
        theme_f = open("./Data/theme.txt","w")
        theme_f.write("light")
        theme_f.close()
        css_f = open("./Form/Css/light.css","r").read()
        self.setStyleSheet(css_f)

    def dark(self):
        theme_f = open("./Data/theme.txt","w")
        theme_f.write("dark")
        theme_f.close()
        css_f = open("./Form/Css/dark.css","r").read()
        self.setStyleSheet(css_f)
    def matrix(self):
        theme_f = open("./Data/theme.txt","w")
        theme_f.write("matrix")
        theme_f.close()
        css_f = open("./Form/Css/matrix.css","r").read()
        self.setStyleSheet(css_f)
    def setting(self):
        
        dlg = QDialog(self)
        loadUi("./Form/setting-ui.ui",dlg)
        dlg.themes.addItems(["Light","Dark","Matrix"])
        dlg.themes.currentIndexChanged.connect(self.selectionchange)
        dlg.font_btn.clicked.connect(self.set_font)
        dlg.license_btn.clicked.connect(self.license_)
        dlg.open_data_btn.clicked.connect(self.open_data)
        dlg.history_btn.clicked.connect(self.history)
        dlg.download_btn.clicked.connect(self.downloads)
        dlg.bookmark_btn.clicked.connect(self.bookmark)
        dlg.source_btn.clicked.connect(self.source)
        dlg.about_btn.clicked.connect(self.about)
        dlg.help_btn.clicked.connect(self.help_)
        dlg.exit_btn.clicked.connect(dlg.close)
        dlg.send_feedback.clicked.connect(self.send_feedback)
        
        dlg.home_line.setText(self.home_url)
        dlg.ok_p_btn.clicked.connect(self.change_home_url)
        self.home_line = dlg.home_line
        
        dlg.ok_p_btn_2.clicked.connect(self.save_user)
        self.user_name = dlg.user_line
        print(self.user_name)
        
        dlg.instagram_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://instagram.com/sina.coder")))
        dlg.twitter_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://twitter.com/Sinameysami")))
        dlg.facebook_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://instagram.com/Sinameysami")))
        dlg.github_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://github.com/mrprogrammer2938")))
        dlg.telegram_btn.clicked.connect(lambda: self.browser.setUrl(QUrl("https://instagram.com/sina_pythonn")))
        dlg.send_emailbtn.clicked.connect(lambda: self.browser.setUrl(QUrl("mailto:mrprogrammer2938@gmail.com")))
        dlg.fullscreen_btn.clicked.connect(self.showFullScreen)
        dlg.normal_btn.clicked.connect(self.showNormal)
        dlg.minimize_btn.clicked.connect(self.showMinimized)
        
        rev = dlg.exec_()
    def save_user(self):
        f = open("./Data/username.txt","w")
        f.write(self.user_name.text())
        f.close()
        
    def change_home_url(self):
        
        self.home_url = self.home_line.text()
        f = open("./Data/home_page.txt","w")
        f.write(self.home_url)
        f.close()
        
    def open_data(self):
        path_now = os.getcwd()
        webbrowser.open(f"{path_now}\\Data")
    def set_font(self):
        font,i = QFontDialog().getFont()
        if i:
            self.line.setFont(font)
            self.browser.setFont(font)
    def selectionchange(self,i):
        if i == 0:
            self.light()
        elif i == 1:
            self.dark()
        elif i == 2:
            self.matrix()
    def history(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Black-Webbrowser/History")
        dlg.setGeometry(1300,150,400,700)
        dlg.setFixedSize(400,700)
        text = QTextEdit(dlg)
        text.resize(400,700)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",13))
        f = open("./Data/history.txt","r").read()
        text.setText(f)
        
        
        rev = dlg.exec_()
    def downloads(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Black-Webbrowser/Downloads")
        dlg.setGeometry(1300,150,400,700)
        dlg.setFixedSize(400,700)
        text = QTextEdit(dlg)
        text.resize(400,700)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",13))
        f = open("./Data/download.txt","r").read()
        text.setText(f)
        
        
        rev = dlg.exec_()
    def bookmark(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("Black-Webbrowser/Bookmarks")
        dlg.setGeometry(1300,150,400,700)
        dlg.setFixedSize(400,700)
        text = QTextEdit(dlg)
        text.resize(400,700)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",13))
        f = open("./Data/bookmark.txt","r").read()
        text.setText(f)
        
        
        rev = dlg.exec_()
    def new_window(self):
        os.system("python main.py")
    def search_link(self):
        q = QUrl(f"https://www.bing.com/search?q={self.line.text()}")
        q2 = QUrl(self.line.text())
        if q2.scheme() == "https" or q2.scheme() == "http":
            self.browser.setUrl(q2)
        else:
            self.browser.setUrl(q)
            
        
        """
        f = open("./Data/history.txt","a")
        f.write(f"{str(self.line.text())}\n")
        f.close()
        """
    def search(self,link):
        self.browser.setUrl(QUrl(str(link)))
    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(f"Black-Webbrowser - {title}")
        
    def home(self):
        self.browser.setUrl(QUrl(self.home_url))
        
    
    def url_change(self,link):
        self.line.setText(link.toString())
        self.line.setCursorPosition(0)
    def key_shortcut(self):
        exit_key = QShortcut(QKeySequence("Ctrl+Q"), self)
        exit_key.activated.connect(self.close)
        exit_key2 = QShortcut(QKeySequence("Ctrl+E"), self)
        exit_key2.activated.connect(self.close)
        forward_key = QShortcut(QKeySequence("Ctrl+F"), self)
        forward_key.activated.connect(self.browser.forward)
        back_key = QShortcut(QKeySequence("Ctrl+B"), self)
        back_key.activated.connect(self.browser.back)
        reload_key = QShortcut(QKeySequence("Ctrl+R"), self)
        reload_key.activated.connect(self.browser.reload)
        history_key = QShortcut(QKeySequence("Ctrl+H"), self)
        history_key.activated.connect(self.history)
        downloads_key = QShortcut(QKeySequence("Ctrl+D"), self)
        downloads_key.activated.connect(self.downloads)
        about_key = QShortcut(QKeySequence("Ctrl+A"), self)
        about_key.activated.connect(self.about)
    def help_(self):
        help_text = """Black-Webbrowser v2.0
Ctrl+N = Open New Window
Ctrl+H = History
Ctrl+D = Downloads
Ctrl+A = About
Ctrl+R = Refresh (Reload Page)
Ctrl+F = Forward
Ctrl+B = Back
Ctrl+Q = Quit
Ctrl+E = Quit
"""
        dlg = QDialog(self)
        dlg.setWindowTitle("Black-Webbrowser/Help")
        dlg.setGeometry(800,200,500,500)
        dlg.setFixedSize(500,500)
        text = QTextEdit(dlg)
        text.resize(500,500)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",13))
        text.setText(help_text)
        
        
        rev = dlg.exec_()
    def about(self):
        about_text = """Developer: Sina Meysami
Version v2.0
Source: https://github.com/mrprogrammer2938/black-webbrowser
"""
        dlg = QDialog(self)
        dlg.setWindowTitle("Black-Webbrowser/َAbout")
        dlg.setGeometry(800,200,500,500)
        dlg.setFixedSize(500,500)
        text = QTextEdit(dlg)
        text.resize(500,500)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",13))
        text.setText(about_text)
        
        
        rev = dlg.exec_()
    def license_(self):
        license_text = open("LICENSE.txt","r").read()
        dlg = QDialog(self)
        dlg.setWindowTitle("Black-Webbrowser/َLicense")
        dlg.setGeometry(800,200,700,500)
        dlg.setFixedSize(700,500)
        text = QTextEdit(dlg)
        text.resize(700,500)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",13))
        text.setText(license_text)
        
        
        rev = dlg.exec_()
    def send_feedback(self):
        self.browser.setUrl(QUrl("https://github.com/mrprogrammer2938/Black-Webbrowser/issues"))
    def set_status(self):
        x = 100
        for i in range(x):
            status = QStatusBar(self)
            status.setStyleSheet("color: #000;")
            status.showMessage("Black-Webbrowser v1.0")
            self.setStatusBar(status)
            x += 100 
    def source(self):
        webbrowser.open_new_tab("https://github.com/mrprogrammer2938/black-webbrowser")
def main():
    username = open("./Data/username.txt","r").read()
    
    # Black-Webbrowser v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Black-Webbrowser")
    app.setApplicationDisplayName(username)
    app.setApplicationVersion("v2.0")
    window = Window()
    window.show()
    
    sys.exit(app.exec_())
    
def argument():
    try:
        if sys.argv[1] == "--start" or sys.argv[1] == "start":
            main()
        if sys.argv[1] == "--url" or sys.argv[1] == "url":
            url = sys.argv[2]
            webbrowser.open_new_tab(str(url))
        if sys.argv[1] == "--help" or sys.argv[1] == "help":
            print(help_arg)
        if sys.argv[1] == "--version" or sys.argv[1] == "version":
            print(black_webbrowser_version)   
    except (IndexError):
        main()
        
    
if __name__ == "__main__":
    # Black-Webbrowser v2.0
    if platform.system() == "Windows" or platform.system() == "Linux" or platform.system() == "Darwin":
        argument()
        
    else:
        print("Please, Run This Program At Windows, Linux Or MacOS!")
        sys.exit()