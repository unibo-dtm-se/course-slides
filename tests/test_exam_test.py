import unittest

from exam import Question, QuestionsStore
from exam.test import TestGenerator, parse_args


class TestGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.questions = QuestionsStore([
            Question(category="A", weight=1, id="A-1"),
            Question(category="A", weight=1, id="A-2"),
            Question(category="B", weight=1, id="B-1"),
        ])

    def test_different_categories_is_enabled_by_default(self):
        solutions = list(TestGenerator(self.questions, 2, {"A"}).solutions)

        self.assertTrue(solutions)
        for solution in solutions:
            self.assertEqual(len(solution.categories), len(solution.questions))

    def test_different_categories_can_be_disabled(self):
        solutions = list(TestGenerator(
            self.questions,
            2,
            {"A"},
            different_categories=False,
        ).solutions)

        self.assertTrue(any(len(solution.categories) < len(solution.questions) for solution in solutions))

    def test_command_line_switch_is_default_on_and_can_be_disabled(self):
        self.assertTrue(parse_args([]).different_categories)
        self.assertFalse(parse_args(["--no-different-categories"]).different_categories)


if __name__ == "__main__":
    unittest.main()
