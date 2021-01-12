import dialogflow_v2
# import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rayhan/Downloads/legend-tfsf-781206294359.json"
import Utilities

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(r'legend-tfsf-781206294359.json')

from google.oauth2 import service_account
def create_entity_type(project_id, display_name, kind):
    """Create an entity type with the given display name."""
    import dialogflow_v2 as dialogflow
    entity_types_client = dialogflow.EntityTypesClient(credentials=credentials)

    parent = entity_types_client.project_agent_path(project_id)
    entity_type = dialogflow.types.EntityType(
        display_name=display_name, kind=kind)

    response = entity_types_client.create_entity_type(parent, entity_type)

    print('Entity type created: \n{}'.format(response))
# create_entity_type(Utilities.Project_ID,"course_price",1)