

import cv2
import numpy as np
import threading
import queue
import time

points = []
flagCollapse = False

def main():
    
    # open webcamera
    cap = cv2.VideoCapture(0)
    

    #share frame
    q = queue.Queue()
    

    # create a thread to get the frame
    t1 = threading.Thread(target=drawFrame, args=(cap, q), daemon=True)
    t1.start()
    t2 = threading.Thread(target=drawPoints, args=(q,), daemon=True)
    t2.start()
    # await until t1 is destroyed
    t1.join()
    
    
    #drawPoints(q)

    cap.release()
    cv2.destroyAllWindows()


def drawPoints(q):
    global points
    while True:
        #await q.get()
        frame = q.get()

        if(not q.empty()):
            break; 
    

    
        lab= cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        l_channel, a, b = cv2.split(lab)

        # Applying CLAHE to L-channel
        clahe = cv2.createCLAHE(clipLimit=2.0)
        cl = clahe.apply(l_channel)

        # merge the CLAHE enhanced L-channel with the a and b channel
        limg = cv2.merge((cl,a,b))

        # Converting image from LAB Color model to BGR color spcae
        frame = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        
       # contrast = cv2.cvtColor(contrastedFrame.astype("uint8"), cv2.COLOR_HSV2BGR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #gray = cv2.GaussianBlur(gray, (5, 5), 0)

        _,threshold = cv2.threshold(gray, 150, 255,  cv2.THRESH_BINARY)

        contours,_=cv2.findContours(threshold, cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours :
            area = cv2.contourArea(cnt)
            
            #cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 3)

            # try to find polygons with 4 sides
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            #cv2.drawContours(frame, [approx], 0, (255, 0, 0), 5)
            if len(approx) <= 4 and area > 200:
                
                cv2.drawContours(frame, [approx], 0, (255, 0, 0), 3)
                #put a circle in each corner
                for point in approx:
                    cv2.circle(frame, (point[0][0], point[0][1]), 5, (0, 0, 255), -1)
                    #lock a global variable to this thread
                    points=approx
                
            
            #createPerspectiveView(approx, frame)
			#await until the new frame is closed
            #cv2.waitKey(0)
        
        q.put(frame)
        #sleep a sec to not overload the system
        time.sleep(0.02)

def placePoint(q, x, y):
    global points
    points.append([[[x, y]]])
    print(points)
    

def drawFrame(cap, q): 
    global points
    global flagCollapse
    buttonLabel="auto mode= 0, manual mode= 1"
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # create a trackbar to switch between auto and manual mode that only has 40% of the width
    cv2.createTrackbar(buttonLabel, "image", 0, 1, lambda x: print(x))
    
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        q.put(frame)
        # press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #send event to kill all threads
            q.put(0xFF)
            break

        # get mode
        mode = cv2.getTrackbarPos(buttonLabel, "image")
        frame=q.get()
        
        # if left mouse button, python being python? lmao
        # I should really start to always use paper even when i think im already there...
        cv2.setMouseCallback('image', lambda event, x, y, flags, param: mouseClick(event, x, y, flags, param, mode, points, q, frame))
        #default behavior
        cv2.imshow("image", frame)
        time.sleep(0.02)
    

    

def mouseClick(event, x, y, flags, param, currentMode, approx, q, frame):
    global flagCollapse
    if event == cv2.EVENT_LBUTTONDOWN:
        #q.put(0xFF)
        #debugging stuff
        print("Current mode: "+str(currentMode))
    
        print("x: " + str(x) + " y: " + str(y))
        if(currentMode == 0):
            clipAnomaliesDistance=20
            print("Points:\n"+str(approx))
            print(".-. too lazy to format .-.")
            # get the distances to the points
            distances = []
            for point in approx:
                distances.append(np.linalg.norm(point - np.array([x, y])))
            
            
            # remove points that are clipAnomaliesDistance away from the previous point
            #for i in range(len(distances)):
           #     if(i == 0):
            #        continue
            #   for j in range(i):
            #        if(distances[i] - distances[j] < clipAnomaliesDistance):
            #            distances.pop(i)
            #            approx = np.delete(approx, i, 0)
            #            i-=1
            #            break
                
                    
            if len(approx) < 4:
                print("ERR Not enough points")
                return
            
            # get the 4 closest points
            closestPoints = []
            for i in range(4):
                closestIndex = np.argmin(distances)
                closestPoints.append(approx[closestIndex])
                #remove from aprox and distances
                approx = np.delete(approx, closestIndex, 0)
                distances.pop(closestIndex)
            # order points clockwise
            closestPoints = orderPoints(closestPoints)

            print("Closest points:\n"+str(closestPoints))
            flagCollapse=True
            createPerspectiveView(closestPoints, frame, q)

            #flagCollapse=False
            #createPerspectiveView(approx, frame)
        else:
            #flagCollapse=True
            if len(points) <= 3:
                placePoint(q, x, y)
            else:
                flagCollapse=True
                createPerspectiveView(approx, frame, q)
            # current mode in manual 
            
        #    mask = cv2.inRange(frame, (0, 0, 255), (0, 0, 255))
        #    nonzero = cv2.findNonZero(mask)
        #    distances = np.sqrt((nonzero[:,:,0] - target[0]) ** 2 + (nonzero[:,:,1] - target[1]) ** 2)
        #    nearest_index = np.argmin(distances)
            
def orderPoints(points):
    print("before:"+str(points))

    # order points using sort fuction by its y value and ascending
    points = sorted(points, key=lambda x: x[0][1], reverse=False)
    print("Points sorted by y:\n"+str(points))

    return points
    


def createPerspectiveView(closestPoints, frame, q):
	# corners
    tl = closestPoints[0][0]
    tr = closestPoints[1][0]
    bl = closestPoints[2][0]
    br = closestPoints[3][0]
    #birds eye view of the square formed by tl, tr, bl, br
    #width and height of the square
    width = int(np.sqrt((tl[0] - tr[0]) ** 2 + (tl[1] - tr[1]) ** 2))
    height = int(np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2))
    #print("width:"+str(width))
    #print("height:"+str(height))
    #transform matrix
    transformMatrix = cv2.getPerspectiveTransform(np.float32([tl, tr, bl, br]), np.float32([[0, 0], [width, 0], [0, height], [width, height]]))
    #transform the image
    birdsEyeView = cv2.warpPerspective(frame, transformMatrix, (width, height))
    cv2.imshow("Warped", birdsEyeView)


        

    




# Execute the main function using the father thread
if __name__ == "__main__":
    main()