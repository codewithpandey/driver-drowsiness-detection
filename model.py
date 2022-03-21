import cv2 as cv
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras import models

class Model:
    
    def __init__(self):
        self.eye_model = models.load_model("eye-model.h5")
        self.yawn_model = models.load_model("yawn-model.h5")

        self.face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
    
    def image_segmentation(self):
        # img = Image.open('frames/frame.jpg')
        # img = img.resize((600, 400), Image.ANTIALIAS)
        # img.save('frames/face.jpg', 'JPEG', quality=95)

        img = cv.imread('frames/face.jpg')

        # face = self.face_cascade.detectMultiScale(img, 1.5, 1)

        # for (fx, fy, fw, fh) in face:

        #     if fx:
        #         print("Found a FACE")

        #     face_found = cv.rectangle(img, (fx, fy), (fx + fw, fy + fh), (255, 0, 0), 2) # def rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
        #     # cv.putText(img,'Face',(fx-fw,fy-fh), font, 0.5, (0,255,255), 2, cv.LINE_AA)

        #     # roi_gray = img[fy:fy+fw, fx:fx+fw]
        #     roi_color = img[fy:fy+fw, fx:fx+fw]

        eyes = self.eye_cascade.detectMultiScale(img, 1.5, 2)

        for (ex, ey, ew, eh) in eyes:

            if ex:
                print("Found an EYE")

            eye_found = cv.rectangle(img, (ex, ey), (ex + ew, ey + ew), (0, 255, 0), 1)

            eyes = img[ey:ey+ew, ex:ex+ew]
            # cv.imshow('Eyes', eyes)
            cv.imwrite('frames/eye.jpg', eyes)

            # img = Image.open('frames/eye.jpg')
            # img = img.resize((100, 100), Image.ANTIALIAS)
            # os.remove('frames/eye100.jpg')
            # img.save('frames/eye100.jpg', 'JPEG', quality=95)

        # # converting to gray, blur it, and find edges
        # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # gray = cv.GaussianBlur(gray, (5,5), 0)
        # edged = cv.Canny(gray, 75, 200) # image, threshold1, threshold2


        # cv.imshow('Image', img)
        # cv.waitKey()

    def predict(self):

        self.image_segmentation()
        # For Eyes
        class_names = ['closed', 'open']
        img = cv.imread('frames/eye.jpg')
        dimensions = (100, 100)
        img = cv.resize(img, dimensions)
        # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = tf.keras.applications.vgg16.preprocess_input(img)
        prediction = self.eye_model.predict(np.array([img]))
        index = np.argmax(prediction) # Getting the argument of maximum value(the greatest of all values generated by the neurons)

        eye_prediction = class_names[index]
        print(eye_prediction)
        if eye_prediction == "closed":
            return "drowsy"
        else:
            pass

        # For Eyes
        class_names = ['no_yawn', 'yawn']
        img = cv.imread('frames/face.jpg')
        dimensions = (600, 400)
        img = cv.resize(img, dimensions)
        # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img = tf.keras.applications.vgg16.preprocess_input(img)
        prediction = self.yawn_model.predict(np.array([img]))
        index = np.argmax(prediction) # Getting the argument of maximum value(the greatest of all values generated by the neurons)

        yawn_prediction = class_names[index]
        print(yawn_prediction)
        if yawn_prediction == "yawn":
            return "drowsy"
        else:
            return "attentive"
        
        # returning status according to the prediction
        if flag:
            return "drowsy"
        else:
            return "attentive"