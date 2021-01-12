# import os
#
# import google
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"

from google.cloud import dialogflow
from google.oauth2 import service_account
from google.cloud.dialogflow_v2.types import intent



credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')
def update_intent(project_id, intent_id, training_phrases_parts):
    client = dialogflow.IntentsClient(credentials=credentials)
    intent_name = client. intent_path(project_id, intent_id)
    intent2 = client.get_intent(request=intent.GetIntentRequest(intent_view=3,name=intent_name))
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)
    # print(intent2.training_phrases)
    print(intent2.training_phrases)
    intent2.training_phrases.extend(training_phrases)

    response = client.update_intent(intent=intent2, language_code='en')
    # print(intent2.training_phrases)


# update_intent('legend-tfsf',"186718a8-5036-4f48-997e-b2afa8961b92", ["google colab","hello amazon","hello apple"])