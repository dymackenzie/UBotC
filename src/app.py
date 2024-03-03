import streamlit as st
import boto3 as bt
from botocore.config import Config
import json

def initApp():

    initStreamlit()

    config = Config(read_timeout=1000)
    client = bt.client('bedrock-agent-runtime', 
                      config=config)

    prompt_template = """
    Make it as elaborate as possible.

    Remove <b> and </b> if possible.
    """

    prompt = st.session_state.get("prompt", [{"role": "system", "content": "none"}])

    # this displays the previous chat messages for history
    for message in prompt:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])
    
    # grab question from the user
    question = st.chat_input("AMA -- ask me anything 🤓☝️")

    # Handle the user's question
    if question:

        prompt[0] = {"role": "system", "content": prompt_template,}

        # append the user's question to the end of the response for history
        prompt.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # while waiting for assistant message, keep the message as empty
        with st.chat_message("assistant"):
            bot_response = st.empty()
            bot_response.write("...")

        # format the API 
        UBotC_agentId = 'Y4WJ0YT1MQ'
        testAliasId ='1XDRVQJNUG' #changed to ubotcv3 from TSTALIASID
        invoke_response = client.invoke_agent(
            agentId = UBotC_agentId,
            agentAliasId = testAliasId,
            sessionId = 'attempt1',
            inputText = prompt[0]['content'] + prompt[len(prompt) - 1]['content']
        )

        # get the response and write it
        text = ""
        for chunk in invoke_response['completion']:
            text += chunk["chunk"]["bytes"].decode("utf-8")
        # text = response_body.get('completion')
        if text is not None:
            bot_response.write(text)

        # add the bot's response to the prompt
        prompt.append({"role": "assistant", "content": text})
        # store it in the session state
        st.session_state["prompt"] = prompt


def initStreamlit():

    # initiate title
    st.title("UBotC 🤓☝️")

    # information
    st.markdown(
    """ 
        ####  Chat with a bot trained on UBC courses! Ask questions that you might have about any UBC course we will try to answer as best we can!
        ----
    """
    )