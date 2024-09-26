from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from app.utils.middleware_models import LoggingMiddleware, ExceptionHandlingMiddleware
from app.singlevariable.routers.limit import router as limit_router
from app.singlevariable.routers.differentiate import router as differentiate_router
from app.singlevariable.routers.integrate import router as integrate_router
from app.multivariable.routers.vector_calc import router as vector_calc_router
from app.multivariable.routers.partial_derivatives import router as partial_derivatives_router


app = FastAPI(title="Calculus API",
              description="""An API to solve calculus problems 
                             and provide AI-generated explanations""",
              version="1.0.0"
            )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(LoggingMiddleware)
app.add_middleware(ExceptionHandlingMiddleware)

app.include_router(limit_router)
app.include_router(differentiate_router)
app.include_router(integrate_router)
app.include_router(vector_calc_router)
app.include_router(partial_derivatives_router)