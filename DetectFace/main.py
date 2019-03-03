#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 19/3/3 20:59
@author : Kay Lee
@file   : main.py 
@email  : wolflikai@163.com
@detail : None
'''
import cv2
import numpy as np
import dlib

def rotate(image, angle, scale=1.0):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # 旋转之后的尺寸
    n_width = int((h * sin) + (w * cos))
    n_height = int((h * cos) + (w * sin))
    M[0, 2] += (n_width - w) / 2
    M[1, 2] += (n_height - h) / 2
    rotated = cv2.warpAffine(image, M, (n_width, n_height))
    return rotated




def is_face(image_file):
    # predictor_path = './model/shape_predictor_68_face_landmarks.dat'
    # face_rec_model_path = "./model/dlib_face_recognition_resnet_model_v1.dat"
    detector = dlib.get_frontal_face_detector()
    # shape_predictor = dlib.shape_predictor(predictor_path)
    print("Processing file: {}".format(image_file))
    try:
        img = cv2.imread(image_file, cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)
        b, g, r = cv2.split(img)
        img_gray = cv2.merge([r, g, b])
        w, h = img_gray.shape[:2]
        resized_w, resized_h = w, h
        if w >= 400 or h >= 400:
            resized_w, resized_h = w // 4, h // 4
            img_gray = cv2.resize(img_gray, (resized_h, resized_w), interpolation=cv2.INTER_CUBIC)
        count = 3  # rotate times
        while count > 0:
            dets = detector(img_gray, 1)
            if len(dets) > 0 and len(dets) < 2:  # 只能包含一个人脸
                break
            elif len(dets) > 1:
                print(' faces counts greater than 1 faces')
                return False
            else:
                img_gray = rotate(img_gray, -90 * count)
                count -= 1
        if len(dets) < 1:
            print(' Do not detect a face in the image')
            return False
        return True

    except Exception as err:
        print(' not a face error:' + str(err))
        return False


if __name__ == '__main__':
    is_face('./img/1.jpg')