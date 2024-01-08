"""Does the semantic anlysis"""

class SemanticAnalyzer:
    """Semantic analyzer class"""
    def __init__(self, statements):
        self.statements = statements
        self.symbol_table = {}
        self.results = []

    def is_in_symbol_table(self, variable):
        """Checks if a variable is already in symbol table"""
        return variable in self.symbol_table

    def evaluate_conditional(self, condition):
        """Analyze a conditional"""

        if len(condition) < 2: #case of else
            return

        if len(condition) == 3:
            self.evaluate_conditional(condition[1])
            self.evaluate_conditional(condition[2])

        if len(condition) == 2:
            token_type, value = condition
            if token_type == 'ID':
                if not self.is_in_symbol_table(value):
                    raise ValueError(f"(semantic error) {value} no se ha declarado")

    def evaluate_if_expr(self, if_branches):
        """Analyze a if expression"""
        for branch in if_branches:
            self.evaluate_conditional(branch[0])
            print("condicion valida")
            for statement in branch[1]:
                self.statements.append(statement)

    def evaluate_operation(self, operations):
        """Evaluate semantic of basic operations"""
        if len(operations) == 2:
            return

        left = operations[1]
        right = operations[2]
        if len(left) == 2 and left[0] == 'ID':
            if not self.is_in_symbol_table(left[1]):
                raise ValueError(f"Error semantico: No se ha declarado {left[1]}")
        if len(right) == 2 and right[0] == 'ID':
            if not self.is_in_symbol_table(right[1]):
                raise ValueError(f"Error semantico: No se ha declarado {right[1]}")
        if len(left) > 2:
            self.evaluate_operation(left)
        if len(right) > 2:
            self.evaluate_operation(right)

    def evaluate_assignment(self, statement):
        """Analyze an assigment"""
        left = statement[1]
        right = statement[2]
        self.evaluate_operation(right)
        self.symbol_table[left[1]] = right
        return True

    def analyze(self):
        """Start with the analysis"""
        for statement in self.statements:
            if statement[0] == 'if':
                self.evaluate_if_expr(statement[1])
                print("if valido")
            elif statement[0] == '=':
                self.evaluate_assignment(statement)
                print("asignacion valida")
            elif statement[0] == 'print':
                pass
            else:
                raise ValueError(f"Invalido: {statement}")
        return self.symbol_table
