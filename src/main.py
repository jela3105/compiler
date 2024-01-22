"""
In this file, the program starts.
"""
from compiler import Compiler

def main():
    """Main function, here the program starts"""

    with open("codiguito.txt", "r", encoding="utf-8") as f:
        source_code = f.read()
        f.close()

    compiler = Compiler(source_code)
    compiler.compile()

if __name__ == "__main__":
    main()
