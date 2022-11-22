### module example ###

def sum(*numbers) -> int:
    result = 0
    for number in numbers:
        result += number    
        
    return result

def minus(*numbers) -> int:
    result = 0
    for number in numbers:
        result -= number    
        
    return result

def multiply(a, b) -> float:
    return a / b

def division(a, b) -> float:
    return a / b
    