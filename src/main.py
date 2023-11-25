"""
The main file that runs the program
"""
from compiler import Compiler

def main():
    """Main function, here the program starts"""

    source_code = """
    x = 10
    y = 11
    IF x > 0
        IF x == 1
            x = 0
        ELSE 
            z = 1 
    ELSE 
        y = 0
    """

    compiler = Compiler(source_code)
    compiler.compile()

if __name__ == "__main__":
    main()
