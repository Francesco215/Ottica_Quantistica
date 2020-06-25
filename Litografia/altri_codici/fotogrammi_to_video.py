import cv2
import os

path='immagini/differenze/'

immagini=[]
for i in range(len(os.listdir(path))):
	immagini.append(str(i)+'.jpg')
frame=cv2.imread(path+immagini[1])
height, width, layers = frame.shape
video = cv2.VideoWriter('video30.avi',0, 30,(width,height))
for image in immagini:
    video.write(cv2.imread(os.path.join(path, image)))
    
cv2.destroyAllWindows()
video.release()