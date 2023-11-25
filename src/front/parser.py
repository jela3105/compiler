"""No modules imported"""

class Parser:
    """Class to run the syntax analysis, creating the AST"""
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse_primary(self):
        """HOLA"""
        token = self.tokens[self.index]

        if token[0] == 'NUM':
            self.index += 1
            return ('NUM', token[1])
        elif token[0] == 'ID':
            self.index += 1
            return ('ID', token[1])
        elif token[0] == '(':
            self.index += 1
            expr = self.parse_expr()
            if self.tokens[self.index][0] == ')':
                self.index += 1
                return expr
            else:
                raise ValueError(f"Expected ')' but found {self.tokens[self.index]}")
        else:
            raise ValueError(f"Unexpected token: {token}")

    def parse_term(self):
        """HOLA"""
        left = self.parse_primary()

        while self.tokens[self.index][0] in {'*', '/'}:
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.parse_primary()
            left = (op, left, right)

        return left

    def parse_expr(self):
        """HOLA"""
        left = self.parse_term()

        while self.tokens[self.index][0] in {'+', '-'}:
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.parse_term()
            left = (op, left, right)

        return left

    def parse_assignment(self):
        """HOLA"""
        left = self.parse_primary()

        if self.tokens[self.index][0] == '=':
            self.index += 1
            right = self.parse_expr()
            return ('=', left, right)
        else:
            raise ValueError(f"Expected '=' but found {self.tokens[self.index]}")

    def parse_statement(self):
        """Validates the token between a IF statement, ID or a semicolon(;)"""
        token = self.tokens[self.index]

        if token[0] == 'IF':
            self.index += 1
            condition = self.parse_expr()
            if_token = self.parse_statement()
            else_token = self.parse_statement() if self.tokens[self.index][0] == 'ELSE' else None
            return ('IF', condition, if_token, else_token)

        if token[0] == 'ID':
            self.index += 1
            return self.parse_assignment()

        if token[0] == ';':
            self.index += 1
            return None

        raise ValueError(f"Unexpected token: {token}")

    def parse(self) -> list:
        """Iterate each token to create the AST"""
        statements = []
        while self.tokens[self.index][0] != 'EOF': #stops when find the end of the file
            statement = self.parse_statement()
            if statement is not None:
                statements.append(statement)
        return statements
