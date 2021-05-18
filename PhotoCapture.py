# -*- coding: utf-8 -*-
"""
Created on Tue May 18 08:13:56 2021

@author: SmartBridgePC
"""

import cv2
import boto3

client = boto3.client('s3',
                        aws_access_key_id = 'AKIA3GFGYRQG5TWGSCYV',
                        aws_secret_access_key = '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')



cam = cv2.VideoCapture(0)

cv2.namedWindow("S3Upload")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("S3Upload", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        upload_file_bucket = 'doodigani'
        upload_file_key = 'Images/' + str(img_name)
        client.upload_file(img_name, upload_file_bucket, upload_file_key)
        img_counter += 1

cam.release()
cv2.destroyAllWindows()