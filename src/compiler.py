"""Compiler module"""
from front.lexer import Lexer
from front.parser import Parser
from front.semantic_analyzer import SemanticAnalyzer

class Compiler:
    """Class that runs each compiler phase"""
    def __init__(self, source_code):
        self.source_code = source_code
        self.lexer = None
        self.parser = None
        self.semantic_analyzer = None

    def compile(self):
        """starts the compilation process"""
        self._run_lexyical_analysis()
        statements = self._run_syntax_analysis()
        self._run_semantic_analysis(statements)
        return self.semantic_analyzer.results

    def _run_lexyical_analysis(self) -> None:
        """Start with lexycal analysis"""
        self.lexer = Lexer(self.source_code)
        self.lexer.tokenize()

    def _run_syntax_analysis(self) -> list:
        """Start with syntax_analysis"""
        self.parser = Parser(self.lexer.tokens)
        return self.parser.parse()

    def _run_semantic_analysis(self, statements) -> None:
        """Start with syntax_analysis"""
        self.semantic_analyzer = SemanticAnalyzer(statements)
        self.semantic_analyzer.analyze()
 