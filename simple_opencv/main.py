from src.camera import Camera
from src.detectors import FaceDetector
from src.display import Display

def main():
    # Initialize components
    camera = Camera()
    detector = FaceDetector()
    display = Display()
    
    print("Face Detection Started!")
    print("Press 'q' to quit")
    
    while True:
        # Capture frame
        frame = camera.read_frame()
        if frame is None:
            break
            
        # Process frame
        processed_frame = detector.detect(frame)
        
        # Display results
        display.show_frame(processed_frame)
        
        # Check for quit
        if display.check_quit():
            break
    
    # Cleanup
    camera.release()

if __name__ == "__main__":
    main()