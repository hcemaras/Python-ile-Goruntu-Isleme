import numpy as np
import cv2

# Gösterme Fonksiyonu
def goster(resim): cv2.imshow("resim", resim);cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)
img= cv2.imread("indir.png")
goster(img)

# Çözünürlük
r= np.shape(img)[0]
c= np.shape(img)[1]
print(r,c)
n= 1.25
h= round(r/n)
w= round(c/n)

ims= np.zeros((h, w, 3), np.uint8)  #Boş Görüntü oluşturma
for i in range(0,h):
      for j in range(0,w):
   	 ims[i,j]=img[round(i*n),round(j*n)]

cv2.imwrite("ims1.png",ims)
goster(ims)
