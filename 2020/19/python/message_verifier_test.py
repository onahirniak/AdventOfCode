import unittest
from message_verifier import MessageVerifier
from readers.message_reader import MessageReader
from readers.rules_reader import RulesReader
import os.path

class MessageVerifierTests(unittest.TestCase):

    def test_given_by_platform_input(self):
        # Arrange
        message_reader = MessageReader()
        rules_reader = RulesReader()

        messages = message_reader.read_messages(os.path.dirname(__file__) + '/data/messages_testcase_1.txt')
        rules = rules_reader.read_rules(os.path.dirname(__file__) + '/data/rules_testcase_1.txt')

        # Act
        verifier = MessageVerifier()
        validMessages = verifier.verify_messages(rules, messages)

        # Assert
        self.assertEqual(validMessages, 285)


if __name__ == '__main__':
    unittest.main() 