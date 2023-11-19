from sympy import symbols, diff, simplify, integrate
import logging
import tkinter as tk

logging.basicConfig(format = '%(levelname)s: %(message)s',
                    level=logging.DEBUG)



def main():
    x = symbols('x')
    while True:
        try:
            equation = input("Equation required: ")

            key = input("Enter 'dev' to derive or 'inte' to integrate: ")   

            if key == "dev":
                dev_times = int(input("Derivative No: "))
                var = input("Differentiate with respect to: ")
                simplified_equation = simplify(equation)
                var = symbols(var)
                result = diff(equation, x, dev_times)

                if result == "Invalid":
                    logging.warning("Re-check your equation!")
                    continue
                
                else:
                    logging.info(f"{equation}")
                    
                    if equation == {simplified_equation}:
                        logging.info(f"{simplified_equation}")
                        logging.info(f"Differentiated equation: {result}")
                    
                    else:
                        logging.info(f"{simplified_equation}")
                        logging.info(f"Differentiated equation: {result}")

                
            elif key == "inte":
                var = input("Integrate with respect to: ")
                simplified_equation = simplify(equation)
                var = symbols(var)
                result = integrate(equation, var)

                if result == SyntaxError:
                    logging.warning('SyntaxError')

                else:
                    logging.info(f"{equation}")

                    if equation == {simplified_equation}:
                        logging.info(f"{simplified_equation}")
                        logging.info(f"Differentiated equation: {result}")
                    
                    else:
                        logging.info(f"{simplified_equation}")
                        logging.info(f"Differentiated equation: {result}")
            
            else:
                logging.info(f"Defferentiated equation: {result}")
        
        except ValueError:
            logging.warning("Invalid input!!")

            continue

if __name__ == "__main__":
    main()