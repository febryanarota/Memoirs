# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QGraphicsDropShadowEffect
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt, QDate
# from CatatanHandler.ToDoList.Boundary.FormTDL import *
from CatatanHandler.ToDoList.Entity.ToDoList import *
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
from CatatanHandler.ToDoList.Boundary.todolist import *
from datetime import datetime

# Class ToDoListDisplay
class TDLDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main, tanggal = datetime.now().strftime("%d/%m/%Y")):
        super().__init__()
        self.parent = Main
        self.parent.date = tanggal
        self.showTDLDisplay(tanggal)

    def showTDLDisplay(self, tanggal):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/ToDoList/Boundary/TDLDisplay.ui", self)

        # Sidebar
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        todolist_sidebar = self.findChild(QLabel, "label")
        todolist_sidebar.mousePressEvent = self.navigateToDoList

        harian_sidebar = self.findChild(QLabel, "label_5")
        harian_sidebar.mousePressEvent = self.navigateHarian

        target_sidebar = self.findChild(QLabel, "label_4")
        target_sidebar.mousePressEvent = self.navigateTarget

        syukur_sidebar = self.findChild(QLabel, "label_8")
        syukur_sidebar.mousePressEvent = self.navigateSyukur

        article_sidebar = self.findChild(QLabel, "label_6")
        article_sidebar.mousePressEvent = self.navigateArticle

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.add_button = self.findChild(QPushButton, "pushButton_2")
        self.add_button.clicked.connect(self.addTDL)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.date = self.findChild(QLabel, "label_3")
        self.date.setText(self.parent.date)

        self.calendar = self.findChild(QPushButton, "pushButton_3")
        self.calendar.clicked.connect(self.showCalendar)

        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.scrollArea.verticalScrollBar().setStyleSheet(
        """
        QScrollBar:vertical {
            min-height: 240px;
            width: 13px;
        }

        QScrollBar::handle {
            background: #1C1D22;
            border-radius: 0px;
        }

        QScrollBar::handle:vertical {
            height: 30px;
            width: 5px;
        }
        """)

        todolistController = TDLController()
        listTodo = todolistController.showTDL(tanggal)
        listTodo.sort(key=lambda x: x.getDone())
        # Container Widget       
        self.widget = QWidget()
        
        # Layout of Container Widget
        listTDL_box = QVBoxLayout()
        listTDL_box.setSpacing(40)
    
        for i in range (len(listTodo)):

            TDL_widget = QWidget()
            TDL_widget.setObjectName("Outer")
            TDL_widget.setStyleSheet("""
                #Outer {
                    background-color: white; 
                    border-radius: 20px;
                }
                QWidget {
                    margin-right: 80px;
                }
                #delete {
                    margin-right: 80px;
                }
                #edit{
                        margin-right: 0px;
                    }
                #checklist{
                    margin-right: 0px;
                }
            """)
            TDL_widget.setMinimumSize(1150, 70)
            TDL_widget.setMaximumHeight(70)
            TDL_widget.setMaximumWidth(1920)

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(5)
            shadow.setOffset(4,4)
            TDL_widget.setGraphicsEffect(shadow)

            TDL_box = QHBoxLayout()


            spacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
            TDL_box.addItem(spacer)

            check_icon = QPushButton()
            check_icon.setObjectName("checklist")
            img = QPixmap("./images/checkBox.png")
            if listTodo[i].getDone() == 1:
                img = QPixmap("./images/checked.png")
                TDL_widget.setStyleSheet("""
                    #Outer {
                        background-color: #E5E5E5;; 
                        border-radius: 20px;
                    }
                    QWidget {
                        margin-right: 80px;
                    }
                    #delete {
                        margin-right: 80px;
                    }
                    #edit{
                        margin-right: 0px;
                    }
                    #checklist{
                        margin-right: 0px;
                    }
                """)
            image = img.scaled(30, 30)
            check_icon.setIcon(QIcon(image))
            check_icon.setIconSize(image.size())
            check_icon.setStyleSheet('''QPushButton::hover{
                background-color: rgba(202, 202, 202, 0.5);
                height: 40px;
                width: 30px;
                border-radius: 10px;
            }''')
            check_icon.mousePressEvent = partial(self.checkTDL, todo = listTodo[i])
            TDL_box.addWidget(check_icon)
            
            TDL_content_widget = QWidget()
            TDL_content = QVBoxLayout()
            to_do = QLabel(listTodo[i].getToDo())
            to_do.setFont(QFont("Poppins", 12, QFont.Bold))
            if listTodo[i].getDone() == 1:
                to_do.setStyleSheet("text-decoration: line-through;")

            TDL_content.addWidget(to_do)
            TDL_content_widget.setLayout(TDL_content)

            spacer2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)        
            TDL_box.addWidget(TDL_content_widget)
            TDL_box.addItem(spacer2)

            delete_icon = QLabel()
            delete_icon.setObjectName("delete")
            icon = QPixmap("./images/delete_btn.png")
            icon = icon.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            delete_icon.setPixmap(icon)
            delete_icon.mousePressEvent = partial(self.deleteTDL, deleteToDo = listTodo[i].getToDo(), deleteTanggal = listTodo[i].getTanggal())

            edit_icon = QLabel()
            edit_icon.setObjectName("edit")
            icon = QPixmap("./images/edit_btn.png")
            icon = icon.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            edit_icon.setPixmap(icon)
            edit_icon.setObjectName("edit")
            edit_icon.mousePressEvent = partial(self.editTDL,todo_list_lama = listTodo[i], todo_lama =  listTodo[i].getToDo(), tanggal = listTodo[i].getTanggal())
            
            TDL_box.addWidget(edit_icon)
            TDL_box.addWidget(delete_icon)

            TDL_widget.setLayout(TDL_box)
            listTDL_box.addWidget(TDL_widget)

        self.widget.setLayout(listTDL_box)
        self.scrollArea.setWidget(self.widget)
        spacer3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        listTDL_box.addItem(spacer3)

    def get_done_status(todo_item):
        return todo_item.getDone()      
            
    def addTDL(self, event):
        # Turn off edit mode
        self.parent.editMode = False

        # Clear inputbox
        self.parent.stackedWidget.widget(6).inputbox.setText("")

        # Set form date
        self.parent.stackedWidget.widget(6).date.setText(self.parent.date)

        self.parent.stackedWidget.setCurrentIndex(6)

    def editTDL(self, event, todo_list_lama, todo_lama, tanggal):
        self.parent.stackedWidget.widget(6).inputbox.setText(todo_lama)
        self.parent.stackedWidget.widget(6).date.setText(tanggal)

        self.parent.editMode = True

        self.parent.date = tanggal
        self.parent.todo_list_lama = todo_list_lama

        self.parent.stackedWidget.setCurrentIndex(6)

    def deleteTDL(self, event, deleteToDo, deleteTanggal):
        TDLController().deleteTDL(deleteToDo, deleteTanggal)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
        self.parent.stackedWidget.insertWidget(5, TDLDisplay(self.parent, deleteTanggal))
        self.parent.stackedWidget.setCurrentIndex(5)

    def checkTDL(self, event, todo):
        if todo.getDone() == 1:
            done = 0
        else:
            done = 1
        TDLController().editTDL(todo, todo.getToDo(), todo.getTanggal(), done)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
        self.parent.stackedWidget.insertWidget(5, TDLDisplay(self.parent, todo.getTanggal()))
        self.parent.stackedWidget.setCurrentIndex(5)

    def showCalendar(self, event):
        self.parent.stackedWidget.setCurrentIndex(14)

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)
        
    def navigateArticle(self, event):
        self.parent.stackedWidget.setCurrentIndex(3)
    
    def navigateToDoList(self, event):
        self.parent.stackedWidget.setCurrentIndex(5)

    def navigateSyukur(self, event):
        self.parent.stackedWidget.setCurrentIndex(7)

    def navigateTarget(self, event):
        self.parent.stackedWidget.setCurrentIndex(9)

    def navigateHarian(self, event):
        self.parent.stackedWidget.widget(13).calendar.setSelectedDate(QDate())
        self.parent.stackedWidget.setCurrentIndex(13)

    def exitEvent(self, event):
        QApplication.quit()