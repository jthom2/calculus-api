from fastapi import APIRouter, HTTPException
import sympy as sp
import re

router = APIRouter()

@router.get("/integrate/indefinite")
async def integrate(equation: str):
    var = sp.symbols("x")
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    expr = sp.sympify(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."}
    try:
        integral = sp.integrate(expr, var)
        integral = str(integral).replace("**", "^")
        integral = re.sub(r'\*(?=[a-zA-Z])', '', integral)
        integral = re.sub(r'(\d+)/(\d+)', r'(\1/\2)', integral)
        return {"integral": str(integral)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/integrate/definite")
async def integrate(equation: str, lower: float, upper: float):
    var = sp.symbols("x")
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    expr = sp.sympify(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."} 
    try:
        integral = sp.integrate(expr, (var, lower, upper))
        integral = str(integral).replace("**", "^")
        integral = re.sub(r'\*(?=[a-zA-Z])', '', integral)
        integral = re.sub(r'(\d+)/(\d+)', r'(\1/\2)', integral)
        return {"integral": str(integral)}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/integrate/trig-substitution")
async def integrate(equation: str, a_value: float):
    x, theta, a = sp.symbols("x theta a")
    equation = equation.replace("^", "**")
    equation = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', equation)
    expr = sp.sympify(equation)
    if "x" not in equation:
        return {"Error": "Please provide an equation with respect to x."}

    # Use .has() instead of 'in' to check for subexpressions
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
    final_result = str(final_result).replace("**", "^")
    final_result = re.sub(r'\*(?=[a-zA-Z])', '', final_result)
    final_result = re.sub(r'(\d+)/(\d+)', r'(\1/\2)', final_result)

    return {"integral": str(final_result)}
