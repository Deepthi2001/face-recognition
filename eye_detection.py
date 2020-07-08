import cv2
detect = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
img = cv2.imread("images\img4.jpg ")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detect.detectMultiScale(gray, 1.1, 5)
for (x, y, w, h) in faces:
    final_img = cv2.rectangle(img, (x, y), (x+w, y+w), (255, 255, 0), 2)
cv2.imshow("Elon eye", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
