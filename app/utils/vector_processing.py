import re
import sympy as sp

def preprocess_vector_input(v: str):
    v = v.replace("^", "**")
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    return sp.Matrix([sp.sympify(i.strip()) for i in v.split(',')])

def postprocess_output(output):
    result = str(output)
    result = result.replace("**", "^")
    result = re.sub(r'\*(?=[a-zA-Z])', '', result)
    result = re.sub(r'(\d+)/(\d+)', r'(\1/\2)', result)
    
    return result
