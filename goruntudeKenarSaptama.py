import cv2

cap = cv2.VideoCapture(0) # Kamera açma

while 1:
    # ret -> cap değişkenin doğru okuyup okumadığını yazar (true, false)
    # frame -> okunan kareleri (frameleri) yazar
    ret, frame = cap.read()  # cap.read() 2 adet değer okur
    frame = cv2.flip(frame, 1)  # Her bir görüntüyü eksenlerde yansıtmaya yarar.
    # (1 -> y ekseni / 0 -> x ekseni / -1 -> orjine göre)

    edges = cv2.Canny(frame, 100, 200) # (input, min threshold, max threshold)

    # Alınan frameler ekranlarda gösterilir
    cv2.imshow("Frame",frame)
    cv2.imshow("Edges",edges)

    # 0xFF == ord("q") -> Klavyeden girilen karaktere göre işlem yapar.
    if cv2.waitKey(25) & 0xFF == ord("q"):  # 25 milisaniye de bir görüntüyü gösterir ve q tuşuna basılırsa döngüyü kır.
        break

cap.release()  # cap değişkenini okutmayı bırakır
cv2.destroyAllWindows()  # Kapatma tuşuna basıldığında OpenCV'ye bağlı tüm pencereleri kapatır.