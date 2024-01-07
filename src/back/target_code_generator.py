"""Transforms the intermediate code to asm 8086 code, crating a file"""

class TargetCodeGenerator:
    """Class that contains methods to generate asm 8086 file"""
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.symbol_table = {}
        self.string_target_code = None
        self._body_target_code = ""
        self._data_target_code = ""

    def append_assigment(self, line) -> str:
        """Assing new value to the give variable"""
        return (
        str(f"""
mov Ax, @data 
mov Ds, Ax
mov {line[1]}, {line[2]}d
            """))

    def generate_8086_code(self):
        """crate 8086 code for each line in intermediate code"""
        for line in self.intermediate_code:
            if line[0] not in self.symbol_table:

                self._data_target_code += str(f"""
{line[1]} db ?""")

                self.symbol_table[line[1]] = line[2]
            self._body_target_code = self._body_target_code + self.append_assigment(line)
        print(self._data_target_code)
        print(self._body_target_code)
