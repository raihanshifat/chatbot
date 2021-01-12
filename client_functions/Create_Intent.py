import dialogflow_v2beta1
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"


from google.oauth2 import service_account
# from Utilities import Project_ID
import client_functions.Utilities

credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')
def create_intent(project_id, display_name, training_phrases_parts,
                  message_texts):
    """Create an intent of the given intent type."""
    from google.cloud import dialogflow
    intents_client = dialogflow.IntentsClient(credentials=credentials)
    # dialogflow.

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message])

    response = intents_client.create_intent(request={'parent':parent, 'intent': intent})

    print('Intent created: {}'.format(response))

# project_id="legend-tfsf"
# display_name="HeWorldv2"
# training_phrases_parts=["Who are you?","how Are You?"]
# message_texts=["I am Legend"]
# create_intent(project_id, display_name, training_phrases_parts,message_texts)
# create_intent("legend-tfsf", "abcd", ["tell me the price of java Course"], None)