import streamlit as st
import boto3 as bt
import json

def initApp():

    initStreamlit()

    client = bt.client('bedrock-agent-runtime')

    prompt_template = """
    Make your answer as short as possible.
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

        # brt = bt.client(service_name='bedrock-runtime')

        # vectordb = st.session_state.get("vectordb", None)
        # if not vectordb:
        #     with st.message("assistant"):
        #         st.write("You need to provide a PDF")
        #         st.stop()

        # search the vectordb for similar content in comparison to user's question
        # search_results = vectordb.similarity_search(question, k=3)
        # search_results
        # pdf_extract = "/n ".join([result.page_content for result in search_results])

        # updating the prompt with the extract from the database
        # prompt[0] = {
        #     "role": "system",
        #     "content": prompt_template.format(pdf_extract=pdf_extract),
        # }

        prompt[0] = {"role": "system", "content": prompt_template,}

        # append the user's question to the end of the response for history
        prompt.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.write(question)

        # while waiting for assistant message, keep the message as empty
        with st.chat_message("assistant"):
            bot_response = st.empty()
            bot_response.write("...")

        print(prompt[0]['content'] + prompt[len(prompt) - 1]['content'])

        # format the API 
        UBotC_agentId = 'Y4WJ0YT1MQ'
        testAliasId ='TSTALIASID'
        invoke_response = client.invoke_agent(
            agentId = UBotC_agentId,
            agentAliasId = testAliasId,
            sessionId = 'attempt1',
            inputText = prompt[0]['content'] + prompt[len(prompt) - 1]['content']
        )    
        
        # body = json.dumps({
        #     "prompt": "\n\nHuman: " + prompt[0]['content'] + prompt[len(prompt) - 1]['content'] + "\n\nAssistant:",
        #     "max_tokens_to_sample": 300,
        #     "temperature": 0.1,
        #     "top_p": 0.9,
        # })

        # load request from model
        # response = client.invoke_model(body = body, modelId = 'anthropic.claude-v2:1', accept = 'application/json', contentType = 'application/json')
        # response_body = json.loads(invoke_response.get('body').read())

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
    st.title("UBotC")

    # information
    st.markdown(
    """ 
        ####  Chat with a bot trained on UBC courses! Ask questions that you might 
        ----
    """
    )