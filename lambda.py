import boto3
import json
from botocore.exceptions import ClientError
from update_utils import get_cal, get_menu

client = boto3.client('s3',
                      region_name='eu-west-1')

def main(event, context):
    if event.get("what") == "calendar": 
        mensaCal = get_cal()
        print(mensaCal)
        response = client.get_object(Bucket="uniopen-data", Key="unipd/mensa.json")
        details = json.loads(response['Body'].read())
        for mensa in mensaCal:
            details[mensa]["calendario"] = mensaCal[mensa]
        r = client.put_object(Bucket="uniopen-data", Key="unipd/mensa.json", Body=json.dumps(details))

    elif event.get("what") == "menu": 
        mensaMenu = get_menu()
        print(mensaMenu)
        response = client.get_object(Bucket="uniopen-data", Key="unipd/mensa.json")
        details = json.loads(response['Body'].read())
        for mensa in mensaMenu:
            details[mensa]["menu"] = mensaMenu[mensa]
        r = client.put_object(Bucket="uniopen-data", Key="unipd/mensa.json", Body=json.dumps(details))

    return "Done"

main({"what": "menu"}, 1)