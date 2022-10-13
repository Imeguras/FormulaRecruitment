

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
        points = np.argwhere(frame == [255, 255, 255])
        # draw a circle in said location
        
        cv2.circle(frame, (points[0][1], points[0][0]), 10, (0, 0, 255), -1)
        #release the frame
        q.put(frame)
        #sleep a sec to not overload the system
        time.sleep(1)



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