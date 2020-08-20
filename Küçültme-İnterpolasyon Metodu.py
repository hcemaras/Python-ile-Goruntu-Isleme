# Küçültme İnterpolasyon
n= 1.25
h= round(r/n)
w= round(c/n)

ims= np.zeros((h, w, 3)) 

# Fonksiyon
def bgrmean(i,j,n,img):
    total = [[0,0,0]]
    for m in range(round(i*n),round((i+1)*n)):
        for n in range(round(j*n),round((j+1)*n)):
            total=np.vstack(total, img[m,n])
    return(np.round(np.mean(total,axis=0)))

# Döngü
for i in range(0,h):
  for j in range(0,w):
    ims[i,j]= bgrmean(i,j,n,img)

cv2.imwrite("ims2.png",ims)
goster(ims)
