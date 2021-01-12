import google
import mysql.connector
from client_functions.Create_Intent import create_intent
from client_functions.list_intent import list_intents
from client_functions.Training_phrase_update import update_intent
from client_functions.Response_Update import update_batch_response
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"
from client_functions.Utilities import Project_ID
mydata= mysql.connector.connect(host="localhost",user="rayhan",password="123",database="practice")
with mydata.cursor() as mycursor:
    sqldata = f"""SELECT distinct intent FROM Training_phrase
                  """
    mycursor.execute(sqldata)
    intent_class=mycursor.fetchall()
    intent_list=[]
    for i in range(len(intent_class)):
        intent_list.append(intent_class[i][0])
for intent in intent_list:
    print(i)
    with mydata.cursor() as mycursor:
        sqldata = f"""SELECT training_phrase FROM Training_phrase
                        where intent='{intent}'
                      """
        mycursor.execute(sqldata)
        training_phrases = mycursor.fetchall()
    training_phrases_list=[]
    for i in range(len(training_phrases)):
        training_phrases_list.append(training_phrases[i][0])
    # print(training_phrases_list)

    with mydata.cursor() as mycursor:
        sqldata = f"""SELECT response_phrase FROM response_phrase
                        where intent='{intent}'
                      """
        mycursor.execute(sqldata)
        response_phrases = mycursor.fetchall()
    response_phrases_list = []
    for i in range(len(response_phrases)):
        response_phrases_list.append(response_phrases[i][0])
    try:
        create_intent("legend-tfsf",intent,training_phrases_list,response_phrases_list)
    except google.api_core.exceptions.InvalidArgument as e:
        intent_id=list_intents("legend-tfsf",intent)
        try:
            update_intent("legend-tfsf",intent_id,training_phrases_list)
        except Exception as e:
            print(e)
        finally:
            try:
                update_batch_response("legend-tfsf",intent_id,response_phrases_list)
            except Exception as e:
                print(e)






    # google.api_core.exceptions.InvalidArgument

# def implicit():
#     from google.cloud import storage
#
#     # If you don't specify credentials when constructing the client, the
#     # client library will look for credentials in the environment.
#     storage_client = storage.Client()
#
#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)
