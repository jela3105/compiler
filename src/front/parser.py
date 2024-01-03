"""Seconde module of compiler: syntax analysis"""

class Parser:
    """Class to run the syntax analysis, creating the AST"""
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def create_primary_node(self):
        """Creates a node of the AST (a tuple)"""
        token = self.tokens[self.index]

        if token[0] == 'NUM':
            self.index += 1
            return ('NUM', token[1])

        if token[0] == 'ID':
            self.index += 1
            return ('ID', token[1])

        if token[0] == '(':
            self.index += 1
            expr = self.parse_operations()
            if self.tokens[self.index][0] == ')':
                self.index += 1
                return expr
            raise ValueError(f"Esperado ')' pero no se encontro{self.tokens[self.index]}")

        raise ValueError(f"(Parse primary) Token inesperado: {token} {self.index}")

    def parse_term(self):
        """Define order of operations"""
        left = self.create_primary_node()

        while self.tokens[self.index][0] in {'*', '/'}:
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.create_primary_node()
            left = (op, left, right)

        return left

    def parse_operations(self):
        """Parses operations following the order of operations"""
        left = self.parse_term()

        while self.tokens[self.index][0] in {'+', '-'}:
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.parse_term()
            left = (op, left, right)

        return left

    def parse_assignment(self):
        """creates subtree for a assignmet, left part is an ID, right is a expresion"""
        left = self.create_primary_node()

        if self.tokens[self.index][0] == '=':
            self.index += 1
            right = self.parse_operations()
            return ('=', left, right)
        raise ValueError(f"Esperado '=' pero encontrado {self.tokens[self.index]}")

    def parse_comparison(self):
        """Validates comparison syntaxis"""
        if not self.tokens[self.index] == '(':
            raise ValueError("(parse statement) expected '(' for if statement")

        self.index += 1
        left = self.parse_operations()

        if self.tokens[self.index][0] in {'==', '!=', '>', '<', '>=', '<='}:
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.parse_operations()
            return (op, left, right)
        else:
            return left

    def get_if_condition(self):
        """return tokens for a if condition"""
        if self.tokens[self.index][0] != '(':
            token = self.tokens[self.index][0]
            raise ValueError(f"(parse statement) Token inesperado condicional if: {token}")
        condition_tokens = []
        while self.tokens[self.index][0] != '{':
            condition_tokens.append(self.tokens[self.index])
            self.index += 1
        return condition_tokens

    def valid_condition(self, condition):
        """Check if a condition is valid in parentheses"""
        open_parentheses = 0
        for token in condition:
            if token[0] == '(' :
                open_parentheses += 1
            elif token[0] == ')':
                if open_parentheses == 0:
                    raise ValueError("(parse statement) Parentesis inecesario")
                open_parentheses -= 1
        return not open_parentheses

    def get_if_body(self):
        """return the body of if statement"""
        token = self.tokens[self.index][0]
        if token != '{':
            raise ValueError(f"(parse statement) Token inesperado cuerpo if: {token}")
        if_body_statements = []
        self.index += 1
        while self.tokens[self.index][0] != '}':
            statement = self.parse_statement()
            if statement is not None:
                if_body_statements.append(statement)
        return if_body_statements

    def parse_if_statement(self):
        """Analyze and creates nodes for if statement"""
        self.index += 1
        initial_condition = self.get_if_condition()
        if not self.valid_condition(initial_condition):
            raise ValueError(f"(parse statement) Condicion no valida: {initial_condition}")
        print(f"condicion inicial valida en parentesis: {initial_condition}")
        initial_body = self.get_if_body()
        return ('IF', initial_condition, initial_body)

    def parse_if_condition(self):
        """Creates the nodes for if statement"""
        self.index += 1
        if_condition = self.parse_comparison()
        if_body_statements = self.parse_statement()
        #print(self.tokens[self.index])
        else_body_statements = None
        if self.tokens[self.index][0] == 'ELSE':
            self.index += 1
            else_body_statements = self.parse_statement()
        return ('IF', if_condition, if_body_statements, else_body_statements)

    def parse_statement(self):
        """Validates the token, it can be IF statement or ID"""
        token = self.tokens[self.index]

        if token[0] == 'IF':
            return self.parse_if_statement()

        if token[0] == 'ID':
            #self.index += 1
            return self.parse_assignment()

        raise ValueError(f"(parse statement) Token inesperado: {token}")

    def parse(self) -> list:
        """Iterate each token to create the AST"""
        statements = []
        while self.tokens[self.index][0] != 'EOF': #stops when find the end of the file
            statement = self.parse_statement()
            print(f"s {statement}")
            if statement is not None:
                statements.append(statement)
        return statements
