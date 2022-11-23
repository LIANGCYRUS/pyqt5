from PyQt5.Qt import *
import sys
import pymysql
from PyQt5 import QtCore


class MyQWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('订单管理系统')
        self.resize(1300,850)

        # 创建一个垂直的布局，在这个布局下的子布局都会垂直展现
        Vlayout = QVBoxLayout()
        Vlayout.addLayout(self.default_btn())
        Vlayout.addLayout(self.default_form())
        Vlayout.addLayout(self.default_table())
        Vlayout.addLayout(self.default_setting())

        # 应用垂直布局
        self.setLayout(Vlayout)

    #功能函数(提交,上传等等)
    def default_btn(self):

        btn_layout = QHBoxLayout() # 设置一个水平form的layout，让里面的widget都水平配置

        time_lable = QLabel()
        time_lable.setText('数据库数据最新时间：YYYY-MM-DD HH:MM:SS')
        btn_layout.addWidget(time_lable)

        btn_layout.addStretch()

        btn_upload = QPushButton('上传/更新订单')
        btn_upload.setMinimumWidth(150)
        btn_layout.addWidget(btn_upload)

        btn_done = QPushButton('完结订单上传')
        btn_done.setMinimumWidth(150)
        btn_layout.addWidget(btn_done)

        return btn_layout

    # 表格函数
    def default_table(self):

        table_layout = QVBoxLayout() # 设置一个table的layout

        table_widget = QTableWidget(0, 13)  # 这是0行16列的表单
        table_widget.setMinimumHeight(650)  # 这是该表单的高度为650

        # 表头设定
        table_header = [
            {'title': 'Partner_transaction_id', },
            {'title': 'Transaction_id', },
            {'title': 'Amount', },
            {'title': 'Rmb_amount', },
            {'title': 'Fee', },
            {'title': 'Refund', },
            {'title': 'Settlement', },
            {'title': 'Rmb_settlement', },
            {'title': 'Currency', },
            {'title': 'Rate', },
            {'title': 'Payment_time', },
            {'title': 'Settlement_time', },
            {'title': 'Type', },
        ]
        # 使用循环将表头应用到表单上
        for idx, info in enumerate(table_header):
            item = QTableWidgetItem()
            item.setText(info['title'])
            table_widget.setHorizontalHeaderItem(idx, item)  # 使用index进行对列明赋值，但是不能直接写字符串，所以先用 QTableWidgetItem 进行设定。
            # table_widget.setColumnWidth(idx,200)

        # 连接数据库
        conn = pymysql.connect(
            host='a0f07344b6ea.c.methodot.com',
            port=34101,
            user='root',
            password='a8787487##',
            db='completone'
        )
        # 获取所有数据
        cursor = conn.cursor()
        cursor.execute('select * from Alipay')
        result = cursor.fetchall()

        print(result)
        # 关闭数据库
        cursor.close()
        conn.close()
        # 把获取的数据显示出来
        current_row_count = table_widget.rowCount() #获取目前表格有多少行
        # print(current_row_count)
        for row_list in result:
            table_widget.insertRow(current_row_count)

            for i,data in enumerate(row_list):
                cell = QTableWidgetItem(str(data))
                #设定单元格不可修改
                cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                table_widget.setItem(current_row_count,i,cell) #(第几行，第几列，值)

            current_row_count += 1


        table_layout.addWidget(table_widget) # 将做好的Widget放到layout上

        return table_layout


    #表单函数(搜索功能)
    def default_form(self):

        form_layout = QHBoxLayout() # 设置一个水平form的layout，让里面的widget都水平配置

        # 输入框
        search_order = QLineEdit()
        search_order.setPlaceholderText('请输入订单号/交易单号')
        search_order.setMinimumHeight(25)
        form_layout.addWidget(search_order)


        def showMessage(self):
            print(search_order.text())
            # 获取到输入的查询文档
            se_num = search_order.text()
            # 连接数据库

            # 连接数据库
            conn = pymysql.connect(
                host='a0f07344b6ea.c.methodot.com',
                port=34101,
                user='root',
                password='a8787487##',
                db='completone'
            )
            # 获取所有数据
            cursor = conn.cursor()
            cursor.execute('select * from Alipay where Partner_transaction_id = %s ',[se_num])
            result = cursor.fetchall()

            print(result)
            # 关闭数据库
            cursor.close()
            conn.close()


        # 搜索按钮
        btn_search = QPushButton('查询')
        btn_search.clicked.connect(showMessage)


        form_layout.addWidget(btn_search)

        return form_layout

    #设置按钮(搜索功能)
    def default_setting(self):

        setting_layout = QHBoxLayout() # 设置一个水平form的layout，让里面的widget都水平配置

        # 搜索按钮
        setting_layout.addStretch()

        btn_setting = QPushButton('设置')

        setting_layout.addWidget(btn_setting)

        return setting_layout

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyQWidget()

    window.show()
    sys.exit(app.exec_())

