"""Connection test for AWS SQS.

"""

import awsconf
import datetime
import json
import hashlib
import hmac
import urllib
import urllib2
import random


rand_integer = random.randint(1, 10000000)
age_integer = random.randint(1, 104)

POST_MESSAGE_SAMPLE = {
    "name": "hogehogepiyopiyo{}".format(str(rand_integer)),
    "age": age_integer
}
print POST_MESSAGE_SAMPLE

JSON_POST_SAMPLE = json.dumps(POST_MESSAGE_SAMPLE)

POST_SAMPLE = {
    "Action": "SendMessage",
    "MessageBody": JSON_POST_SAMPLE,
    "Version": "2012-11-05",
    "Expires": "2016-10-15T12%3A00%3A00Z"
    # ,
    # "Credential": awsconf.ACCESS_KEY_ID,
    # "SignedHeaders": awsconf.SECRET_ACCESS_KEY
}

t = datetime.datetime.utcnow()
amz_date = t.strftime('%Y%m%dT%H%M%SZ')
method = 'POST'
region = 'us-west-2'
service = 'dynamodb'
date_stamp = t.strftime('%Y%m%d') # Date w/o time, used in credential scope

algorithm = 'AWS4-HMAC-SHA256'

def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, date_stamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning

canonical_uri = '/'
canonical_querystring = ''
canonical_headers = 'content-type:' + content_type + '\n' + 'host:' + host + '\n' + 'x-amz-date:' + amz_date + '\n' + 'x-amz-target:' + amz_target + '\n'
signed_headers = 'content-type;host;x-amz-date;x-amz-target'
canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

credential_scope = date_stamp + '/' + region + '/' + service + '/' + 'aws4_request'
string_to_sign = algorithm + '\n' +  amz_date + '\n' +  credential_scope + '\n' +  hashlib.sha256(canonical_request).hexdigest()


# ************* TASK 3: CALCULATE THE SIGNATURE *************
# Create the signing key using the function defined above.
signing_key = getSignatureKey(secret_key, date_stamp, region, service)

# Sign the string_to_sign using the signing_key
signature = hmac.new(signing_key, (string_to_sign).encode('utf-8'), hashlib.sha256).hexdigest()


AUTHORIZATION = (algorithm + ' ' + 
    'Credential=' + awsconf.ACCESS_KEY_ID + '/' + credential_scope + ', ' +  
    'SignedHeaders=' + awsconf.SECRET_ACCESS_KEY + ', ' + 
    'Signature=' + signature)

post_data = urllib.urlencode(POST_SAMPLE)
req = urllib2.Request(awsconf.SQS_DOMAIN,
                      post_data,
                      {'Content-Type': 'application/x-www-form-urlencoded',
                       'Authorization': AUTHORIZATION})
res = urllib2.urlopen(req)
print res
