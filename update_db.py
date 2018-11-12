import os.path
import json
import argparse


def load_json_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return json.load(file)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--filepath',
        help='a JSON file with ads info for database update '
             '(default value: ads.json)',
        default='ads.json',
        type=str,
    )
    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    filepath = command_line_arguments.filepath


if __name__ == '__main__':
    main()
