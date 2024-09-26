import re
import sympy as sp

def preprocess_input(equation: str, variable: str = "x"):
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)

    expr = sp.sympify(equation)

    if variable not in equation:
        raise ValueError(f"Please provide an equation with respect to {variable}.")
    
    return expr

def postprocess_output(output):
    result = str(output)
    result = result.replace("**", "^")
    result = re.sub(r'\*(?=[a-zA-Z])', '', result)
    result = re.sub(r'(\d+)/(\d+)', r'(\1/\2)', result)
    
    return result
