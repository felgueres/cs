# Given a string, evaluate the expression
def calculate(s:str)-> int:
    stack, cur_number, cur_sign, result = [],0,1,0
    for char in s:
        if char.isdigit():
            cur_number=cur_number*10+int(char)
        elif char in '+-':
            result += cur_number * cur_sign
            cur_sign = 1 if char == '+' else -1
            cur_number = 0
        elif char == '(':
            stack.append(result)
            stack.append(cur_sign)
            result,cur_sign=0,1
        elif char == ')':
            result += cur_sign * cur_number
            result *= stack.pop()
            result += stack.pop()
            cur_number = 0
        
    if cur_number != 0:
        result+= cur_sign * cur_number

    return result

print(calculate('-(100-10)+5'))