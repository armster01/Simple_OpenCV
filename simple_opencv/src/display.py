import cv2

class Display:
    def __init__(self, window_name="Face Detection"):
        self.window_name = window_name
        
    def show_frame(self, frame):
        cv2.imshow(self.window_name, frame)
        
    def check_quit(self):
        # Return True if 'q' is pressed
        return cv2.waitKey(1) & 0xFF == ord('q')