from PyQt5 import QtWidgets, QtCore, QtGui
import json


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setWindowTitle("登录")
        self.setFixedWidth(450)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QFormLayout()  # 表单布局层
        self.main_widget.setLayout(self.main_layout)
        self.choose_btn = QtWidgets.QPushButton('选择文件')  # 用户名输入框
        self.path_input = QtWidgets.QLineEdit()

        self.login_btn = QtWidgets.QPushButton("生成json文件")  # 登录按钮
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.main_layout.addRow(self.tr("&文件："), self.choose_btn)
        self.main_layout.addRow(self.tr("&上传路径："), self.path_input)
        self.main_layout.addRow(self.login_btn)
        self.setCentralWidget(self.main_widget)
        self.login_btn.setShortcut("Return")
        self.choose_btn.clicked.connect(self.choose_file)
        self.login_btn.clicked.connect(self.make_json)# 绑定登录按钮点击信号

        self.upload_list = []

    def choose_file(self):
        l = QtWidgets.QFileDialog.getOpenFileNames(self, '选择图片', directory='D:\suxss.github.io\photos\photoalbum')
        self.upload_list = l[0]

    # os.system(f'b2 upload-file photosalbum --quiet {item} {name} > D:\Python\PythonProjects\\adbtest\logs.txt')
    def make_json(self):
        path = self.path_input.text().strip()
        dic = {path: self.upload_list}
        with open('uploadlist.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    demo = LoginWindow()
    demo.show()
    sys.exit(app.exec_())