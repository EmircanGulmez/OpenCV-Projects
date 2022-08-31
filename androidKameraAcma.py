""" IP Webcam Android telefon uygulaması üzerinden ip bağlanarak kamera açma """
"""
IP Webcam uygulamasında Start Server tıklanır ve açılan kameranın alt kısmında bağlantının sadece 192.168.1.34:8080 
kısmı PC tarayıcıya yapıştırılır. Açılan sekmede Video rederer kısmında Browser seçilerek yayın görüntülenebilir.
Ardından sekmedeki url sonuna //shot.jpg yapıştırılır ve gidilir. Artık sekme frame gibi davranır url nin hepsi alınarak
kodlardaki url kısmına yapıştırılır.
"""
import cv2 # OpenCV kütüphanesi tanımlama
import numpy as np # Numpy kütüphanesi tanımlama
import requests # İnternetteki verilere etkileşim sağlar.

url = "https://192.168.1.34:8080//shot.jpg"

while True:
    img_resp = requests.get(url) # Devamlı olarak frame alınır.
    img_arr = np.array(bytearray(img_resp.content), dtype= np.uint8) # Alınan görüntüyü bytearray çevirerek array içerisinde tutulur.
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR) # Hafızadan çekilen görüntüyü renkli görüntülenebilir hale getirir
    img = cv2.resize(img, (640,480)) # Görüntüyü boyutlandırma
    cv2.imshow("Telefon Kamera", img) # Görüntüyü gösterme

    if cv2.waitKey(1) == 27: # 25 milisaniye de bir görüntüyü gösterir ve ESC ye basarak kapatılır
        break

cv2.destroyAllWindows() # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.