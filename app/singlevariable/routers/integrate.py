from fastapi import APIRouter, HTTPException
from app.utils.equation_processing import preprocess_input, postprocess_output
import sympy as sp
import re

router = APIRouter()

@router.get("/integrate/indefinite")
async def integrate(equation: str):
    try:
        expr = preprocess_input(equation)
        var = sp.symbols("x")
        
        integral = sp.integrate(expr, var)
        
        result = postprocess_output(integral)
        
        return {"integral": result}
    except ValueError as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/integrate/definite")
async def integrate(equation: str, lower: float, upper: float):
    try:
        expr = preprocess_input(equation)
        var = sp.symbols("x")
        
        integral = sp.integrate(expr, (var, lower, upper))
        
        result = postprocess_output(integral)
        
        return {"integral": result}
    except ValueError as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/integrate/trig-substitution")
async def integrate(equation: str, a_value: float):
    try:
        expr = preprocess_input(equation)
        x, theta, a = sp.symbols("x theta a")
        
        if expr.has(sp.sqrt(a**2 - x**2)):
            substitution = {x: a * sp.sin(theta)}
            dx_sub = sp.diff(a * sp.sin(theta), theta)
        elif expr.has(sp.sqrt(x**2 - a**2)):
            substitution = {x: a * sp.sec(theta)}
            dx_sub = sp.diff(a * sp.sec(theta), theta)
        elif expr.has(sp.sqrt(x**2 + a**2)):
            substitution = {x: a * sp.tan(theta)}
            dx_sub = sp.diff(a * sp.tan(theta), theta)
        else:
            raise HTTPException(status_code=400, detail="No trigonometric substitution found.")
        
        substituted_expr = expr.subs(substitution) * dx_sub
        simplified_expr = sp.simplify(substituted_expr)
        
        integral_result = sp.integrate(simplified_expr, theta)
        simplified_result = sp.simplify(integral_result)
        
        final_result = simplified_result.subs(a, a_value)
        result = postprocess_output(final_result)
        
        return {"integral": result}
    except ValueError as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}
