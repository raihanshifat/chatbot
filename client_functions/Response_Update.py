import dialogflow_v2beta1
# import os

# import google

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"

from google.oauth2 import service_account
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict, MessageToJson, Parse
from proto.marshal.collections.repeated import Repeated
from google.protobuf import field_mask_pb2


credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')

def update_intent_response(project_id, intent_id, response_part):
    client = dialogflow.IntentsClient(credentials=credentials)
    intent_name = client.intent_path(project_id, intent_id,)
    intent = client.get_intent(name=intent_name)
    response_list = [response_part]
    text = dialogflow.Intent.Message.Text(text=response_list)
    message = dialogflow.Intent.Message(text=text)
    intent.messages[0].text.text.extend(message.text.text)
    update_mask = field_mask_pb2.FieldMask(paths=['messages'])
    response  = client.update_intent(intent=intent,language_code='en',update_mask=update_mask)
# client = dialogflow.IntentsClient()
# intent_name = client.intent_path('legend-tfsf','900dcd6f-ebcc-4da5-bd2a-5cb1ee7591c3')
# # print(intent_name)
# intent = client.get_intent(name=intent_name)
# # print(intent)
# response_list = ['text response hello ']
# text = dialogflow.Intent.Message.Text(text=response_list)
# message = dialogflow.Intent.Message(text=text)
# # print(message.text)
# # print(intent.messages[0].text.append({message.text}))
# # intent.messages[0].text.extend([message.text])
# # # response  = client.'(intent, language_code='en')
# # response  = client.update_intent(intent=intent,language_code='en')
# # intent.messages[0].text.text.append(response)
# # intent.messages[0].text.extend([message[0].text])
# print(intent.messages[0].text.text)
# print(message.text.text)
# intent.messages[0].text.text.extend(message.text.text)
# response  = client.update_intent(intent=intent,language_code='en')
def update_batch_response(project_id, intent_id, response_parts):
    for response_part in response_parts:
        update_intent_response(project_id, intent_id, response_part)
# update_batch_response('legend-tfsf',"186718a8-5036-4f48-997e-b2afa8961b92",["Dusk Till Dawn","Tears Dont Fall","Pycharm Community Edition"])






