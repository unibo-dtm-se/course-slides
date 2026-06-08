import argparse
import sys

from exam import *


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("questions_file", nargs="?", default=DEFAULT_QUESTIONS_FILE)
	parser.add_argument(
		"--white-list",
		"--whitelist",
		dest="white_list",
		action="append",
		default=None,
		metavar="CATEGORY",
		help="Include only the specified category. Repeat the flag to include multiple categories.",
	)
	parser.add_argument(
		"--black-list",
		"--blacklist",
		dest="black_list",
		action="append",
		default=None,
		metavar="CATEGORY",
		help="Exclude the specified category. Repeat the flag to exclude multiple categories.",
	)
	return parser.parse_args()


def resolve_categories(parser, questions, categories, option_name):
	if categories is None:
		return None
	try:
		return {questions.category(category) for category in categories}
	except KeyError as error:
		parser.error(f"{option_name}: {error}")


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("questions_file", nargs="?", default=DEFAULT_QUESTIONS_FILE)
	parser.add_argument(
		"--white-list",
		"--whitelist",
		dest="white_list",
		action="append",
		default=None,
		metavar="CATEGORY",
		help="Include only the specified category. Repeat the flag to include multiple categories.",
	)
	parser.add_argument(
		"--black-list",
		"--blacklist",
		dest="black_list",
		action="append",
		default=None,
		metavar="CATEGORY",
		help="Exclude the specified category. Repeat the flag to exclude multiple categories.",
	)

	args = parser.parse_args()
	questions = QuestionsStore(args.questions_file)
	white_list = resolve_categories(parser, questions, args.white_list, "--white-list")
	black_list = resolve_categories(parser, questions, args.black_list, "--black-list")

	tree = questions.to_xml(white_list=white_list, black_list=black_list)
	tree.write(sys.stdout, encoding="unicode", xml_declaration=True)


if __name__ == "__main__":
	main()
