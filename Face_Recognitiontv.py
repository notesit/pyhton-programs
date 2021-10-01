# Face Recognition by Tushar Verma

import cv2
import os
import numpy as np
from PIL import Image




# This function is use to capture user face
def face_capture():
    vid_cam = cv2.VideoCapture(0)

    face_detector = cv2.CascadeClassifier(
        'cascades/data/haarcascade_frontalface_default.xml')

    face_id = 1
    count = 0


    while(vid_cam.isOpened()):
        ret, image_frame = vid_cam.read()

        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(image_frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' +
                        str(count) + ".jpg", gray[y:y+h, x:x+w])

        cv2.imshow('Face Recognition', image_frame)

        if cv2.waitKey(100) & 0xFF == ord('~'):
            break
        elif count > 100:
            break

    vid_cam.release()
    cv2.destroyAllWindows()

    face_trainer()

    return


# This funtion is use to train face images
def face_trainer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(
        "cascades/data/haarcascade_frontalface_default.xml")


    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []
        ids = []

        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y+h, x:x+w])
                ids.append(id)
        return faceSamples, ids


    faces, ids = getImagesAndLabels('dataset')

    recognizer.train(faces, np.array(ids))
    recognizer.save("recognizers/face-trainner.yml")


# This function is use to face recognition
def face_check():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("recognizers/face-trainner.yml")

    cascadePath = "cascades/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)


    cam = cv2.VideoCapture(0)

    # Count for 10 seconds
    count = 0

    # Check if face is recognition or not
    check = 0

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)

        for(x, y, w, h) in faces:
            cv2.rectangle(im, (x-20, y-20), (x+w+20, y+h+20), (0, 255, 0), 4)
            Id, conf = recognizer.predict(gray[y:y+h, x:x+w])
            print(conf)

            if conf>=4 and conf <= 75:
                with open('user_info/user_recognition.txt', 'w') as f:  # Write if face is recognitize
                    f.write('known')
                
                check = 1

            else:
                with open('user_info/user_recognition.txt', 'w') as f:  # Write if face is not recognitize
                    f.write('unknown')

            
        # Break if face is recognitize
        if check == 1:
            break

        # Count upto 100
        count += 1

        if count == 100:
            break

        if cv2.waitKey(10) & 0xFF == ord('~'):
            break
    cam.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    face_capture()

    face_trainer()

    face_check()







