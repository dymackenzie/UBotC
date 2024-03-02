import boto3 as bt


def setUpAgent():
    region = 'us-west-2'

    #client = bt.client(service_name='bedrock-runtime')
    client = bt.client('bedrock-agent-runtime')

    UBotC_agentId = 'Y4WJ0YT1MQ'
    UBotC_agentAliasId='UBotC:1'
    UBotC_agentAliasName = 'UBotCv2'
    testAliasId ='TSTALIASID'
    testVersion = 'DRAFT'

    # prepare_response = client.prepare_agent(
    #     agentId=UBotC_agentId
    # )

    # print (prepare_response['agentVersion'])

    # get_agent_response = client.get_agent(
    #     agentId=UBotC_agentId
    # )

    # print (get_agent_response['agent']['agentName'])



    

    # create_alias_response = client.create_agent_alias(
    # agentId=UBotC_agentId,
    # agentAliasName=UBotC_agentAliasName,
    # routingConfiguration=[
    #     {
    #         'agentVersion': testVersion
    #     },
    # ]
    # )

    # print(create_alias_response['agentAlias'])

    invoke_response = client.invoke_agent(
        agentId = UBotC_agentId,
        agentAliasId=testAliasId,
        sessionId='attempt1', 
        inputText='Which CPSC course is the easiest?'
    )

    for i in (invoke_response['completion']):
        print(i)

setUpAgent()

# def retrieve(query, numberOfResults=5):
#     global brt
#     return brt.retrieve(
#         retrievalQuery= {
#             'text': query
#         },
#         knowledgeBaseId="BK6RACYVK8",
#         retrievalConfiguration= {
#             'vectorSearchConfiguration': {
#                 'numberOfResults': numberOfResults
#             }
#         }
#     )
# response = retrieve("What is Amazon Bedrock?", "AES9P3MT9T")["retrievalResults"]

