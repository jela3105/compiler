"""Seconde module of compiler: syntax analysis"""

class Parser:
    """Class to run the syntax analysis, creating the AST"""
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def create_primary_node(self):
        """Creates a node of the AST (a tuple), for ID or NUM"""
        token = self.tokens[self.index]

        if token[0] == 'NUM' or token[0] == 'ID':
            self.index += 1
            return token

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
        """creates subtree for a assigment, left part is an ID, right is a expresion"""
        left = self.create_primary_node()

        if self.tokens[self.index][0] == '=':
            self.index += 1
            right = self.parse_operations()
            return ('=', left, right)
        raise ValueError(f"Esperado '=' pero encontrado {self.tokens[self.index]}")

    def parse_comparison(self):
        """Parses a comparison '==', '!=','>', '<', '>=', '<=',"""
        left = self.parse_operations()
        op = self.tokens[self.index][0]
        if(op not in {'==', '!=','>', '<', '>=', '<='}):
            raise ValueError(f"Token {op} no permitido en comparacion")

        self.index += 1
        right = self.parse_operations()
        return (op, left, right)

    def parse_condition(self):
        """Validates condition syntaxis"""
        self.index += 1
        left = self.parse_comparison()
        while self.tokens[self.index][0] != ')':
            op = self.tokens[self.index][0]
            self.index += 1
            right = self.parse_comparison()
            left = (op, left, right)
        self.index += 1
        return left

    def get_if_condition(self):
        """return tokens for a if condition"""
        if self.tokens[self.index][0] != '(':
            token = self.tokens[self.index][0]
            raise ValueError(f"(parse statement) Token inesperado condicional if: {token}")
        return self.parse_condition()

    def get_if_body(self):
        """return the body of if statement stops when finds { and move index next position"""
        token = self.tokens[self.index][0]
        if token != '{':
            raise ValueError(f"(parse statement) esperado apertura llave, obtenido: {token[0]}")
        if_body_statements = []
        self.index += 1
        while self.tokens[self.index][0] != '}':
            statement = self.parse_statement()
            if statement is not None:
                if_body_statements.append(statement)
        self.index += 1
        return if_body_statements

    def parse_if_statement(self):
        """Analyze and creates nodes for if statement"""
        self.index += 1
        if_branches = []
        initial_condition = self.get_if_condition()
        initial_body = self.get_if_body()
        if_branches.append((initial_condition, initial_body))
        while(self.tokens[self.index][0] == 'else' or
              self.tokens[self.index][0] == 'elif'):
            if self.tokens[self.index][0] == 'else':
                self.index += 1
                body = self.get_if_body()
                if_branches.append(('', body))
                break
            condition = self.get_if_condition()
            body = self.get_if_body()
            if_branches.append((condition, body))

        return ('if', if_branches)

    def parse_if_condition(self):
        """Creates the nodes for if statement"""
        self.index += 1
        if_condition = self.parse_comparison()
        if_body_statements = self.parse_statement()
        else_body_statements = None
        if self.tokens[self.index][0] == 'else':
            self.index += 1
            else_body_statements = self.parse_statement()
        return ('if', if_condition, if_body_statements, else_body_statements)

    def parse_statement(self):
        """Validates the token, it can be IF statement or ID"""
        token = self.tokens[self.index]

        if token[0] == 'if':
            return self.parse_if_statement()

        if token[0] == 'ID':
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
