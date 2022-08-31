import cv2
import numpy as np

cap = cv2.VideoCapture("dog.mp4")

while 1:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # HSV code for blue,red,white şeklinde internette aranabilir
    sensitivity = 50 # hassasiyet değer
    lower_white = np.array([0,0,255-sensitivity]) # en düşük beyaz değer
    upper_white = np.array([255,sensitivity,255]) # En yüksek beyaz değer

    # (hsv değişkeni, min değerler, max değerler)
    mask = cv2.inRange(hsv,lower_white,upper_white) # en düşük ve en yüksek değerler göre hsv değişkenine maske uygula
    res = cv2.bitwise_and(frame,frame,mask=mask)
    # 2 kere yazmamızın sebebi bir resimde ilk orjinal resim, diğeri ise kazma yani bu fonk içerisinde 2li döngü oluşuyor

    # Çıktıları ekranda gösterme
    cv2.imshow("frame", frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",res)

    if cv2.waitKey(25) & 0xFF == ord("q"):  # 25 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

cap.release() # cap değişkenini okutmayı bırakır
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.