import json
import os
import sys
import boto3 as bt

from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

boto3_bedrock = bt.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None),
    runtime=False
)

boto3_bedrock.list_foundation_models()

# modelId = "anthropic.claude-v2"
# cl_llm = Bedrock(
#     model_id=modelId,
#     client=boto3_bedrock,
#     model_kwargs={"max_tokens_to_sample": 1000},
# )

