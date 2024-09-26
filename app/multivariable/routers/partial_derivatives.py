from fastapi import APIRouter, HTTPException
import sympy as sp
import re

router = APIRouter()

@router.get("/partial-derivative/simple")
async def partial_derivative(equation: str, variable: str):
    var = sp.symbols(variable)
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    expr = sp.sympify(equation)
    try:
        derivative = sp.diff(expr, var)
        derivative = str(derivative).replace("**", "^")
        derivative = re.sub(r'\*(?=[a-zA-Z])', '', derivative)
        return {"derivative with respect to {var}": str(derivative)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}