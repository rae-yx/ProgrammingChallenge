def find_type(value):
    if value.isdigit():
        return "Integer"
    
    try:
        float_value = float(value)
        if '.' in value:
            return "Real Number"
        
    except ValueError:
        pass

    if any(char.isdigit() for char in value) and any(char.isdigit() for char in value):
        return "Alphanumeric"
    
    return "Alphabetical String"