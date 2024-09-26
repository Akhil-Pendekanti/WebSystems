from typing import List, Union

class Calculation:
    def __init__(self, operation: str, operands: List[Union[int, float]]):
        self.operation = operation
        self.operands = operands

    def execute(self) -> float:
        if self.operation == 'add':
            return sum(self.operands)
        elif self.operation == 'subtract':
            return self.operands[0] - self.operands[1]
        elif self.operation == 'multiply':
            result = 1
            for operand in self.operands:
                result *= operand
            return result
        elif self.operation == 'divide':
            if self.operands[1] == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return self.operands[0] / self.operands[1]

class Calculator:
    history: List[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        calc = Calculation('add', [a, b])
        Calculator.history.append(calc)
        return calc.execute()

    @staticmethod
    def subtract(a: float, b: float) -> float:
        calc = Calculation('subtract', [a, b])
        Calculator.history.append(calc)
        return calc.execute()

    @staticmethod
    def multiply(a: float, b: float) -> float:
        calc = Calculation('multiply', [a, b])
        Calculator.history.append(calc)
        return calc.execute()

    @staticmethod
    def divide(a: float, b: float) -> float:
        calc = Calculation('divide', [a, b])
        Calculator.history.append(calc)
        return calc.execute()

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1]

    @classmethod
    def clear_history(cls):
        cls.history.clear()
