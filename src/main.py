"""
The main file that runs the program
"""
from compiler import Compiler

def main():
    """Main function, here the program starts"""

    source_code = """
    var1 = 10
    var2 = var1 - 5 
    if (var2 > 10){
        x = 0
    }elif(var2 < 2){
        y = 0
    }else{
        z = 1 
    }
    
    """

    compiler = Compiler(source_code)
    compiler.compile()

if __name__ == "__main__":
    main()
