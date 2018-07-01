import json
import boto3
import logging
import random

queue_name = 'sandbox_account'
max_queue = 10

SAMPLE_JSON = [
    {"type": "add",
     "id": "num%s".format(random.randint(1, 10000)),
     "fields": {
         "message": "testhogehoge"}}
    ]
str_json = json.dumps(SAMPLE_JSON)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        logger.info('--------------- START ---------------------')
        logger.info(event)

        # ===== SQS operation =====
#        queue = boto3.resource('sqs').get_queue_by_name(
#            QueueName = queue_name)
#        messages = queue.receive_messages(MaxNumberOfMessages = max_queue)
#        recs = []
#        for message in messages:
#            recs.append(message.body)
#            logger.info(str(message.body))
#            logger.info("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

        # ===== DynamoDB operation =====
        # dynamo_table = boto3.resource('dynamodb').Table('sandbox-dynamo')
        # with table.batch_writer
        new_recs = []
        for record in event['Records']:
            print "----- RECORD ------"
            print record
            new_recs.append(record['dynamodb']['Keys']['id']['N'])
            for rec_key in record.keys():
                print(record[rec_key])
        print('Successfully processed %s records.' % str(
            len(event['Records'])))
        # ===== CloudSearch operation =====
#        logger.info('####### CloudSearch Sync! ########')
#        cloudsearch_client = boto3.client(
#            'cloudsearchdomain',
#            endpoint_url='url')
#        cloudsearch_client = boto3.client('url')
#        logger.info('####### HERE!!!!! ########')
#        logger.info(str(cloudsearch_client))
#        response = cloudsearch_client.upload_documents(
#            documents=str_json,
#            contentType='application/json')
#        logger.info(str(response))
        dynamo_table = boto3.resource('dynamodb').Table('sandbox-naming')
        with dynamo_table.batch_writer() as batch:
            for new_rec in new_recs:
                batch.put_item(Item={"myname": str(new_rec)})
        return 'OK!'
    except Exception as e:
        logger.error(e)
        raise e
