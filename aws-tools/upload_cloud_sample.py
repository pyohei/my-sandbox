import json
import uuid
import boto3
import logging
import random
import StringIO


queue_name = ''
cloudsearch_name = '-sync-sandbox'
max_queue = 1

logger = logging.getLogger()
logger.setLevel(logging.INFO)

##### Test data ######
TEST_SAMPLE = [
 {"type": "add",
  "id":   "tt0484562",
  "fields": {
    "name": "piyopiyo",
    "age": 10
  }
 }
]
TEST_SAMPLE_JSON = json.dumps(TEST_SAMPLE)
stringiotest = StringIO.StringIO()
stringiotest.write('TEST_SAMPLE_JSON')
#stringiotest.close()
######################

def lambda_handler(event, context):
    logger.info('--------------- START ------------------')

    # Get Queue
    logger.info('###### Get Queue #######')
    queue = boto3.resource('sqs').get_queue_by_name(QueueName = queue_name)
    messages = queue.receive_messages(MaxNumberOfMessages = max_queue)
    recs = []
    for message in messages:
        recs.append(message.body)
        logger.info("ADD: {}".format(str(message.body)))

    # CloudSearch Synchronize
    logger.info('####### CloudSearch Sync! ########')
    cloudsearch_client = boto3.client(
        'cloudsearchdomain', 
        region_name = '',
        endpoint_url='')
    response = cloudsearch_client.upload_documents(
        documents=TEST_SAMPLE_JSON,
        contentType='application/json')
    logger.info(str(response))
    return 'Finish'

#def upload_cloudsearch_domain():
#    """Upload data to CloudSearch."""
#    import urllib
#    import urllib2
#    endpoint_url = "
#    
#"""
