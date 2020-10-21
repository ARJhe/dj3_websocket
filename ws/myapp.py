import uvicorn

if __name__ == "__main__":
    uvicorn.run("ws.asgi:application", reload=True)