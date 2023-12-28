"""Module to match regular expressions"""
import re

class Lexer:
    """Lexycal analyzer class"""
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.keywords = ('+', '-', '*', '/', '==', '!=',
                         '>', '<', '>=', '<=','{','}', 
                         '=', ';', 'IF', 'ELSE')
        self.index = 0

    def tokenize(self) -> None:
        """Creates tokens of the given code"""
        while self.code:
            if self.code[0].isspace():
                self.code = self.code[1:]
                continue

            if self.code[0].isdigit():
                match = re.match(r'\d+', self.code)
                self.tokens.append(('NUM', int(match.group())))
                self.code = self.code[len(match.group()):]
                continue

            if self.code[0].isalpha():
                match = re.match(r'[a-zA-Z_]\w*', self.code)
                self.tokens.append(('ID', match.group()))
                self.code = self.code[len(match.group()):]
                continue

            for keyword in self.keywords:
                if self.code.startswith(keyword):
                    self.tokens.append((keyword, ''))
                    self.code = self.code[len(keyword):]
                    break

        self.tokens.append(('EOF', ''))

    def print_tokens(self) -> None:
        """Print generated tokens"""
        for token in self.tokens:
            print(f"{token}")
