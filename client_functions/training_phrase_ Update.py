# import os
#
# import google
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"

from google.cloud import dialogflow
from google.oauth2 import service_account

# import dialogflow_v2


credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')
def update_intent(project_id, intent_id, training_phrases_parts):
    client = dialogflow.IntentsClient(credentials=credentials)
    intent_name = client. intent_path(project_id, intent_id)
    intent = client.get_intent(name=intent_name)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    print(intent.training_phrases)
    intent.training_phrases.extend(training_phrases)
    response  = client.update_intent(intent=intent, language_code='en')

update_intent('legend-tfsf',"0868764a-ff10-4c08-bd6c-30538bf82b21", ["hello google","hello amazon","hello apple"])
