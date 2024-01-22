"""Compiler module"""
import copy
from front.lexer import Lexer
from front.parser import Parser
from front.semantic_analyzer import SemanticAnalyzer
from back.intermediate_code_generator import IntermediateCodeGenerator
from back.target_code_generator import TargetCodeGenerator

class Compiler:
    """Class that runs each compiler phase"""
    def __init__(self):
        self.source_code = None
        self.lexer = None
        self.parser = None
        self.semantic_analyzer = None
        self.intermediate_code_generator = None
        self.target_code_generator = None

    def compile(self):
        """starts the compilation process------"""
        print("------Tokens generados------")
        self._run_lexyical_analysis()
        print("------Arbol sintactico (AST)------")
        statements = self._run_syntax_analysis()
        print("------Analisis semantico------")
        #we send a copy so it doesn't modify the original statements
        self._run_semantic_analysis(copy.copy(statements))
        print("------Codigo intermedio------")
        intermediate_code = self._create_intermediate_code(statements)
        print("------Codigo objeto------")
        self._create_target_code(intermediate_code)

    def read_code(self, path = "") -> None:
        """reads code from file"""
        with open(path + "codiguito.txt", "r", encoding="utf-8") as f:
            self.source_code = f.read()
            f.close()

    def _run_lexyical_analysis(self) -> None:
        """Start with lexycal analysis"""
        self.lexer = Lexer(self.source_code)
        self.lexer.tokenize()
        self.lexer.print_tokens()

    def _run_syntax_analysis(self) -> list:
        """Start with syntax_analysis"""
        self.parser = Parser(self.lexer.tokens)
        return self.parser.parse()

    def _run_semantic_analysis(self, statements) -> None:
        """Start with syntax_analysis"""
        self.semantic_analyzer = SemanticAnalyzer(statements)
        self.semantic_analyzer.analyze()

    def _create_intermediate_code(self, statements) -> None:
        self.intermediate_code_generator = IntermediateCodeGenerator(statements)
        return self.intermediate_code_generator.generate_intermediate_code()

    def _create_target_code(self, intermediate_code):
        self.target_code_generator = TargetCodeGenerator(intermediate_code)
        self.target_code_generator.generate_8086_code()
 