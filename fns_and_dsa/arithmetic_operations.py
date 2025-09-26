def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 == 0:
                return "Error: Cannot divide by zero."
            else:
                result = num1 / num2
        case _:
            return "Error: Invalid operation"
    return result
