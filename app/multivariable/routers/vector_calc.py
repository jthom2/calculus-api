from fastapi import APIRouter, HTTPException
import sympy as sp
import re

router = APIRouter()

@router.get("/vector/dot-product")
async def dot_product(v1: str, v2: str):
    # Preprocessing input
    v1 = v1.replace("^", "**")
    v2 = v2.replace("^", "**")
    # Add '*' between numbers and variables
    v1 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v1)
    v2 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v2)
    v1 = sp.Matrix(v1)
    v2 = sp.Matrix(v2)
    try:
        dot_product = v1.dot(v2)
        # Reverse '**' back to '^' in the result
        result = str(dot_product).replace("**", "^")
        return {"dot_product": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/cross-product")
async def cross_product(v1: str, v2: str):
    # Preprocessing input
    v1 = v1.replace("^", "**")
    v2 = v2.replace("^", "**")
    # Add '*' between numbers and variables
    v1 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v1)
    v2 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v2)
    v1 = sp.Matrix(v1)
    v2 = sp.Matrix(v2)
    try:
        cross_product = v1.cross(v2)
        # Reverse '**' back to '^' in the result
        result = str(cross_product).replace("**", "^")
        return {"cross_product": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}
        
@router.get("/vector/magnitude")
async def magnitude(v: str):
    # Preprocessing input
    v = v.replace("^", "**")
    # Add '*' between numbers and variables
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    v = sp.Matrix(v)
    try:
        magnitude = v.norm()
        # Reverse '**' back to '^' in the result
        result = str(magnitude).replace("**", "^")
        return {"magnitude": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/normalize")
async def normalize(v: str):
    # Preprocessing input
    v = v.replace("^", "**")
    # Add '*' between numbers and variables
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    v = sp.Matrix(v)
    try:
        normalized_vector = v.normalized()
        # Reverse '**' back to '^' in the result
        result = str(normalized_vector).replace("**", "^")
        return {"normalized_vector": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/projection")
async def projection(v1: str, v2: str):
    # Preprocessing input
    v1 = v1.replace("^", "**")
    v2 = v2.replace("^", "**")
    # Add '*' between numbers and variables
    v1 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v1)
    v2 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v2)
    v1 = sp.Matrix(v1)
    v2 = sp.Matrix(v2)
    try:
        projection = v1.project(v2)
        # Reverse '**' back to '^' in the result
        result = str(projection).replace("**", "^")
        return {"projection": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/equation-of-plane")
async def equation_of_plane(v1: str, v2: str, point: str):
    # Preprocessing input
    v1 = v1.replace("^", "**")
    v2 = v2.replace("^", "**")
    point = point.replace("^", "**")
    # Add '*' between numbers and variables
    v1 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v1)
    v2 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v2)
    point = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', point)
    v1 = sp.Matrix(v1)
    v2 = sp.Matrix(v2)
    point = sp.Matrix(point)
    try:
        # Calculate normal vector as cross product of v1 and v2
        normal_vector = v1.cross(v2)
        plane = sp.Plane(point, normal_vector=normal_vector)
        # Reverse '**' back to '^' in the result
        result = str(plane.equation()).replace("**", "^")
        return {"plane": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/equation-of-line")
async def equation_of_line(point: str, direction: str):
    # Preprocessing input
    point = point.replace("^", "**")
    direction = direction.replace("^", "**")
    # Add '*' between numbers and variables
    point = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', point)
    direction = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', direction)
    point = sp.Point3D(point)
    direction = sp.Matrix(direction)
    try:
        line = sp.Line3D(point, direction_ratio=direction)
        # Reverse '**' back to '^' in the result
        result = str(line.equation()).replace("**", "^")
        return {"line": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/derivative")
async def derivative(v: str, variable: str):
    # Preprocessing input
    v = v.replace("^", "**")
    # Add '*' between numbers and variables
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    v = sp.Matrix(v)
    var = sp.symbols(variable)
    try:
        derivative = v.diff(var)
        # Reverse '**' back to '^' in the result
        result = str(derivative).replace("**", "^")
        return {"derivative": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/integral")
async def integral(v: str, variable: str):
    # Preprocessing input
    v = v.replace("^", "**")
    # Add '*' between numbers and variables
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    v = sp.Matrix(v)
    var = sp.symbols(variable)
    try:
        integral = v.integrate(var)
        # Reverse '**' back to '^' in the result
        result = str(integral).replace("**", "^")
        return {"integral": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/limit")
async def limit(v: str, variable: str, value: float):
    # Preprocessing input
    v = v.replace("^", "**")
    # Add '*' between numbers and variables
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    v = sp.Matrix(v)
    var = sp.symbols(variable)
    try:
        limit = v.limit(var, value)
        # Reverse '**' back to '^' in the result
        result = str(limit).replace("**", "^")
        return {"limit": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/gradient")
async def gradient(v: str, variables: str):
    # Preprocessing input
    v = v.replace("^", "**")
    # Add '*' between numbers and variables
    v = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', v)
    v = sp.Matrix(v)
    variables = sp.symbols(variables)
    try:
        gradient = v.jacobian(variables)
        # Reverse '**' back to '^' in the result
        result = str(gradient).replace("**", "^")
        return {"gradient": result}
    except HTTPException as e:
        return {"Error": str(e)}
    except Exception as e:
        return {"Error": str(e)}
