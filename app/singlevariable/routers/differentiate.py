from fastapi import APIRouter, HTTPException
import sympy as sp
import re

router = APIRouter()

@router.get("/differentiate/simple")
async def differentiate(equation: str):
    var = sp.symbols("x")
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    expr = sp.sympify(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."}
    try:
        derivative = sp.diff(expr, var)
        derivative = str(derivative).replace("**", "^")
        derivative = re.sub(r'\*(?=[a-zA-Z])', '', derivative)
        return {"derivative": str(derivative)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}