import os
import cv2
import numpy as np
from PyQt5.QtWidgets import *
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("사진 특수 효과")
        self.setGeometry(200, 200, 800, 200)

        pictureButton = QPushButton("사진 업로드", self)
        embossButton = QPushButton("엠보싱", self)
        cartoonButton = QPushButton("카툰", self)
        sketchGrayButton = QPushButton("명암 스케치", self)
        sketchColorButton = QPushButton("색상 스케치", self)
        oilButton = QPushButton("유화", self)
        saveButton = QPushButton("저장하기", self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(["emboss", "cartoon", "sketch(gray)", "sketch(color)", "oilPainting"])
        quitButton = QPushButton("나가기", self)
        self.label = QLabel("환영합니다!", self)
        
        pictureButton.setGeometry(20, 20, 150, 30)
        embossButton.setGeometry(200, 20, 100, 30)
        cartoonButton.setGeometry(310, 20, 100, 30)
        oilButton.setGeometry(420, 20, 100, 30)
        sketchGrayButton.setGeometry(210, 60, 140, 30)
        sketchColorButton.setGeometry(370, 60, 140, 30)
        saveButton.setGeometry(550, 20, 150, 30)
        self.pickCombo.setGeometry(550, 60, 150, 30)
        quitButton.setGeometry(480, 100, 220, 30)
        self.label.setGeometry(30, 95, 450, 30)
        
        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction)
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchGrayButton.clicked.connect(self.sketchGrayFunction)
        sketchColorButton.clicked.connect(self.sketchColorFunction)
        oilButton.clicked.connect(self.oilFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        self.original_filename = None  # 원본 파일 이름 저장
        self.img = None

    def pictureOpenFunction(self):
        fname, _ = QFileDialog.getOpenFileName(self, "사진 읽기", "./")

        if not fname:  # 파일이 선택되지 않은 경우
            return
    
        self.img = cv2.imread(fname)
        if self.img is None:
            self.label.setText("파일을 찾을 수 없습니다.")
            return
                
    
        # 원본 파일 이름 저장
        self.original_filename = os.path.splitext(os.path.basename(fname))[0]  # 확장자 제외
        self.label.setText(f"현재 파일 이름: {self.original_filename}")

        cv2.imshow("Painting", self.img)
        cv2.waitKey(1000)  # 1초 대기
        cv2.destroyAllWindows()  # 창 닫기

    def embossFunction(self):
        if self.img is None:
            self.label.setText("불러온 사진이 없습니다.")
            return
        
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv2.filter2D(gray16, -1, femboss) + 128, 0, 255))

        cv2.imshow("Emboss", self.emboss)
        cv2.waitKey(1000)  # 1초 대기
        cv2.destroyAllWindows()  # 창 닫기

    def cartoonFunction(self):
        if self.img is None:
            self.label.setText("불러온 사진이 없습니다.")
            return
        
        self.cartoon = cv2.stylization(self.img, sigma_s=60, sigma_r=0.45)
        cv2.imshow("Cartoon", self.cartoon)
        cv2.waitKey(1000)  # 1초 대기
        cv2.destroyAllWindows()  # 창 닫기
        

    def sketchGrayFunction(self):
        if self.img is None:
            self.label.setText("불러온 사진이 없습니다.")
            return
        
        self.sketch_gray, _ = cv2.pencilSketch(
            self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02
        )
        cv2.imshow("Pencil sketch(gray)", self.sketch_gray)
        cv2.waitKey(1000)  # 1초 대기
        cv2.destroyAllWindows()  # 창 닫기

    def sketchColorFunction(self):
        if self.img is None:
            self.label.setText("불러온 사진이 없습니다.")
            return
        
        _, self.sketch_color = cv2.pencilSketch(
            self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02
        )
        cv2.imshow("Pencil sketch(color)", self.sketch_color)
        cv2.waitKey(1000)  # 1초 대기
        cv2.destroyAllWindows()  # 창 닫기

    def oilFunction(self):
        if self.img is None:
            self.label.setText("불러온 사진이 없습니다.")
            return
        
        self.oil = cv2.xphoto.oilPainting(self.img, 10, 1, cv2.COLOR_BGR2Lab)
        cv2.imshow("Oil painting", self.oil)
        cv2.waitKey(1000)  # 1초 대기
        cv2.destroyAllWindows()  # 창 닫기

    def saveFunction(self):
        if self.original_filename is None:
            self.label.setText("저장할 이미지가 없습니다.")
            return

        # 현재 선택된 효과에 따라 자동으로 파일 이름 생성
        effect_name = self.pickCombo.currentText()
        new_filename = f"{self.original_filename}_{effect_name}.png"

        # 파일 존재 여부 확인
        if os.path.exists(new_filename):
            self.label.setText("중복된 파일입니다.")
            return

        i = self.pickCombo.currentIndex()
        if i == 0:
            self.embossFunction()
            cv2.imwrite(new_filename, self.emboss)
        elif i == 1:
            self.cartoonFunction()
            cv2.imwrite(new_filename, self.cartoon)
        elif i == 2:
            self.sketchGrayFunction()
            cv2.imwrite(new_filename, self.sketch_gray)
        elif i == 3:
            self.sketchColorFunction()
            cv2.imwrite(new_filename, self.sketch_color)
        elif i == 4:
            self.oilFunction()
            cv2.imwrite(new_filename, self.oil)
        else:
            self.label.setText("저장할 이미지가 없습니다.")

        self.label.setText(f"이미지가 저장되었습니다: {new_filename}")

    def quitFunction(self):
        cv2.destroyAllWindows()
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = SpecialEffect()
    win.show()
    app.exec_()