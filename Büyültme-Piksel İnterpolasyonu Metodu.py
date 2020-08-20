# Okuma
img= cv2.imread("ims1.png")
goster(img)

# Çözünürlük
r= np.shape(img)[0]
c= np.shape(img)[1]
print(r,c)

n= 1.25
h= round(r*n)
w= round(c*n)

# Aynı Değerleri Atama ve Orijinal Noktalar Arası İnterpolasyonu Döngüsü
for i in range (0,h):
    for j in range (0,w):
        if (i%n==0) and (j%n==0):
            imn[i,j]=img[(i//n),(j//n)]
        elif (i%n==0):
            aa = np.multiply((n-(j%n))/n,img[i//n,(j-(j%n))//n])
            bb = np.multiply((j%n)/n,img[i//n,((j+n-(j%n)))//n-1])             
            imn[i,j]=np.sum((aa,bb),axis=0)
        elif (j%n==0):
            aa = np.multiply((n-(i%n))/n,img[(i-(i%n))//n,j//n])
            bb = np.multiply((i%n)/n,img[(i+n-(i%n))//n-1,j//n])
            imn[i,j]=np.sum((aa,bb),axis=0)

# Yeni Atanmış Noktalar Arası İnterpolasyonu Döngüsü
for i in range(0,h):
    if (i%n!=0):
        for j in range (0,w):
            if (j%n != 0):
                u=np.multiply((n-i%n)/2/n,img[(i-i%n)//n-1,j//n])
                d=np.multiply((i%n)/2/n,img[(i+n-i%n)//n-1,j//n])
                l=np.multiply((n-j%n)/2/n,img[i//n,(j-j%n)//n-1])
                r=np.multiply((j%n)/2/n,img[i//n,(j+n-j%n)//n-1])
                imn[i,j]=np.sum([u,d,l,r], axis=0)

goster(imn)
