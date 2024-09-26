from fastapi import APIRouter, HTTPException
from app.utils.equation_processing import preprocess_input, postprocess_output
import sympy as sp
import re

router = APIRouter()

@router.get("/differentiate/simple")
async def differentiate(equation: str):
    var = sp.symbols("x")
    expr = preprocess_input(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."}
    try:
        derivative = sp.diff(expr, var)
        derivative = postprocess_output(derivative)
        return {"derivative": str(derivative)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}