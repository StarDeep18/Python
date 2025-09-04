import cv2 #importing openCV library
cap = cv2.VideoCapture(0) #opening camera
while True:
    ret,frame = cap.read() #read frame from camera
    if not ret:
        break
    m_frame = cv2.flip(frame,1) #flipping the camera
    cv2.imshow("Cam",m_frame)
    if cv2.waitKey(2) & 0xFF == ord('x'): # Wait for a key press for 2 ms, if 'x' is pressed, break loop
        break
cap.release()
cap.destroyAllWindows() #close all openCV windows