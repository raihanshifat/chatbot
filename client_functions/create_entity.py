import dialogflow_v2
# import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')

from google.oauth2 import service_account


def create_entity(project_id, entity_type_id, entity_value, synonyms):
    """Create an entity of the given entity type."""
    import dialogflow_v2 as dialogflow
    entity_types_client = dialogflow.EntityTypesClient(credentials=credentials)

    # Note: synonyms must be exactly [entity_value] if the
    # entity_type's kind is KIND_LIST


    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity = dialogflow.types.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms.extend(synonyms)

    response = entity_types_client.batch_create_entities(
        entity_type_path, [entity])

    print('Entity created: {}'.format(response))
# def create_entity_type(project_id, display_name, kind):
#     """Create an entity type with the given display name."""
#     import dialogflow_v2 as dialogflow
#     entity_types_client = dialogflow.EntityTypesClient()
#
#     parent = entity_types_client.project_agent_path(project_id)
#     entity_type = dialogflow.types.EntityType(
#         display_name=display_name, kind=kind)
#
#     response = entity_types_client.create_entity_type(parent, entity_type)
#
#     print('Entity type created: \n{}'.format(response))
project_id="legend-tfsf"
display_name="HellWorldv4"
kind=1
# create_entity_type(project_id, display_name, kind)
# create_entity(project_id, "0a5c3be4-40df-4f63-a5dc-88fa79989aec", "ML", ["py","java"])
# import dialogflow_v2
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/rayhan/Downloads/legend-tfsf-781206294359.json"
#
# from google.oauth2 import service_account
#
# credentials = service_account.Credentials.from_service_account_file("/home/rayhan/Downloads/legend-tfsf-781206294359.json")
# client = dialogflow_v2.EntityTypesClient(credentials=credentials)
# parent = client.project_agent_path('legend-tfsf')
# entity_type = {
#   "displayName": "hellow",
#   "kind": 1,
#   "entities": [
#     {
# "value":"python",
#   "synonyms": [
#     "py"
#   ]
#     }
#   ]
# }
# response = client.create_entity_type(parent, entity_type)

def create_batch_entity(project_id, entity_type_id, entity_dic):
    for key,value in entity_dic.items():
        create_entity(project_id, entity_type_id, key, value)
data_dict={'Python':["python"],'Java':["java"],'C++':["C++"],'Machine Learning':["machine learning"],'Deep Learning':["deep learning"],'Web Development':["web development"]}
create_batch_entity(project_id, "c5853e7e-36b0-41a1-86e9-102611bab5b6",data_dict)