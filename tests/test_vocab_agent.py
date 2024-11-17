# tests/test_vocab_agent.py
import unittest
import sys
import os

# Add the 'src' directory to sys.path to import VocabAgent
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.agents.vocab_agent import VocabAgent
from langchain_core.chat_history import InMemoryChatMessageHistory

class TestVocabAgent(unittest.TestCase):
    def setUp(self):
        self.agent = VocabAgent()

    def test_restart_session(self):
        initial_message = self.agent.restart_session()
        self.assertIsInstance(initial_message, InMemoryChatMessageHistory)
        self.assertEqual(len(initial_message.messages), 0)

if __name__ == '__main__':
    unittest.main()