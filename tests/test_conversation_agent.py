# tests/test_conversation_agent.py
import unittest
import sys
import os

# Add the 'src' directory to sys.path to import ConversationAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.agents.conversation_agent import ConversationAgent

class TestConversationAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ConversationAgent()

    def test_initialization(self):
        self.assertEqual(self.agent.name, "conversation")
        self.assertEqual(self.agent.prompt_file, "prompts/conversation_prompt.txt")
        self.assertIsNotNone(self.agent.session_id)

if __name__ == '__main__':
    unittest.main()