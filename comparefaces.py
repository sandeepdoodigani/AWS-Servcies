# -*- coding: utf-8 -*-
"""
Created on Sun May  9 06:22:37 2021

@author: SmartBridgePC
"""

#import the boto3  library to connect to the AWS service
import boto3

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA3GFGYRQGVRGPDFG4'
secret_access_key = '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'

#Region
region='ap-southeast-2' 

#client representing AWS Rekognition service
client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
                     
#image of the bucket
photo = 'pawan.jpg'
photo1='kcr.jpg'


response = client.compare_faces(
    SourceImage={
        'S3Object': {
            'Bucket': 'rekognitionmallareddy',
            'Name': photo1
            }},
    TargetImage={
        'S3Object': {
            'Bucket': 'rekognitionmallareddy',
            'Name': photo1
        }
    },
      
    )
for key, value in response.items():
    if key in ('FaceMatches', 'UnMatchedFaces'):
        print(key)
        for att in value:
            print(att)
print(response)