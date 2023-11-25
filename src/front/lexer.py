"""Module to match regular expressions"""
import re

class Lexer:
    """Lexycal analyzer class"""
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = {'+', '-', '*', '/', '==', '!=',
                         '>', '<', '>=', '<=', 
                         'NUM', 'ID', '=', ';', 'IF', 'ELSE','EOF'}
        self.index = 0

    def tokenize(self) -> None:
        """Creates tokes looping throw the code"""
        while self.code:
            if self.code[0].isspace():
                self.code = self.code[1:]
            elif self.code.startswith('+'):
                self.tokens.append(('+', ''))
                self.code = self.code[1:]
            elif self.code.startswith('-'):
                self.tokens.append(('-', ''))
                self.code = self.code[1:]
            elif self.code.startswith('*'):
                self.tokens.append(('*', ''))
                self.code = self.code[1:]
            elif self.code.startswith('/'):
                self.tokens.append(('/', ''))
                self.code = self.code[1:]
            elif self.code.startswith('=='):
                self.tokens.append(('==', ''))
                self.code = self.code[2:]
            elif self.code.startswith('!='):
                self.tokens.append(('!=', ''))
                self.code = self.code[2:]
            elif self.code.startswith('>'):
                self.tokens.append(('>', ''))
                self.code = self.code[1:]
            elif self.code.startswith('<'):
                self.tokens.append(('<', ''))
                self.code = self.code[1:]
            elif self.code.startswith('>='):
                self.tokens.append(('>=', ''))
                self.code = self.code[2:]
            elif self.code.startswith('<='):
                self.tokens.append(('<=', ''))
                self.code = self.code[2:]
            elif self.code.startswith('IF'):
                self.tokens.append(('IF', ''))
                self.code = self.code[2:]
            elif self.code.startswith('ELSE'):
                self.tokens.append(('ELSE', ''))
                self.code = self.code[4:]
            elif self.code.startswith('='):
                self.tokens.append(('=', ''))
                self.code = self.code[1:]
            elif self.code.startswith(';'):
                self.tokens.append((';', ''))
                self.code = self.code[1:]
            elif self.code[0].isdigit():
                match = re.match(r'\d+', self.code)
                self.tokens.append(('NUM', int(match.group())))
                self.code = self.code[len(match.group()):]
            elif self.code[0].isalpha():
                match = re.match(r'[a-zA-Z_]\w*', self.code)
                self.tokens.append(('ID', match.group()))
                self.code = self.code[len(match.group()):]
            else:
                raise ValueError(f"Invalid token: {self.code}")

        self.tokens.append(('EOF', ''))

    def print_tokens(self) -> None:
        """Print generated tokens"""
        for token in self.tokens:
            print(f"{token},\n")
