def verify_options(option: str, quantity: int) -> bool:
    try:
        option = int(option)
        if option in range(1, quantity + 1):
            return True
    except:
        return False