import dialogflow_v2beta1
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"


from google.oauth2 import service_account
# from Utilities import Project_ID
import client_functions.Utilities
from google.cloud import dialogflow

credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')
def list_intents(project_id,intent_name):
    # from google.cloud import dialogflow
    intents_client = dialogflow.IntentsClient(credentials=credentials)

    parent = dialogflow.AgentsClient.agent_path(project_id)

    intents = intents_client.list_intents(request={'parent': parent})

    # for intent in intents:
    #     print('=' * 20)
    #     print('Intent name: {}'.format(intent.name))
    #     print('Intent display_name: {}'.format(intent.display_name))
    #     print('Action: {}\n'.format(intent.action))
    #     print('Root followup intent: {}'.format(
    #         intent.root_followup_intent_name))
    #     print('Parent followup intent: {}\n'.format(
    #         intent.parent_followup_intent_name))
    #
    #     print('Input contexts:')
    #     for input_context_name in intent.input_context_names:
    #         print('\tName: {}'.format(input_context_name))
    #
    #     print('Output contexts:')
    #     for output_context in intent.output_contexts:
    #         print('\tName: {}'.format(output_context.name))
    intent=list(filter(lambda x:x.display_name==intent_name,intents))
    intent_id=intent[0].name
    intent_id=intent_id.split("/")
    intent_id=intent_id[-1]
    # print(intent_id)
    return intent_id
# list_intents("legend-tfsf","A")