"""
    Azure Functions HTTP Example Code for Python

    Created by Anthony Eden
    http://MediaRealm.com.au/
"""

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))

import json
from AzureHTTPHelper import HTTPHelper
from twilio.rest import TwilioRestClient

# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()

# All these print statements get sent to the Azure Functions live log
print "--- GET ---"
print http.get
print

print "--- POST ---"
print http.post
print

print "--- HEADERS ---"
print http.headers
print

print "--- OTHER ENVIRONMENTAL VARIABLES ---"
for x in http.env:
    print x
print


def getTwilioCredentials():
    SID = os.environ['TWILIO_ACCOUNT_SID']
    TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    return SID,TOKEN

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def sendMessage(toNum, fromNum, msgBody, media):

    client.messages.create(
        to = toNum,
        from_= fromNum,
        body= msgBody,
        media_url=media,
    )
    return None

ACCOUNT_SID, AUTH_TOKEN = getTwilioCredentials()
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

sendMessage("+17037727371",
            "+17037214313",
            "Azure: Serverless Microservice Architecture in AWS",
            "https://s3.amazonaws.com/awscomputeblogmedia/Serverless+Architecture+Diagram.png"
            )
# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,

    #Response Body:
    "body": "<h1>Hey Srini! Azure Works :)</h1>",

    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))
