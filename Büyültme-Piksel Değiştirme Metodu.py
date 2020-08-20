# Okuma
img= cv2.imread("ims1.png")
goster(img)

# Çözünürlük
r= np.shape(img)[0]
c= np.shape(img)[1]
print(r,c)

n= 1.25
h= round(r*n)-1
w= round(c*n)-1

#Boş Görüntü oluşturma
imb= np.zeros((h, w, 3), np.uint8) 

for i in range(0,h):
  for j in range(0,w):
    imb[i,j]=img[round(i/n),round(j/n)]

cv2.imwrite("imb1.png",imb)
goster(imb)
