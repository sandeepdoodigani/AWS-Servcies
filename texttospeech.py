# -*- coding: utf-8 -*-
"""
Created on Sun May  9 08:11:41 2021

@author: SmartBridgePC
"""

#import the boto3  library to connect to the AWS service
import boto3
from pygame import mixer
import os


#Giving the credentials to gain complete access from the Rekognition API(service)
access_key_id = 'AKIA3GFGYRQGVRGPDFG4'
secret_access_key = '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'

#Region
region='ap-southeast-2' 

polly_client = boto3.client('polly',
                            region,
                            aws_access_key_id = access_key_id,
                            aws_secret_access_key = secret_access_key)
  

speech = polly_client.synthesize_speech(VoiceId='Joanna',
                OutputFormat='mp3', 
                Text = "helloword")

with open('output.mp3', 'wb') as f:
    f.write(speech['AudioStream'].read())
    f.close()

mixer.init()#initilizing mixer
mixer.music.load('output.mp3')#load our output
mixer.music.play()#play the loaded output

#once speaking is done delete the file
while mixer.music.get_busy() == True:
    pass

mixer.quit()
os.remove('output.mp3')