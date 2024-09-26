from fastapi import APIRouter, HTTPException
from app.utils.vector_processing import preprocess_vector_input, postprocess_output
import sympy as sp
import re

router = APIRouter()

@router.get("/vector/dot-product")
async def dot_product(v1: str, v2: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        dot_product = v1.dot(v2)
        result = postprocess_output(dot_product)
        return {"dot_product": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/cross-product")
async def cross_product(v1: str, v2: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        cross_product = v1.cross(v2)
        result = postprocess_output(cross_product)
        return {"cross_product": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/magnitude")
async def magnitude(v: str):
    try:
        v = preprocess_vector_input(v)
        magnitude = v.norm()
        result = postprocess_output(magnitude)
        return {"magnitude": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/normalize")
async def normalize(v: str):
    try:
        v = preprocess_vector_input(v)
        normalized_vector = v.normalized()
        result = postprocess_output(normalized_vector)
        return {"normalized_vector": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/projection")
async def projection(v1: str, v2: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        projection = v1.project(v2)
        result = postprocess_output(projection)
        return {"projection": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/equation-of-plane")
async def equation_of_plane(v1: str, v2: str, point: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        point = preprocess_vector_input(point)
        normal_vector = v1.cross(v2)
        plane = sp.Plane(point, normal_vector=normal_vector)
        result = postprocess_output(plane.equation())
        return {"plane": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/equation-of-line")
async def equation_of_line(point: str, direction: str):
    try:
        point = preprocess_vector_input(point)
        direction = preprocess_vector_input(direction)
        line = sp.Line3D(point, direction_ratio=direction)
        result = postprocess_output(line.equation())
        return {"line": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/derivative")
async def derivative(v: str, variable: str):
    try:
        v = preprocess_vector_input(v)
        var = sp.symbols(variable)
        derivative = v.diff(var)
        result = postprocess_output(derivative)
        return {"derivative": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/integral")
async def integral(v: str, variable: str):
    try:
        v = preprocess_vector_input(v)
        var = sp.symbols(variable)
        integral = v.integrate(var)
        result = postprocess_output(integral)
        return {"integral": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/limit")
async def limit(v: str, variable: str, value: float):
    try:
        v = preprocess_vector_input(v)
        var = sp.symbols(variable)
        limit = v.limit(var, value)
        result = postprocess_output(limit)
        return {"limit": result}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/gradient")
async def gradient(v: str, variables: str):
    try:
        v = preprocess_vector_input(v)
        variables = sp.symbols(variables)
        gradient = v.jacobian(variables)
        result = postprocess_output(gradient)
        return {"gradient": result}
    except Exception as e:
        return {"Error": str(e)}
