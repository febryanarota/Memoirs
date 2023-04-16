# Importing libraries and MainMenu Class to test
import sys
sys.path.append('./src/MainMenu')
import MainMenu
import pytest
from PyQt5 import QtCore, QtWidgets

# Create test app
@pytest.fixture
def test(qtbot):
    # Construct app
    test_app = MainMenu.MainMenu("")
    
    # Add widget
    qtbot.addWidget(test_app)

    return test_app

def test_label_todolist(test):
    # Testing Label To Do List
    assert test.todolist_menu.text() == "To Do List"

def test_label_catatanharian(test):
    # Testing Label Daily Plan
    assert test.harian_menu.text() == "Daily Plan"

def test_label_catatantarget(test):
    # Testing Label Target
    assert test.target_menu.text() == "Target"

def test_label_catatansyukur(test):
    # Testing Label Gratitude
    assert test.syukur_menu.text() == "Gratitude"

def test_label_artikel(test):
    # Testing Label Article
    assert test.article_menu.text() == "Article"

def test_quit_application(test, qtbot):
    # Testing Click Exit Button on Sidebar
    qtbot.mouseClick(test.exit, QtCore.Qt.LeftButton)

    # Wait for the application to quit
    qtbot.waitSignal(QtWidgets.qApp.aboutToQuit)

    # Assert that the application has quit
    assert QtWidgets.QApplication.instance().quitOnLastWindowClosed()
