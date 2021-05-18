# -*- coding: utf-8 -*-
"""
Created on Sun May 16 18:41:10 2021

@author: SmartBridgePC
"""


import boto3
import os

client = boto3.client('s3',
                        aws_access_key_id = 'AKIA3GFGYRQG5TWGSCYV',
                        aws_secret_access_key = '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')


for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'doodigani'
        upload_file_key = 'python/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)