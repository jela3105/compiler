"""Transforms the intermediate code to asm 8086 code, crating a file"""

class TargetCodeGenerator:
    """Class that contains methods to generate asm 8086 file"""
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.string_target_code = None

    def generate_8086_code(self):
        """crate 8086 code for each line in intermediate code"""
        for line in self.intermediate_code:
            print(line)
