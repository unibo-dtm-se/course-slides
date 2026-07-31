import unittest

from exam import Question, QuestionsStore
from exam.test import TestGenerator, parse_args, parse_question_commands


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

    def test_string_target_categories_are_enforced(self):
        questions = QuestionsStore([
            Question(category="A", weight=1, id="A-1"),
            Question(category="B", weight=1, id="B-1"),
            Question(category="C", weight=1, id="C-1"),
        ])

        solutions = list(TestGenerator(questions, 2, {"A"}).solutions)

        self.assertTrue(solutions)
        self.assertTrue(all("A-1" in {q.id for q in solution.questions} for solution in solutions))

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

    def test_question_commands_support_ranges_and_combinations(self):
        excluded, kept = parse_question_commands(
            "no Q1 Q3-Q5 keep Q2 keep Q7",
            question_count=7,
        )

        self.assertEqual(excluded, {1, 3, 4, 5})
        self.assertEqual(kept, {2, 7})

    def test_question_commands_reject_conflicts_and_invalid_indexes(self):
        with self.assertRaisesRegex(ValueError, "both replaced and kept"):
            parse_question_commands("no Q1 keep Q1", question_count=2)
        with self.assertRaisesRegex(ValueError, "between Q1 and Q2"):
            parse_question_commands("no Q3", question_count=2)

    def test_next_solution_can_replace_selected_questions_and_retain_the_rest(self):
        questions = QuestionsStore([
            Question(category="A", weight=1, id="A-1"),
            Question(category="B", weight=1, id="B-1"),
            Question(category="C", weight=1, id="C-1"),
        ])
        generator = TestGenerator(questions, 2, set())
        first = generator.next_solution()
        first_ids = {question.id for question in first.questions}
        excluded_id = next(iter(first_ids))
        retained_ids = first_ids - {excluded_id}

        second = generator.next_solution(
            required_question_ids=retained_ids,
            excluded_question_ids={excluded_id},
        )

        second_ids = {question.id for question in second.questions}
        self.assertTrue(retained_ids <= second_ids)
        self.assertNotIn(excluded_id, second_ids)

    def test_question_output_uses_numbered_command_labels(self):
        output = str(self.questions)

        self.assertIn("1. [Q1] A-1", output)
        self.assertIn("2. [Q2] A-2", output)
        self.assertIn("3. [Q3] B-1", output)


if __name__ == "__main__":
    unittest.main()
