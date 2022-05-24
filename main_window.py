from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import QTimer
import cv2
import os
import face_recognition as fr
import os
from ui_gui import *
import pandas as pd


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.camnum = 2
        self.match = False

        #List of previously stored data
        self.encoded_data = {"Name":[],"Coords":[]}
        self.detected_people = []
        self.detected_time = []


        #Changing stylesheet
        with open("theme.qss", "r") as f:
            stylesheet  = f.read()
            self.setStyleSheet(stylesheet)

        #Getting camera number from a text tile
        try:
            with open("cam_num.txt", "r") as f:
                num  = f.read()
                num = int(num)
                self.camnum = num
        except:
            self.camnum = 2



        #Run the camera 
        self.timer = QTimer()
        self.timer.timeout.connect(self.showcam)
        self.controlTimer()

        self.ui.download_btn.clicked.connect(lambda:self.Update_enc())
        self.ui.start_btn.clicked.connect(lambda:self.start_clicked())
        self.ui.clear_btn.clicked.connect(lambda:self.clear_stuff())

    def clear_stuff(self):
        self.ui.listWidget.clear()
        self.detected_people.clear()

    def start_clicked(self):
        
        if self.encoded_data["Name"] == []:
            self.msg("Warning","No data was loaded, please load data first before recognizing",QMessageBox.Warning)
            return

        
        if self.match:
            self.match = False
            self.ui.start_btn.setText("Start")
        else:
            self.match = True
            self.ui.start_btn.setText("Stop")

    def Update_enc(self):
        """
        This section loads all existing pics from images folder in memory (RAM).
        
        It is necessary because it enhances detection and recognition speed.
        """


        i = 0

        current_folder_path = os.getcwd()
        images_folder = current_folder_path+'\\images'
        #Updating the dictionary with new face encodings
        
        self.msg("Notification", "The system will load existing data please wait and don't interact with user interface",QMessageBox.Warning)

        for name in os.listdir(images_folder):
            address2 = images_folder+'/'+name
            sec_pic = cv2.imread(address2)
            sec_encoding = fr.face_encodings(sec_pic)[0]
            self.encoded_data["Name"].append(name)
            print(name)
            self.encoded_data["Coords"].append(sec_encoding)
            i+=1

        self.msg("Notification", "Data loaded successfully, you can start recognition module",QMessageBox.Information)

    def showcam(self):
        """
        This method displays frame of given camera
        
        Camera input is taken by a timer
        """
        #Getting frame from webcam
        _, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if self.match:
            names, times = self.recognize_img(image)
            face_locations = fr.face_locations(image)
            
            #If it detects anyone, store their name in database 
            if names!= [] and face_locations!= []:

                ind = 0
                
                for n in names:

                    if n not in self.detected_people:
                        self.detected_people.append(n)
                        self.detected_time.append(times[ind])
                        
                        
                        self.ui.listWidget.addItem(n+' was detected at '+str(times[ind]))

                print(self.detected_people,self.detected_time)
                df = pd.DataFrame({'RollNumbers':self.detected_people,'Time':self.detected_time})
                df.to_csv('Attendance.csv',index=False)

                for (top, right, bottom, left), name in zip(face_locations, names):
                    # Draw a box around the face
                    cv2.rectangle(image, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(image, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(image, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)

                ind += 1
            
            elif face_locations != [] and names == []:
                nameee = ['Unknown']
                print(nameee)

                for (top, right, bottom, left), name in zip(face_locations, nameee):
                    # Draw a box around the facebandi
                    cv2.rectangle(image, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

                    # Draw a label with a name below the face
                    cv2.rectangle(image, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(image, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)


        #Setting dimensions of the frame
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)


        #Displaying frame in window
        self.ui.cam_lbl.setPixmap(QPixmap.fromImage(qImg))
         
    def controlTimer(self):
        """
        This method takes camera input for display
        """

        # Get camera input and start timer
        self.cap = cv2.VideoCapture(self.camnum)
        self.timer.start(20)
 
    def msg(self, titl,txt,icon):
        """
        This is a simple messagebox function.
        """
        
        msg = QMessageBox()
        msg.setWindowTitle(titl)
        msg.setText(txt)
        msg.setIcon(icon)
        msg.exec_()

    def recognize_img(self, main_pic):
        value = ''
        counter = -1
        list_of_names = []
        list_of_time = []

        target_encoding = fr.face_encodings(main_pic)
        #Declaring a dictionary to hold names and encodings of available data

        for coords in self.encoded_data["Coords"]:
            result = fr.compare_faces(target_encoding, coords, tolerance=0.5)
            counter+=1
            for result_f in result:
                if result_f:
                    value = self.encoded_data["Name"][counter]
                    value = str(value)
                    value = value.replace('.jpg','')
                    value = value.replace('.jpeg','')
                    value = value.replace('.PNG','')

                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    list_of_time.append(current_time)
                    list_of_names.append(value)

            
        return list_of_names, list_of_time

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())