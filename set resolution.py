import cv2 as cv

def main():
    Name="live video feed"
    cv.namedWindow(Name)
                 
    cap= cv.VideoCapture(0)
    
    print('Width :' +str(cap.get(3)))
    print('Height :' +str(cap.get(4)))
    
    cap.set(3,6000)
    cap.set(4,6000)
    print('Width :' +str(cap.get(3)))
    print('Height :' +str(cap.get(4)))
    
    
    
    if cap.isOpened():
        ret, frame=cap.read()
        
    else:
        ret=False
        
    while ret:
        
        ret,frame=cap.read()
        
        product=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
        cv.imshow("Gray",product)
        cv.imshow(Name,frame)
        
        if cv.waitKey(1)== 27:
            break
    cv.destroyAllWindows()
    
    cap.release()
    
if __name__=="__main__":
    main()

#high resolution= 1280*720               

