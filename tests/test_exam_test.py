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

    def test_minimum_questions_can_be_set(self):
        questions = QuestionsStore([
            Question(category="A", weight=1, id="A-1"),
            Question(category="B", weight=1, id="B-1"),
            Question(category="C", weight=2, id="C-1"),
        ])

        solutions = list(TestGenerator(
            questions,
            2,
            set(),
            min_questions=2,
        ).solutions)

        self.assertTrue(solutions)
        self.assertTrue(all(len(solution.questions) >= 2 for solution in solutions))

    def test_minimum_questions_defaults_to_target_category_count(self):
        args = parse_args([])
        self.assertIsNone(args.min_questions)
        self.assertEqual(parse_args(["--min-questions", "4"]).min_questions, 4)

        generator = TestGenerator(self.questions, 2, {"A", "A"})
        self.assertTrue(list(generator.solutions))

    def test_negative_minimum_questions_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            TestGenerator(self.questions, 2, {"A"}, min_questions=-1)


if __name__ == "__main__":
    unittest.main()
