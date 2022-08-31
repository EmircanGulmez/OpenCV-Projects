import cv2
import numpy as np

def nothing(): # OpenCV createTrackbar fonksiyonunun hatasız çalışması için gerekli
    pass

# np.uint8 -> Çizim yaptığımız veri tipidir.
canvas = np.zeros((512, 512, 3), dtype=np.uint8) # Tuval oluşturulur
cv2.namedWindow("Trackbar") # Oluşturulan pencereye ad verilir (Tracbarlar için)

# Trackbar oluşturma
# (Trackbar adı, yerleşeceği pencere adı, başlangıç değeri, bitiş değeri, boş fonk)
cv2.createTrackbar("R", "Trackbar", 0, 255, nothing) # RED
cv2.createTrackbar("G", "Trackbar", 0, 255, nothing) # GREEN
cv2.createTrackbar("B", "Trackbar", 0, 255, nothing) # BLUE
anahtar = "ON-OFF"
cv2.createTrackbar(anahtar, "Trackbar", 0, 1, nothing) # SWITCH

while True: # Pencerenin sürekli yenilenmesi için
    cv2.imshow("Trackbar", canvas) # Pencerede olşturulan tuval gösterilir

    if cv2.waitKey(1) & 0xFF == ord("q"): # 1 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

    # Kızakların konumlarının değerlerini alma
    r = cv2.getTrackbarPos("R", "Trackbar")
    g = cv2.getTrackbarPos("G", "Trackbar")
    b = cv2.getTrackbarPos("B", "Trackbar")
    k = cv2.getTrackbarPos(anahtar, "Trackbar")

    if k == 0: # Anahtar kapalı ise siyah ekran yap
        canvas[:] = [0, 0, 0] # Canvas daki tüm piksel değerini 0 yapar (siyah)

    if k == 1: # Anahtar açık ise kızakların değerlerini yaz
        canvas[:] = [b, g, r] # Canvas daki b g r değerlerine göre atama yapar

cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.