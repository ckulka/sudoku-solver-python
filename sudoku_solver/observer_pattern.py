from __future__ import annotations

import copy
from typing import Optional


class Field:
    """Represents a field in the Sudoku"""

    def __init__(self, number):
        self.observer = []
        self.number = number

        if number is None:
            self.options = set(range(1, 10))

    def subscribe(self, observer):
        """
        Subscribe to this field to be notified when a number is set.
        """
        self.observer.append(observer)

    def notify(self, number: int):
        """
        Invoked when a field that this field is observing has been determined.
        """
        if self.number is not None:
            return

        self.options.discard(number)
        if len(self.options) == 1:
            self.set_number(self.options.pop())

    def set_number(self, number: int):
        self.number = number
        for observer in self.observer:
            observer.notify(number)


class DependentFields:
    """A group of fields that are in a relationship, e.g. a row or column."""

    def __init__(self):
        self.fields = []

    def subscribe(self, field: Field):
        self.fields.append(field)
        field.subscribe(self)

    def notify(self, number: int):
        """
        If a field in this group has an update, notify all other fields
        in this group.
        """
        for f in self.fields:
            f.notify(number)


class Sudoku:
    def __init__(self, sudoku):
        self.fields = []
        self.rows = list(map(lambda _: DependentFields(), range(9)))
        self.columns = list(map(lambda _: DependentFields(), range(9)))
        self.quadrants = list(map(lambda _: DependentFields(), range(9)))

        for y in range(9):
            for x in range(9):
                field = Field(sudoku[y][x])

                self.fields.append(field)
                self.rows[y].subscribe(field)
                self.columns[x].subscribe(field)

                quadrant_x_offset = int(x / 3)
                quadrant_y_offset = int(y / 3) * 3
                quadrant_index = quadrant_x_offset + quadrant_y_offset
                self.quadrants[quadrant_index].subscribe(field)

    def print(self):
        for y in range(9):
            if y % 3 == 0:
                print("")

            for x in range(9):
                if x % 3 == 0:
                    print(" ", end="")

                field = self.fields[y * 9 + x]
                if field.number is None:
                    print("   ", end="")
                else:
                    print(f" {field.number} ", end="")
            print("")

    def is_solved(self) -> bool:
        """
        :return: True if the Sudoku is solved, False otherwise
        """
        # Assert every number is in every row, column and quadrant.
        # By extension, this also makes sure that
        # - there are no empty fields
        # - there are no duplicate numbers

        for number in range(1, 10):
            for row in self.rows:
                if not any(field.number == number for field in row.fields):
                    return False
            for column in self.columns:
                if not any(field.number == number for field in column.fields):
                    return False
            for quadrant in self.quadrants:
                if not any(field.number == number for field in quadrant.fields):
                    return False

        return True

    def solve(self, update_options=True) -> Optional[Sudoku]:
        """
        Attempt to solve this Sudoku.

        :return: A solved Sudoku, None otherwise
        """

        # print("Attempting to solve Sudoku")
        # self.print()

        # Update the options for all undetermined fields
        if update_options:
            for field in self.fields:
                if field.number is not None:
                    field.set_number(field.number)
            # print("Updated all options")
            # self.print()

        for index in range(len(self.fields)):
            field = self.fields[index]
            if field.number is not None:
                continue

            for number in field.options:
                # print(f"{index}: testing {number}")
                sandbox = copy.deepcopy(self)
                sandbox_field = sandbox.fields[index]
                sandbox_field.set_number(number)
                sandbox = sandbox.solve(False)

                # The number resulted in a valid solution, therefore return it
                if sandbox is not None:
                    # print(f"{index}: {number} was valid!")
                    return sandbox

            # All available numbers were tested, but none
            # resulted in a correctly solved Sudoku
            # print(f"{index}: no solutions found, stepping back")
            return None

        # There are no undetermined fields left, therefore return this
        # Sudoku if it's solved, otherwise return None
        # print(f"All fields set, result is: {self.is_solved()}")
        return self if self.is_solved() else None
