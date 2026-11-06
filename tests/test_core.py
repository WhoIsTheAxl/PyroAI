import unittest
from pyroai.core import (Action, Experience, Feedback, FeedbackStatus, Observation,
                         StepResult, TaskDefinition, TaskInstance, TaskOutcome, TaskStatus)
from pyroai.environments import TicTacToeEnvironment

class CoreTests(unittest.TestCase):
    def test_action_is_deeply_immutable_and_detached(self):
        source = {"nested": [1, 2]}
        action = Action("move", source)
        source["nested"].append(3)
        self.assertEqual(action.parameters["nested"], (1, 2))
        with self.assertRaises(TypeError): action.parameters["nested"] = ()

    def test_observation_mutable_copy_is_detached(self):
        observation = Observation({"board": [[None]]})
        mutable = observation.mutable_copy()
        mutable["board"][0][0] = "X"
        self.assertIsNone(observation.data["board"][0][0])

    def test_task_lifecycle(self):
        task = TaskInstance(TaskDefinition("Test"))
        task.start()
        task.complete(TaskOutcome.SUCCESS)
        self.assertEqual(task.status, TaskStatus.COMPLETED)
        self.assertEqual(task.outcome, TaskOutcome.SUCCESS)

    def test_experience_accepts_standard_transition(self):
        obs, nxt = Observation({"n": 0}), Observation({"n": 1})
        feedback = Feedback(True, FeedbackStatus.SUCCESS)
        item = Experience(obs, Action("increment"), feedback, nxt, TaskStatus.ACTIVE)
        self.assertEqual(item.next_observation.data["n"], 1)

class TicTacToeTests(unittest.TestCase):
    def setUp(self):
        self.env = TicTacToeEnvironment()
        self.env.reset()

    def move(self, row, column):
        return self.env.execute(Action("place", {"row": row, "column": column}))

    def test_valid_move_updates_board_and_player(self):
        result = self.move(0, 0)
        self.assertTrue(result.feedback.accepted)
        self.assertEqual(result.observation.data["board"][0][0], "X")
        self.assertEqual(result.observation.data["current_player"], "O")

    def test_occupied_cell_is_rejected_without_mutation(self):
        self.move(0, 0)
        result = self.move(0, 0)
        self.assertFalse(result.feedback.accepted)
        self.assertEqual(result.feedback.status, FeedbackStatus.REJECTED)
        self.assertEqual(result.observation.data["current_player"], "O")

    def test_win_completes_task(self):
        for move in [(0,0), (1,0), (0,1), (1,1), (0,2)]:
            result = self.move(*move)
        self.assertEqual(result.task_status, TaskStatus.COMPLETED)
        self.assertEqual(result.task_outcome, TaskOutcome.SUCCESS)
        self.assertEqual(result.observation.data["winner"], "X")

    def test_invalid_coordinates_are_rejected(self):
        result = self.move(3, 0)
        self.assertEqual(result.feedback.status, FeedbackStatus.REJECTED)

if __name__ == '__main__':
    unittest.main()