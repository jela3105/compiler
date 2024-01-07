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

        operations = {
            '+': (left + right),
            '-': (left - right),
            '*': (left * right),
            '/': (left / right)
        }
        return operations[op]

    def _do_comparison(self, op, left, right):
        operations = {
            '==': (left == right),
            '!=': (left != right),
            '>': (left > right),
            '<': (left < right),
            '>=': (left >= right),
            '<=': (left <= right),
        }
        return operations[op]

    def generate_operation(self, statement) -> int:
        """return intex of temporal variable for operations"""
        if len(statement) == 2:
            if statement[0] == 'ID':
                self._temporal_variables.append(self.symbol_table[statement[1]])
                return len(self._temporal_variables) - 1
            self._temporal_variables.append(statement[1])
            return len(self._temporal_variables) -1

        op, left, right = statement
        if len(right) == 2:
            self._temporal_variables.append(self._do_operation(op, left[1],right[1]))
            return len(self._temporal_variables) - 1
        temp_right_index = self.generate_operation(right)
        op_result = self._temporal_variables[temp_right_index]
        self._temporal_variables.append(self._do_operation(op, left[1], op_result))
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
            self.symbol_table[left[1]] = self.symbol_table[right[1]]
            return

        if len(right) == 3:
            operation_result = self._temporal_variables[self.generate_operation(right)]
            self.intermediate_code.append((op, left[1], operation_result))
            self.symbol_table[left[1]] = operation_result

    def satisfy_condition(self, condition) -> bool:
        """returns if a tree of conditions is true"""
        if condition == '':
            return True

        op, left, right = condition

        if op in {'==','!=','>','<','>=','<='}:
            l_comparison = self._temporal_variables[self.generate_operation(left)]
            r_comparison=self._temporal_variables[self.generate_operation(right)]
            return self._do_comparison(op, l_comparison, r_comparison)

        left_satisfied = self.satisfy_condition(left)
        right_satisfied = self.satisfy_condition(right)

        operations = {
            'and': (left_satisfied and right_satisfied),
            'or': (left_satisfied or right_satisfied)
        }
        return operations[op]

    def generate_branch_code(self, branch_statements):
        """append intermediate code of the given brach statements"""
        for statement in branch_statements:
            if statement[0] == '=':
                self.generate_assignment(statement)
            if statement[0] == 'if':
                self.generate_if(statement[1])

    def generate_if(self, if_branches):
        """checks branches conditions and writes the branch that is true"""
        for branch in if_branches:
            if self.satisfy_condition(branch[0]):
                self.generate_branch_code(branch[1])
                return

    def generate_intermediate_code(self):
        """Start the generation of the intermediate code"""
        for statement in self.statements:
            print(f"tabla simbolos {self.symbol_table}")
            if statement[0] == '=':
                self.generate_assignment(statement)
            if statement[0] == 'if':
                self.generate_if(statement[1])
        print(self.intermediate_code)
        return self.intermediate_code
