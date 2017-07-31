TEST_SAMPLE = [
  {"type": "add",
   "id":   "n1",
   "fields": {
     "name": "c",
     "age": 130
   }
  }
]

import boto3
import json

cloudsearch_client = boto3.client(
    'cloudsearchdomain',
    region_name = 'ap-northeast-1',
    endpoint_url='https://')
print cloudsearch_client

TEST_SAMPLE_JSON = json.dumps(TEST_SAMPLE)

response = cloudsearch_client.upload_documents(documents=TEST_SAMPLE_JSON,contentType='application/json')

print response
