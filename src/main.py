import os
from typing import Dict

from directories import Directory

commands: Dict = {
    "CREATE": "create",
    "MOVE": "move",
    "DELETE": "delete",
    "LIST": "list",
}


def main() -> None:
    directory: Directory = Directory()

    with open(os.path.join(os.path.dirname(__file__), "instructions.txt"), "r") as file:
        instructions = file.read().splitlines()
        for instruction in instructions:
            print(instruction)
            instruction = instruction.split(" ", 1)
            command = commands.get(instruction[0])
            if command == "list":
                getattr(directory, command)()
            else:
                arguments = instruction[1]
                getattr(directory, command)(arguments)


if __name__ == "__main__":
    main()
