import cv2 as cv
from colorDetect import GreenDetector ,BlueDetector
from pyfirmata import Arduino,SERVO


def colorChoosing():
    return int(input("Lutfen Takip Etmek Istediginiz Rengi Seciniz 1-yesil 2-mavi : "))

def convertTuple(tup):   
    str = ''
    for item in tup:
        str = str + " " + item
    return str

def coordinatesWrite(frame,coordinates,cx,cy):
    return cv.putText(frame,coordinates,(cx+20,cy+20),cv.QT_FONT_NORMAL,0.5 ,(0,0,255),1)

def drawCircle(frame,cx,cy):
    return cv.circle(frame,(cx,cy),10,(0,0,255),2)

def portChoosing():
    portName = str(input("Arduino Portunu Giriniz ex(COM1) : "))
    return portName.upper()

def servoCoordinates(x,y):
    x=x/30
    x = int(round(x,0))
    y=y/30
    y = int(round(y,0))
    return x,y

#def rotateServo(pin,pin2,angle,angle2):
#    board.digital[pin].write(angle)
#    board.digital[pin2].write(angle2)

gd = GreenDetector()
bd = BlueDetector()

pin = 10
pin2 = 9
#arduinoPort = portChoosing()
#board = Arduino(arduinoPort)
#board.digital[pin].mode = SERVO
#board.digital[pin2].mode = SERVO

colorPicker = colorChoosing()
AxisX,AxisY = 0,0
#GreenDetect
if colorPicker == 1:
    cap = cv.VideoCapture(0,cv.CAP_DSHOW)
    while True:
        ret,frame = cap.read()
        if ret == False:
            break
        coordinate = gd.detect(frame)
        x,y = coordinate
        drawCircle(frame,x,y)
        AxisX ,AxisY = servoCoordinates(x,y)
        print(AxisX,AxisY)
        #rotateServo[pin,pin2,AxisX,AxisY]
        coordinates = convertTuple(("X : " + str(x) ,"Y : " + str(y)))
        coordinatesWrite(frame,coordinates,x,y)     
        cv.imshow("WebCam",frame)
        key = cv.waitKey(1)
        if(key== ord('q')):
            break
#Bluedetect
elif colorPicker == 2:
    cap = cv.VideoCapture(0,cv.CAP_DSHOW)
    while True:
        ret,frame = cap.read()
        if ret == False:
            break
        coordinate = bd.detect(frame)
        x,y = coordinate
        drawCircle(frame,x,y)
        coordinates = convertTuple(("X : " + str(x) ,"Y : " + str(y)))
        coordinatesWrite(frame,coordinates,x,y)     
        cv.imshow("WebCam",frame)
        key = cv.waitKey(1)
        if(key== ord('q')):
            break

cv.destroyAllWindows()