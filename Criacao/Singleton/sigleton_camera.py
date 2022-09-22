import cv2

class SingletonCam(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class ConnectCam(metaclass=SingletonCam):

    def __init__(self):
        self.__camera = 0
    
    @property
    def get_cam(self):
        return self.__camera


    @get_cam.setter
    def set_cam(self,__newcam):
        self.__camera = __newcam


    def connect_cam(self):
        cam = cv2.VideoCapture(self.__camera)
        
        if not cam.isOpened():
            raise  IOError("Cannot open webcam")
        else :
            print("aqui")
            return cam


    def video_stream(self, cap):

        while(1):
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

        cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":

    cam = ConnectCam()
    cap = cam.connect_cam()
    cam.video_stream(cap)

    cam2 = ConnectCam()
    cap2 = cam2.connect_cam()

    cam.video_stream(cap2)