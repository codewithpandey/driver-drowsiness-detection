import PIL
import cv2 as cv

class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0)
        
        if not self.camera.isOpened():
            raise ValueError("Unable to open the camera!")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

        print(f'height:width{self.height}:{self.width}')


    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()


    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camera.read()

            if ret:
                return (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return None

    def update_frame(self):
        ret, frame = self.get_frame()
        cv.imwrite('frames/face.jpg', cv.cvtColor(frame, cv.COLOR_BGR2RGB))
        