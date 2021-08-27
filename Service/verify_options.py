def verify_options(option: int, quantity: int) -> bool:
    if option in range(1, quantity + 1):
        return True
    
    return False