#Copyright MicroLearn, Aryan Arora

#This program takes in a csv file

import gui
import sys

#TODO make popups to show progress

def main():
    #to open gui

    app = gui.QApplication(sys.argv)
    ex = gui.App()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()