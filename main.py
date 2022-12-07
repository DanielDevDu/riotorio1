from app.core import app

if __name__ == "__main__":
    import uvicorn
    import os

    env = os.environ.get
    HOST = env("HOST", default="0.0.0.0")
    PORT = env("PORT", default=8000)
    RELOAD = env("RELOAD", default=True)

    uvicorn.run("__main__:app", host=HOST, port=PORT, reload=RELOAD)