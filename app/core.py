from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routes.auth import auth_router
from routes.river import river_router 


app = FastAPI(
    title="River API",
    version="1.0.0",
    description="With this API you can get information about Colombia rivers",
)

@app.get("/", tags=["Root"])
def root():
    return {"message": "Hello Worldasasdas"}


app.include_router(router=auth_router)
app.include_router(router=river_router)

# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="River API",
#         version="1.0.0",
#         description="With this API you can get information about Colombia rivers",
#         routes=app.routes,
#     )
#     openapi_schema[]

#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
#     }
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

# app.openapi = custom_openapi