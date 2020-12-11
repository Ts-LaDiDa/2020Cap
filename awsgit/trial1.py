'''
basic functionality intact, next step for meta data timestamp and last upload first download
'''
import json
import boto3
from botocore.config import Config
import datetime as d
import key as k

test ={}
test['order-test']=[]
test['order-test'].append(
    {
        'drink-name':'White Russian',
        'drink-number':1
    }
)
test['order-test'].append(
    {
        'drink-name':'Apple Martini',
        'drink-number':1
    }
)

testSerialized = json.dumps(test)


timestamp = d.datetime.now()

a_a_k = k.key1     #input your key
a_s_a_k = k.skey1  #input your secret key
a_d_r = 'us-east-2'

conner_aak = k.key2
conner_asak = k.skey2

bucketName = 'robarorders'

s3 = boto3.client(
    service_name = 's3',
    region_name = a_d_r,
    aws_access_key_id = conner_aak,
    aws_secret_access_key = conner_asak
)

s3.put_object(Bucket = bucketName, Key='order0.json')


