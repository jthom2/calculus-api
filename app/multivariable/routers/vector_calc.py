from fastapi import APIRouter, HTTPException
from app.utils.vector_input_processing import preprocess_vector_input
import sympy as sp
import re

router = APIRouter()

@router.get("/vector/dot-product")
async def dot_product(v1: str, v2: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        dot_product = v1.dot(v2)
        return {"dot_product": str(dot_product)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/cross-product")
async def cross_product(v1: str, v2: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        cross_product = v1.cross(v2)
        return {"cross_product": str(cross_product)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/magnitude")
async def magnitude(v: str):
    try:
        v = preprocess_vector_input(v)
        magnitude = v.norm()
        return {"magnitude": str(magnitude)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/normalize")
async def normalize(v: str):
    try:
        v = preprocess_vector_input(v)
        normalized_vector = v.normalized()
        return {"normalized_vector": str(normalized_vector)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/projection")
async def projection(v1: str, v2: str):
    try:
        v1 = preprocess_vector_input(v1)
        v2 = preprocess_vector_input(v2)
        projection = v1.project(v2)
        return {"projection": str(projection)}
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
        return {"plane": str(plane.equation())}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/equation-of-line")
async def equation_of_line(point: str, direction: str):
    try:
        point = preprocess_vector_input(point)
        direction = preprocess_vector_input(direction)
        line = sp.Line3D(point, direction_ratio=direction)
        return {"line": str(line.equation())}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/derivative")
async def derivative(v: str, variable: str):
    try:
        v = preprocess_vector_input(v)
        var = sp.symbols(variable)
        derivative = v.diff(var)
        return {"derivative": str(derivative)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/integral")
async def integral(v: str, variable: str):
    try:
        v = preprocess_vector_input(v)
        var = sp.symbols(variable)
        integral = v.integrate(var)
        return {"integral": str(integral)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/limit")
async def limit(v: str, variable: str, value: float):
    try:
        v = preprocess_vector_input(v)
        var = sp.symbols(variable)
        limit = v.limit(var, value)
        return {"limit": str(limit)}
    except Exception as e:
        return {"Error": str(e)}

@router.get("/vector/gradient")
async def gradient(v: str, variables: str):
    try:
        v = preprocess_vector_input(v)
        variables = sp.symbols(variables)
        gradient = v.jacobian(variables)
        return {"gradient": str(gradient)}
    except Exception as e:
        return {"Error": str(e)}
