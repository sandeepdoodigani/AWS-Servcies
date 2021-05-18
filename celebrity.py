# -*- coding: utf-8 -*-
"""
Created on Sun May  9 06:51:45 2021

@author: SmartBridgePC
"""

#import the boto3  library to connect to the AWS service
import boto3

#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA3GFGYRQGTSSPL3N3'
secret_access_key = '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'

#Region
region='us-west-2' 

#client representing AWS Rekognition service
client = boto3.client('rekognition', region, aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)
                     
#image of the bucket
photo = 'chiranjeevi.jpg'
response = client.recognize_celebrities(
    Image={
        'S3Object': {
            'Bucket': 'rekoginition',
            'Name': photo
            }},
      
    )

for key, value in response.items():
    if key =="CelebrityFaces":
        for people in value:
            print(people['Name'])

#print(response)