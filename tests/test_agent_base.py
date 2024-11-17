# tests/test_agent_base.py
import unittest
import sys
import os

# Add the 'src' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.agents.agent_base import AgentBase

class TestAgentBase(unittest.TestCase):
    def setUp(self):
        self.agent = AgentBase(
            name="test_agent",
            prompt_file="prompts/job_interview_prompt.txt",
            intro_file="content/intro/job_interview.json"
        )

    def test_load_prompt(self):
        prompt = self.agent.load_prompt()
        self.assertIsInstance(prompt, str)
        self.assertTrue(len(prompt) > 0)

    def test_load_intro(self):
        intro_messages = self.agent.load_intro()
        self.assertIsInstance(intro_messages, list)
        self.assertTrue(len(intro_messages) > 0)

if __name__ == '__main__':
    unittest.main()