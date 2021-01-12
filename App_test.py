import unittest
from unittest.mock import  Mock,MagicMock,patch
import Detect_Intent
from Detect_Intent import detect_intent_texts
from client_functions.Create_Intent import create_intent
from client_functions.create_entity import create_entity
from client_functions.Create_entity_type import create_entity_type
from client_functions.list_intent import list_intents
from client_functions.Response_Update import update_intent_response
from client_functions.Training_phrase_update import  update_intent



class MyTestCase(unittest.TestCase):
    @patch('Detect_Intent.dialogflow',spec=True,spec_set=True)
    def test_detect_intent_texts(self,mock_SessionsClient):
        x=detect_intent_texts('a','b','c','d')
        mock_SessionsClient.SessionsClient.return_value.session_path.assert_called_with('a','b')
        self.assertIsNotNone(x)
    @patch('Create_Intent.dialogflow',spec=True,spec_set=True)
    def test_create_intent(self,mock):
    @patch('Detect_Intent.dialogflow', spec=True, spec_set=True)
    @patch('Detect_Intent.dialogflow', spec=True, spec_set=True)
    @patch('Detect_Intent.dialogflow', spec=True, spec_set=True)
    @patch('Detect_Intent.dialogflow', spec=True, spec_set=True)
    @patch('Detect_Intent.dialogflow', spec=True, spec_set=True)






if __name__ == '__main__':
    unittest.main()
