# tests/test_scenario_agent.py
import unittest
import sys
import os

# Add the 'src' directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.agents.scenario_agent import ScenarioAgent

class TestScenarioAgent(unittest.TestCase):
    def setUp(self):
        self.agent = ScenarioAgent("job_interview")  # Use an existing scenario

    def test_start_new_session(self):
        initial_message = self.agent.start_new_session()
        self.assertIsInstance(initial_message, str)
        self.assertTrue(len(initial_message) > 0)

if __name__ == '__main__':
    unittest.main()