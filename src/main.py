"""
In this file, the program starts.
"""
from compiler import Compiler

def main():
    """Main function, here the program starts"""

    compiler = Compiler()
    compiler.read_code()
    compiler.compile()

if __name__ == "__main__":
    main()
