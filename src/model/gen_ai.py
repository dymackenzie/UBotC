import boto3 as bt
import json
brt


def gen_model():
    global brt 
    brt = bt.client(service_name='bedrock-runtime')
    
    userQuestion = "Hello! what colour is the sky?"     # get user question, (from ui)?

    body = json.dumps({
        "prompt": "\n\nHuman: " + userQuestion + "\n\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 0.1,
        "top_p": 0.9,
    })
    

    modelId = 'anthropic.claude-v2:1'
    accept = 'application/json'
    contentType = 'application/json'

    response = brt.invoke_model(body = body, modelId = modelId, accept = accept, contentType = contentType)

    response_body = json.loads(response.get('body').read())

    print(response_body.get('completion'))

def retrieve(query, numberOfResults=5):
    global brt
    return brt.retrieve(
        retrievalQuery= {
            'text': query
        },
        knowledgeBaseId="BK6RACYVK8" 
        retrievalConfiguration= {
            'vectorSearchConfiguration': {
                'numberOfResults': numberOfResults
            }
        }
    )

#response = retrieve("What is Amazon Bedrock?", "AES9P3MT9T")["retrievalResults"]

def setUpAgent():
    region = 'us-west-2'

    client = bt.client(service_name='bedrock-runtime')

    UBotC_agentId = 'Y4WJ0YT1MQ',
    UBotC_agentAliasId='UBotC:1',
    testAliasId ='TSTALIASID'
    testVersion = 'DRAFT'

    prepare_response = bt.client.prepare_agent(
        agentId=UBotC_agentId
    )

    print (prepare_response['agentVersion'])

    # get_agent_response = client.get_agent(
    # agentId=UBotC_agentId
    # )



    

    create_alias_response = client.create_agent_alias(
    agentId='string',
    agentAliasName='string',
    clientToken='string',
    description='string',
    routingConfiguration=[
        {
            'agentVersion': 'string'
        },
    ],
    tags={
        'string': 'string'
    }
    )

    # invoke_response = bt.client.invoke_agent(
    # agentId = 'Y4WJ0YT1MQ',
    # agentAliasId='UBotC:1',
    # sessionId='string', !!!
    # endSession=True|False,
    # enableTrace=True|False,
    # inputText='string'
    # )
setUpAgent()