import cv2           
# Loading module

cap = cv2.VideoCapture(0)
# Creating video capture object

four_cc = cv2.VideoWriter_fourcc('X','V','I','D')   
# Declaring the video format

writer = cv2.VideoWriter('outputVideo.avi',four_cc,20.0,(640,480))
# Creating video writer object

frames = []         
# Creating a list where every input frame will be stored.
while cap.isOpened():            
    ret,image = cap.read()
    # Taking frame input
    
    if ret:                              
        frames.append(image)
        # Storing  frame into a list
    
    cv2.imshow("Input video",image)   
    # Displaying input frame
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
for frame in frames[::-1]:        
    writer.write(frame)    
    # Writing the video from the frames appended in list in reverse order

cap.release()                
# Releasing Video Capture object

writer.release()
# Releasing video writer object

cv2.destroyAllWindows()  
# Freeing up memory by destorying all opened windows.
