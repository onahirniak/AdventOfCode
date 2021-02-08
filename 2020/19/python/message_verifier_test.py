import unittest
from message_verifier import MessageVerifier
from readers.message_reader import MessageReader
from readers.rules_reader import RulesReader
import os.path

class MessageVerifierTests(unittest.TestCase):

    def test_given_by_platform_input(self):
        
        message_reader = MessageReader()

        messages = message_reader.read_messages(os.path.dirname(__file__) + '/data/messages_testcase_1.txt')

        rules_reader = RulesReader()

        rules = rules_reader.read_rules(os.path.dirname(__file__) + '/data/rules_testcase_1.txt')

        verifier = MessageVerifier()

        validMessages = verifier.verify_messages(rules, messages)

        self.assertEqual(validMessages, 285)


if __name__ == '__main__':
    unittest.main() 