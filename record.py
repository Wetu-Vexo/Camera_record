import cv2
import queue
import time
import rhreading

q = queue.Queue()
videopath = 0
duration = 5*60
savepath = "video.avi"
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter(save_video, fourcc, 20, (width, height))

start_time = time.time()

def Receive():
    print("start Reveive")
    cap = cv2.VideoCapture("rtsp://admin:admin_123@172.0.0.0")
    ret, frame = cap.read()
    q.put(frame)
    while ret:
        ret, frame = cap.read()
        q.put(frame)

def Record():
  while True:
    if .empty() !=True:
      frame = q.get()
      writer.write(frame)
      if (time.time() - start_time >= duration):
          break
      if cv2.waitKey(1) & 0xff == ord('q'):
          break

if __name__=='__main__':
    p1=threading.Thread(target=Receive)
    p2 = threading.Thread(target=Display)
    p1.start()
    p2.start()
