

import cv2
import numpy as np
import threading
import queue
import time

def main():
    # open webcamera
    cap = cv2.VideoCapture(0)
    #share frame
    q = queue.Queue()
    # create a thread to get the frame
    t1 = threading.Thread(target=drawFrame, args=(cap, q), daemon=True)
    #t2 = threading.Thread(target=drawPoints, args=(q,))
    t1.start()

    drawPoints(q)

    cap.release()
    cv2.destroyAllWindows()


def drawPoints(q):
    while True:
        #await q.get()
        frame = q.get()

        if(not q.empty()):
            break; 

        # get the points of image where the color is white
        #points = np.argwhere(frame == [255, 255, 255])

        maxWidth = frame.shape[1]
        maxHeight = frame.shape[0]
        satadj=1.5
        # increase saturation
        imghsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype("float32")

        (h, s, v) = cv2.split(imghsv)
        s = s*satadj
        s = np.clip(s,40,255)
        imghsv = cv2.merge([h,s,v])

        saturatedImage = cv2.cvtColor(imghsv.astype("uint8"), cv2.COLOR_HSV2BGR)

        gray = cv2.cvtColor(saturatedImage, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        _,threshold = cv2.threshold(gray, 100, 255,  cv2.THRESH_BINARY)

        contours,_=cv2.findContours(threshold, cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours :
            area = cv2.contourArea(cnt)
            
            #cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 3)

            # try to find polygons with 4 sides
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            #cv2.drawContours(frame, [approx], 0, (255, 0, 0), 5)
            if len(approx) <= 7 and area > 200:
                
                cv2.drawContours(frame, [approx], 0, (255, 0, 0), 3)
                #put a circle in each corner
                for point in approx:
                    cv2.circle(frame, (point[0][0], point[0][1]), 5, (0, 0, 255), -1)
                
                #print("found one at: ", approx)
                
                #cv2.drawContours(frame, [approx], 0, (200, 50, 70), 5)
        
        q.put(frame)
        #sleep a sec to not overload the system
        time.sleep(2)



def drawFrame(cap, q): 
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        q.put(frame)
        # press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #send event to kill all threads
            q.put(0xFF)
            break

        
        frame=q.get()
        # call drwaPoints as a thread
        cv2.imshow("frame", frame)

# Execute the main function using the father thread
if __name__ == "__main__":
    main()