import json
import boto3

client = boto3.client('sns')

def send_sms(PhoneNumber='',Message=''):
    response= client.publish(
        PhoneNumber='+8618910261245',
#        PhoneNumber='+8613261992681',
        Message=Message,
        Subject='First SMS'
    )


if __name__ == '__main__':
    send_sms()
    #print(response.get('MessageId'))
    #print(response)
