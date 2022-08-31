import cv2
import numpy as np

# Resimleri tanımlama
img = cv2.imread("text.png")
img1 = cv2.imread("contour.png")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # Resmi grileştirme

gray = np.float32(gray) # İşleme sokabilmek için float32 tipine dönüşmesi gerek

# (resim değişkeni, köşe sayısı, kalite değeri, köşeler arası min uzaklık)
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10) # Köşeleri bulan fonk

corners = np.int0(corners) # Çember vs çizerken float sayılar kullanılmaz

for corner in corners:
  x, y = corner.ravel() # x ve y değerlerini rahat alabilmek için cornersı tek bir satır haline getiriyoruz
  cv2.circle(img1, (x,y), 3, (0,0,255), -1) # Çember çizimi

cv2.imshow("corner",img1) # İşlenmiş resmi ekranda gösterir

cv2.waitKey(0) # Pencere açıldığında kapanma süresi ms cinsinden (0 olması sonuz açık pykalman).
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.