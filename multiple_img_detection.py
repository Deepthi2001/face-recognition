import cv2, glob
# glob is a particular module that helps us to get all files from a particular file

all_images = glob.glob("images/*.jpg")
detect = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
print(all_images)
print(len(all_images))

for image in all_images:
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detect.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        final_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Final output", final_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()

