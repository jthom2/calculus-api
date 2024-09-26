from fastapi import APIRouter, HTTPException
from app.utils.equation_processing import preprocess_input
import sympy as sp
import re

router = APIRouter()

@router.get("/limit/simple")
async def limit(equation: str, value: float):
    var = sp.symbols("x")
    expr = preprocess_input(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."}
    try:
        limit = sp.limit(expr, var, value)
        return {"limit": str(limit)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

