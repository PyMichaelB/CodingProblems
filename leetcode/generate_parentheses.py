from typing import List, Tuple


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        prev_solutions = ["("]  # We must always start with an open bracket
        temp = []

        while prev_solutions != temp:
            prev_solutions = self.add_possible_combinations(prev_solutions, n)  # i.e. Updates are made
            temp = prev_solutions

        return prev_solutions

    def add_possible_combinations(self, current_solutions: List[str], n: int) -> List[str]:
        new_solutions = []

        for sol in current_solutions:

            opened, closed = self.count_open(sol)
            if closed < opened:
                if 0 < opened < n:
                    new_solutions.append(sol + "(")  # Can open OR close a bracket
                new_solutions.append(sol + ")")

            elif opened == closed and opened != n:
                new_solutions.append(sol + "(")  # Can open a bracket
            else:
                new_solutions.append(sol)

        return new_solutions

    def count_open(self, solution: str) -> Tuple[int, int]:
        count_open = count_closed = 0

        for char in solution:
            if char == "(":
                count_open += 1
            elif char == ")":
                count_closed += 1

        return count_open, count_closed
