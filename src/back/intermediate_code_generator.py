"""Generates the intermediate code to then convert it in asm"""
class IntermediateCodeGenerator:
    """Generates an array of intermediate code"""
    def __init__(self, statements):
        self.statements = statements
        self.intermediate_code = []
        self._temporal_variables = []
        self.symbol_table = {}

    def _do_operation(self, op, left, right):
        if left in self.symbol_table:
            left = self.symbol_table[left] 

        if right in self.symbol_table:
            right = self.symbol_table[right]

        print(f"left {left} and right {right}")
        operations = {
            '+': (left + right),
            '-': (left - right),
            '*': (left * right),
            '/': (left / right)
        }
        return operations[op]

    def generate_operation(self, statement) -> int:
        """creates intermediate code for operations"""
        op, left, right = statement
        if len(right) == 2:
            self._temporal_variables.append(self._do_operation(op, left[1],right[1]))
            return len(self._temporal_variables) - 1
        temp_right_index = self.generate_operation(right)
        r = self._temporal_variables[temp_right_index]
        self._temporal_variables.append(self._do_operation(op, left[1], r))
        return len(self._temporal_variables) - 1

    def generate_assignment(self, statement):
        """creates intermediate code for assignment"""
        print(f"generate assigment {statement}")
        op = statement[0]
        left = statement[1]
        right = statement[2]

        if len(right) == 2 and right[0] == 'NUM':
            self.intermediate_code.append((op, left[1], right[1],))
            self.symbol_table[left[1]] = right[1]
            return

        if len(right) == 2 and right[0] == 'ID':
            self.intermediate_code.append((op, left[1], self.symbol_table[right[1]],))
            return

        if len(right) == 3:
            operation_result = self._temporal_variables[self.generate_operation(right)]
            self.intermediate_code.append((op, left[1], operation_result))
            self.symbol_table[left[1]] = operation_result

    def generate_intermediate_code(self):
        """Start the generation of the intermediate code"""
        for statement in self.statements:
            print(f"tabla simbolos {self.symbol_table}")
            if statement[0] == '=':
                self.generate_assignment(statement)
        print(self.intermediate_code)
