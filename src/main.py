"""
The main file that runs the program
"""
from compiler import Compiler

def main():
    """Main function, here the program starts"""

    source_code = """
    x = 10;
    y = 10;
    IF x > 0
        y = 10;
    ELSE 
        y = 0;
    """

    compiler = Compiler(source_code)
    results = compiler.compile()

    print("Semantic analysis results:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
