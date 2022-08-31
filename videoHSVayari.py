import cv2
import numpy as np

"""
0 -> PC'nin sabit kamerasını kullanır
1 -> USB'ye bağlı olan kamerayı kullanır
"""
cap = cv2.VideoCapture(0) # Kamera açma

def nothing(): # OpenCV createTrackbar fonksiyonunun hatasız çalışması için gerekli
    pass

cv2.namedWindow("Trackbar") # Pencereye ad verilir (Tracbarlar için)
cv2.resizeWindow("Trackbar",500,500) # Trackbar penceresinin boyutu

# Trackbar oluşturma
# (Trackbar adı, yerleşeceği pencere adı, başlangıç değeri, bitiş değeri, boş fonk)
cv2.createTrackbar("Lower-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lower-S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lower-V", "Trackbar", 0, 255, nothing)

cv2.createTrackbar("Upper-H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper-S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper-V", "Trackbar", 0, 255, nothing)

# Trackbar ilk başlama ayarı
cv2.setTrackbarPos("Upper-H", "Trackbar", 180)
cv2.setTrackbarPos("Upper-S", "Trackbar", 255)
cv2.setTrackbarPos("Upper-V", "Trackbar", 255)

while True:
    # ret -> cap değişkenin doğru okuyup okumadığını yazar (true, false)
    # frame -> okunan kareleri (frameleri) yazar
    ret, frame = cap.read()  # cap.read() 2 adet değer okur
    frame = cv2.flip(frame, 1)  # Her bir görüntüyü eksenlerde yansıtmaya yarar.
    # (1 -> y ekseni / 0 -> x ekseni / -1 -> orjine göre)

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Frameleri HSV formatına dönüştürür

    # Kızakların konumlarının değerlerini alma
    lower_h = cv2.getTrackbarPos("Lower-H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lower-S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lower-V", "Trackbar")

    upper_h = cv2.getTrackbarPos("Upper-H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper-S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper-V", "Trackbar")

    # Değerleri bir değişken içerisinde tutma
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    # maskelemek için girilen fonk
    mask = cv2.inRange(frame_hsv, lower_color, upper_color) # (hsv formatındaki frame, düşük değer, yüksek değer)

    cv2.imshow("Original", frame) # Orjinal frame
    cv2.imshow("Mask", mask) # Maskelenmiş frame

    if cv2.waitKey(1) & 0xFF == ord("q"):  # 1 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

cap.release() # cap değişkenini okutmayı bırakır
cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.