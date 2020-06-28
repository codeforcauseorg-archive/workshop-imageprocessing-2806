import cv2

cap = cv2.VideoCapture(0)

classifier = classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    ret, frame = cap.read()

    if ret:

        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            if (w>100) and (h > 100):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (179, 175, 107), 5)

        cv2.imshow("My Camera", frame)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()