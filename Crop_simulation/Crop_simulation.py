import sys
import random

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from radio_button_widget_class import * # provides radio buto widget
from manual_grow_dialog_class import * #provides manual grow dialog


from wheat_class import *
from potato_class import *


class CropWindow(QMainWindow):
    """this class creates a main widow to observe growth of a simulated crop"""

    #constructor
    def __init__(self):
        super().__init__() # call super constructor
        self.setWindowTitle("Crop Simulator") #window title
        self.create_select_crop_layout()

        self.stacked_layout = QStackedLayout() # create stack
        self.stacked_layout.addWidget(self.select_crop_widget)

        #set the central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)

    def create_select_crop_layout(self):
        #initial layout to select crop tpe

        self.crop_radio_buttons = RadioButtonWidget("Crop Simulation", "Please select a crop",("Wheat","Potato",))
        self.instantiate_button = QPushButton("Create Crop")

        #create layout to hold widgets
        self.initial_layout = QVBoxLayout()
        self.initial_layout.addWidget(self.crop_radio_buttons)
        self.initial_layout.addWidget(self.instantiate_button)

        self.select_crop_widget = QWidget()
        self.select_crop_widget.setLayout(self.initial_layout)


        #connections
        self.instantiate_button.clicked.connect(self.instantiate_crop)
        
    def create_view_crop_layout(self, crop_type):
        #this is the second layout

        self.growth_label = QLabel("Growth")
        self.days_label = QLabel("Days Growing")
        self.status_label = QLabel("Crop Status")

        self.growth_line_edit = QLineEdit()
        self.days_line_edit = QLineEdit()
        self.status_line_edit = QLineEdit()

        self.manual_grow_button = QPushButton("Manually Grow")
        self.automatic_grow_button = QPushButton("Automatically Grow")

        self.grow_grid = QGridLayout()
        self.status_grid = QGridLayout()

        #add label widgets to the status layout
        self.status_grid.addWidget(self.growth_label,0,0)
        self.status_grid.addWidget(self.days_label,1,0)
        self.status_grid.addWidget(self.status_label,2,0)

        #add line edits
        self.status_grid.addWidget(self.growth_line_edit,0,1)
        self.status_grid.addWidget(self.days_line_edit,1,1)
        self.status_grid.addWidget(self.status_line_edit,2,1)

        #add widget/layouts to te grow layout
        self.grow_grid.addLayout(self.status_grid,0,1)
        self.grow_grid.addWidget(self.manual_grow_button,1,0)
        self.grow_grid.addWidget(self.automatic_grow_button,1,1)

        #create a widget to display the laout
        self.view_crop_widget = QWidget()
        self.view_crop_widget.setLayout(self.grow_grid)

        #connections
        self.automatic_grow_button.clicked.connect(self.automatically_grow_crop)
        self.manual_grow_button.clicked.connect(self.manually_grow_crop)
                

    def instantiate_crop(self):
        crop_type = self.crop_radio_buttons.selected_button() # get selected button
        if crop_type == 1:
            self.simulated_crop = Wheat()
        elif crop_type == 2:
            self.simulated_crop = Potato()

        self.create_view_crop_layout(crop_type) #create the view crop growth layout
        self.stacked_layout.addWidget(self.view_crop_widget) # adds to the stack
        self.stacked_layout.setCurrentIndex(1) #changes layout


    def automatically_grow_crop(self):
        for days in range(30):
            light = random.randint(1,10)
            water = random.randint(1,10)
            self.simulated_crop.grow(light,water)
        self.update_crop_view_status()

    def manually_grow_crop(self):
        manual_values_dialog = ManualGrowDialog()
        manual_values_dialog.exec_()#run dialog window
        light, water = manual_values_dialog.values()
        self.simulated_crop.grow(light,water)
        self.update_crop_view_status()


    
    def update_crop_view_status(self):
        crop_status_report = self.simulated_crop.report()

        #update the text fields
        self.growth_line_edit.setText(str(crop_status_report["growth"]))
        self.days_line_edit.setText(str(crop_status_report["days growing"]))
        self.status_line_edit.setText(str(crop_status_report["status"]))
        

        
def main():
    crop_simulation = QApplication(sys.argv) #create new application
    crop_window = CropWindow() #create new instace of main window
    crop_window.show() # make instace visable
    crop_window.raise_() #raise to top of stack
    crop_simulation.exec_() #monitor for events

if __name__ == "__main__":
    main()
    
