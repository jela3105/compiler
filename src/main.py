"""
The main file that runs the program
"""
from compiler import Compiler

def main():
    """Main function, here the program starts"""

    source_code = """
    x = 10
    y = 11
    if (x > 0){
        x = 0
        z = 1 
    }elif(x < 2){
        y = 0
    }else{
        id = x + y
    }
    """

    compiler = Compiler(source_code)
    compiler.compile()

if __name__ == "__main__":
    main()
