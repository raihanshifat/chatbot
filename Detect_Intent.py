import dialogflow_v2beta1
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"

from google.oauth2 import service_account
from google.cloud import dialogflow

credentials = service_account.Credentials.from_service_account_file("legend-tfsf-781206294359.json")
def detect_intent_texts(project_id, session_id, texts,language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient(credentials=credentials)

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.TextInput(
            text=text,language_code = language_code)


        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={'session': session, 'query_input': query_input})

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        return ('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
# detect_intent_texts("legend-tfsf",1,[" আমার একটি চাকরি দরকার","i can not save my profile"],"en")