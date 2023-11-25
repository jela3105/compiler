"""Does the semantic anlysis"""

class SemanticAnalyzer:
    """Semantic analyzer class"""
    def __init__(self, statements):
        self.statements = statements
        self.symbol_table = {}
        self.results = []

    def evaluate_expr(self, expr):
        """HOLA"""
        if isinstance(expr, tuple):
            op, left, right = expr
            left_value = self.evaluate_expr(left)
            right_value = self.evaluate_expr(right)

            if op == '+':
                return left_value + right_value
            elif op == '-':
                return left_value - right_value
            elif op == '*':
                return left_value * right_value
            elif op == '/':
                return left_value // right_value
            elif op == '==':
                return left_value == right_value
            elif op == '!=':
                return left_value != right_value
            elif op == '>':
                return left_value > right_value
            elif op == '<':
                return left_value < right_value
            elif op == '>=':
                return left_value >= right_value
            elif op == '<=':
                return left_value <= right_value
            elif op == '=':
                if isinstance(left, tuple) and left[0] == 'ID':
                    self.symbol_table[left[1]] = right_value
                else:
                    raise ValueError(f"Invalid assignment: {left}")
            else:
                raise ValueError(f"Invalid operation: {op}")
        elif expr[0] == 'ID':
            if expr[1] in self.symbol_table:
                return self.symbol_table[expr[1]]
            else:
                raise ValueError(f"Variable '{expr[1]}' not defined")
        elif expr[0] == 'NUM':
            return expr[1]

    def analyze(self):
        """HOLA"""
        for statement in self.statements:
            if isinstance(statement, tuple) and statement[0] == 'IF':
                condition = self.evaluate_expr(statement[1])
                if condition:
                    result = self.analyze_statement(statement[2])
                else:
                    result = self.analyze_statement(statement[3]) if statement[3] else None
                self.results.append(result)
            elif isinstance(statement, tuple) and statement[0] == '=':
                self.evaluate_expr(statement)
                self.results.append(None)
            elif statement is None:
                self.results.append(None)
            else:
                raise ValueError(f"Invalid statement: {statement}")

    def analyze_statement(self, statement):
        """HOLA"""
        if isinstance(statement, tuple) and statement[0] == 'IF':
            condition = self.evaluate_expr(statement[1])
            if condition:
                return self.analyze_statement(statement[2])
            else:
                return self.analyze_statement(statement[3]) if statement[3] else None
        elif isinstance(statement, tuple) and statement[0] == '=':
            self.evaluate_expr(statement)
            return None
        elif statement is None:
            return None
        else:
            raise ValueError(f"Invalid statement: {statement}")
