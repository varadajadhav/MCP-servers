# libraries
#This imports the FastMCP class from the fastmcp library.
from fastmcp import FastMCP 

# Create the MCP server instance
mcp = FastMCP(name="calculator")

# Define the tools (each is like a small API endpoint)
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b
@mcp.tool(name="add", description="Add two numbers", tags=["math", "arithmetic"])
def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

@mcp.tool(name="subtract", description="Subtract two numbers", tags=["math", "arithmetic"])
def subtract(c: float, d: float) -> float:
    """Subtract two numbers (c - d)."""
    return c - d

@mcp.tool()
def divide(e: float, f: float) -> float:
    """Divide two numbers (e / f)."""
    if f == 0:
        raise ValueError("cannot divide by zero")
    return e / f

if __name__ == "__main__":
#The construct if __name__ == "__main__": in Python is a common idiom used to control the execution of code within a script. It allows you to define code that should only run when the script is executed directly, and not when it's imported as a module into another script.
#Here's a breakdown:
#__name__: This is a special built-in variable in Python. When a Python script is executed, the interpreter assigns a value to __name__.
#If the script is the main program being run directly (e.g., python your_script.py), then __name__ is set to the string "__main__".
#If the script is being imported as a module into another script (e.g., import your_script), then __name__ is set to the name of the module (which is typically the filename without the .py extension).
#"__main__": This is a string literal representing the name assigned to the top-level execution environment when a script is run directly.
    # Start the MCP server so clients (like the Inspector or Claude) can connect
    mcp.run()
