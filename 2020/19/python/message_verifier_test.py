import unittest
from message_verifier import MessageVerifier
from readers.message_reader import MessageReader
from readers.rules_reader import RulesReader
import os.path

class MessageVerifierTests(unittest.TestCase):


    def test_given_by_platform_input_part_1(self):
        # Arrange
        message_reader = MessageReader()
        rules_reader = RulesReader()

        messages = message_reader.read_messages(os.path.dirname(__file__) + '/data/messages_testcase_1.txt')
        rules = rules_reader.read_rules(os.path.dirname(__file__) + '/data/rules_testcase_1.txt')

        # Act
        verifier = MessageVerifier()
        validMessages = verifier.verify_messages_part_one(rules, messages)

        # Assert
        self.assertEqual(validMessages, 285)

    def test_given_by_platform_input_part_2(self):
        # Arrange
        message_reader = MessageReader()
        rules_reader = RulesReader()

        messages = message_reader.read_messages(os.path.dirname(__file__) + '/data/messages_testcase_1.txt')
        rules = rules_reader.read_rules(os.path.dirname(__file__) + '/data/rules_testcase_1.txt')

        rules['8'] = [(42), (42, 8)]
        rules['11'] = [(42, 31), (42, 11, 31)]

        # Act
        verifier = MessageVerifier()
        validMessages = verifier.verify_messages_part_two(rules, messages)

        # Assert
        self.assertEqual(validMessages, 412)

if __name__ == '__main__':
    unittest.main() 