# UBotC



**UBotC** is a chatbot powered by Claude v2.1 from Amazon Web Services that acts as an online academic advisor. Due to the extremely unintuitive user interface of the UBC website, this bot allows you to access information and generate statistics about UBC grades, professors, course information, and pass and fail rate.

Features:
- Utilizes S3 Bucket as a secure object storage system for our UBC dataset.
- Employs Titan Embeddings to transform the dataset into vectors which allow accurate search for relevent passages.
- Through the AWS API, accesses the custom agent based on Claude v2.1 trained on the knowledge base provided and instructed through advanced prompt engineering.
- Interacts with the user through Streamlit-based UI.