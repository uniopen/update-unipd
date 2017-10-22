import boto3
import json
from botocore.exceptions import ClientError
from update_utils import getcal

client = boto3.client('s3',
                      region_name='eu-west-1')

def main(event, context):
    if event.get("what") == "calendar": 
        mensaCal = getcal()
        print(mensaCal)
        response = client.get_object(Bucket="uniopen-data", Key="unipd/mensa.json")
        details = json.loads(response['Body'].read())
        print(details)
        for mensa in mensaCal:
            details[mensa]["calendario"] = mensaCal[mensa]
        print(details)

        r = client.put_object(Bucket="uniopen-data", Key="unipd/mensa.json", Body=json.dumps(details))
        print(r)

    return "Done"

# main({"what": "calendar"}, 1)