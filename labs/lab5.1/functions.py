def add(x, y):
    return x + y

def subtract(x, y):
    return x -y 

def multuply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error:: divide by 0"
    else:
        return x / y
    
def square(x,y):
    return x ** y
    
def func_manager(x, y, action):
    match action:
        case "add":
            print(f"Operation: add > result: {add(x,y)}")
            
        case "subtract":
            print(f"Operation: subtract > result: {subtract(x,y)}")  
            
        case "multiply":
            print(f"Operation: multiply > result: {multuply(x,y)}")  

        case "divide":
            print(f"Operation: divide > result: {divide(x,y)}")
        case "square":
            print(f"Operator: square Result > {square(x,y)}") 
        case _:
            print("unsupported operator")