import cv2 as cv

def main():
    Name="live video feed"
    cv.namedWindow(Name)
                 
    cap= cv.VideoCapture(0)
    if cap.isOpened():
        ret, frame=cap.read()
        
    else:
        ret=False
        
    while ret:
        
        ret,frame=cap.read()
        
       # product=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        
       # cv.imshow("Gray",product)
        cv.imshow(Name,frame)
        
        if cv.waitKey(1)== 27:
            break
    cv.destroyAllWindows()
    
    cap.release()
    
if __name__=="__main__":
    main()
                  