def precedence(operator):
    if operator in {'→', '↔'}:
        return 1
    elif operator == '∨':
        return 2
    elif operator == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    precedence = {'^': 3, '∨': 2, '→': 1, '↔': 1}
    output = []
    operators = []

    for token in expression:
        if token in precedence:
            while operators and precedence.get(operators[-1], 0) >= precedence[token]:
                output.append(operators.pop(0))
            operators.insert(0, token)
        elif token == '(':
            operators.insert(0, token)
        elif token == ')':
            while operators and operators[0] != '(':
                output.append(operators.pop(0))
            operators.pop(0)  # Удаляем '(' из стека
        else:
            output.append(token)

    output.extend(reversed(operators))
    return output



def evaluate_postfix(expression):
    stack = []
    for token in expression:
        for char in token:
            if char in {'^', '∨', '→', '↔'}:
                try:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                except IndexError:
                    continue
                if char == '^':
                    stack.append(operand1 and operand2)
                elif char == '∨':
                    stack.append(operand1 or operand2)
                elif char == '→':
                    stack.append(not operand1 or operand2)
                elif char == '↔':
                    stack.append(operand1 == operand2)
            elif char == ' ':
                continue
            else:
                stack.append(char == 'T')
    if len(stack) != 1:
        raise SyntaxError("Invalid expression")
    return stack[0]


def parse_expression(expression):
    # Удаление пробелов и разбиение на токены
    tokens = expression.replace(' ', '').replace('→', '->').replace('↔', '<->')
    tokens = tokens.replace('(', ' ( ').replace(')', ' ) ').split()

    # Преобразование в обратную польскую запись
    try:
        postfix = infix_to_postfix(tokens)
        print(postfix)
    except SyntaxError as e:
        print("Syntax Error:", e)
        return

    # Вычисление значения выражения
    try:
        result = evaluate_postfix(postfix)
        print("Значение выражения:", "T" if result else "F")
    except SyntaxError as e:
        print("Syntax Error:", e)


expression = input("Введите логическое выражение: ")
parse_expression(expression)
