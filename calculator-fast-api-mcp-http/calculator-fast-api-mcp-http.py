#Calculator API -> MCP [FastAPI_MCP - HTTP]
#
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1. make a fastAPI app (means API first)
app = FastAPI(title="calculator API")

@app.post("/multiply")
#functions
def multiply_numbers(a: float, b: float): 
    """
    multiplies two numbers and returns the resukt.
    """
    result = a * b
    return {"result": result}

@app.post("/add")
#functions
def add_numbers(a: float, b: float): 
    """
    addition of two numbers and returns the resukt.
    """
    result = a + b
    return {"result": result}

@app.post("/substract")
#functions
def substract_numbers(a: float, b: float): 
    """
    substract two numbers and returns the resukt.
    """
    result = a - b
    return {"result": result}

@app.post("/divide")
#functions
def divide_numbers(a: float, b: float): 
    """
    divide two numbers and returns the resukt.
    """
    result = a / b
    return {"result": result}

#2. Connverting it into MCP
mcp = FastApiMCP(app, name="calculator MPC FastApi")
#in order to run we need to mount it somewhere
mcp.moun_http()

if __name__ == "__main__":
#uvicorn - bridge between network requests (like HTTP or WebSockets) and modern asynchronous Python frameworks such as FastAPI,
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
