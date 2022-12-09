from deepface import DeepFace
import os
import cv2
from config import dict_faces
from PIL import Image
from pixellib.instance import instance_segmentation


def face_detection_cv(image):
    face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = cv2.imread(image)
    # img = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4), interpolation=cv2.INTER_AREA)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(imgGray, 1.1, 19)
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        im = Image.open(image)
        cr = im.crop((x, y, x + w, y + h))
        cr.save('imgNotBg/cr{}.png'.format(dict_faces['count']))
        dict_faces['count'] += 1

    print(f'{dict_faces["imCount"]} / 548, {str((dict_faces["imCount"] / 548) * 100)[:5]} %')
    # imgRe = cv2.resize(img, (img.shape[1] // 4, img.shape[0] // 4), interpolation=cv2.INTER_AREA)
    # cv2.imshow('result', imgRe)
    # cv2.waitKey()


def face_detection(img, output):
    segment_image = instance_segmentation()
    model = MaskRCNN(mode="inference", model_dir=r'C:\Users\User001\PycharmProjects\NewFaceRecog\mask_rcnn_balloon.h5',
                     config=ImageBoundaryConfig())
    segment_image.load_model(r'C:\Users\User001\PycharmProjects\NewFaceRecog\mask_rcnn_balloon.h5')
    segment_image.segmentImage(
        image_path=img,
        output_image_name=output,
    )


def face_verify(img1, img2):
    try:
        result_dict = DeepFace.verify(img1_path=img1, img2_path=img2)

        if result_dict.get('verified'):
            return 'Ok!'
        return 'Not Ok!'

    except Exception as _ex:
        return _ex


def face_recog(direct):
    try:
        for per in os.listdir('faces'):
            print(per)
            for image in os.listdir(direct):
                result = DeepFace.find(img_path=f'{direct}/{image}',
                                       db_path=r'faces/{}'.format(per),
                                       model_name='Facenet512',
                                       enforce_detection=False,)
                result = result.values.tolist()

                if len(result) > 0:
                    dict_faces[per] += 1
            print(dict_faces[per])

    except Exception as _ex:
        return _ex


def main():
    # print(face_verify(img1=r'faces\Nastya\2Z2A7266.jpg', img2=r'faces\Nastya\2Z2A7271.jpg'))
    print(face_recog('imgNotBg'))
    print(dict_faces)
    # face_detection_cv('images/2Z2A6319.jpg')
    # face_detection_cv('images/2Z2A6337.jpg')
    # for image in os.listdir('images'):
    #     face_detection_cv('images/' + image)
    #     dict_faces['imCount'] += 1


if __name__ == '__main__':
    main()
