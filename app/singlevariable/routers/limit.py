from fastapi import APIRouter, HTTPException
import sympy as sp
import re

router = APIRouter()

@router.get("/limit/simple")
async def limit(equation: str, value: float):
    var = sp.symbols("x")
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    expr = sp.sympify(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."}
    try:
        limit = sp.limit(expr, var, value)
        return {"limit": str(limit)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

