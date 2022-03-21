import os
import sys
import model
import camera
import cv2 as cv
import tkinter as tk
import PIL.Image, PIL.ImageTk
from pydub import AudioSegment
from pydub.playback import play

sys.setrecursionlimit(3000)

class App:
    def __init__(self, window = tk.Tk(), window_title = "Drive Drowsiness Detector"):
        self.window = window
        self.window_title = window_title

        self.counters = [1, 1]

        self.model = model.Model()

        self.auto_predict = False

        self.camera = camera.Camera()

        self.start_GUI()

        self.delay = 100
        self.update()

        self.window.attributes('-topmost', True)
        self.window.mainloop()

    def start_GUI(self):
        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height)
        self.canvas.pack(anchor=tk.CENTER, expand=True)

        self.btn = tk.Button(self.window, text="Start / Stop", width=50, command=lambda: self.start_prediction())
        self.btn.pack(anchor=tk.CENTER, expand=True)

        self.status_label = tk.Label(self.window, text="Status")
        self.status_label.config(font=('Calibri', 20))
        self.status_label.pack(anchor=tk.CENTER, expand=True)

        # self.auto_predict = True

    def start_prediction(self):
        self.auto_predict = not self.auto_predict

    def update(self):
        if self.auto_predict:
            self.predict()
            pass
        ret, frame = self.camera.get_frame()
        

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.camera.update_frame()

        print("Updating...")
        self.window.after(self.delay, self.update)

    def predict(self):
        prediction = self.model.predict()

        if prediction == "drowsy":
            self.status_label.config(text="Drowsy")
            
            sound = AudioSegment.from_wav("train-horn.wav")
            play(sound)

            return prediction
            pass
        else:
            self.status_label.config(text="Attentive")
            pass