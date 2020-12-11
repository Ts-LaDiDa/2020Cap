# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:37:17 2020

@author: tuya
"""

import boto3
import json
import OrderPy as odrs
import key as k

id = 0

raw_data = odrs.excelread()

raw_ls = odrs.to_ls(raw_data)

print(raw_ls[0])

orders = dict()


conner_aak = k.key2
conner_asak = k.skey2

#bucketName = 'robarorders'

s3 = boto3.client(
    service_name = 's3',
    region_name = 'us-east-2',
    aws_access_key_id = conner_aak,
    aws_secret_access_key = conner_asak
    )

#Bucket;
bucket_e = s3.list_buckets()
e_data = bucket_e['Buckets'][0]
bucket_name = e_data['Name']
#print(e_data['Name'],' ',e_data['CreationDate'].ctime())

#objects:
objects = s3.list_objects_v2(Bucket = bucketName)['Contents']
obj_key = objects[0]['Key']
print(obj_key)


#download department
obje = s3.get_object(Bucket = bucketName, Key = obj_key)
print(obje['ResponseMetadata']['HTTPHeaders']['last-modified'])

with open('j_t.json','wb') as f:
    s3.download_fileobj(bucket_name,obj_key,f)
    f.close()

ordrs.data_server()