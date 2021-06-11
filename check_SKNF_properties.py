def variables_in_formula(formula):
    variables = []
    formula = formula.upper()
    for i in range(65, 91):
        symbol = chr(i)
        if formula.count(symbol) > 0:
            variables.append(symbol)
    return variables


def first_rules(formula):
    variables = variables_in_formula(formula)
    list_of_disjunction = formula[1:-1].split("/\\")
    list_of_variables = []
    for i in range(len(list_of_disjunction)):
        tmp = []
        for j in range(len(list_of_disjunction[i])):
            if variables.count(list_of_disjunction[i][j]) > 0 and list_of_disjunction[i][j - 1] == '!':
                tmp.append(list_of_disjunction[i][j - 1:j + 1])
            elif variables.count(list_of_disjunction[i][j]) > 0:
                tmp.append(list_of_disjunction[i][j])
        tmp.sort()
        list_of_variables.append(tmp)
    for i in list_of_variables:
        if list_of_variables.count(i) > 1:
            return False
    return True


def second_rules(formula):
    list_of_disjunction = formula[1:-1].split("/\\")
    for i in range(len(list_of_disjunction)):
        list_of_disjunction[i] = list_of_disjunction[i].replace(')', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('(', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('!', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('/', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('\\', '')
        list_of_disjunction[i] = sorted(list_of_disjunction[i])
    for i in list_of_disjunction:
        if len(i) != len(set(i)):
            return False
    return True


def third_rules(formula):
    variables = variables_in_formula(formula)
    list_of_disjunction = formula[1:-1].split("/\\")

    for i in range(len(list_of_disjunction)):
        list_of_disjunction[i] = list_of_disjunction[i].replace(')', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('(', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('!', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('/', '')
        list_of_disjunction[i] = list_of_disjunction[i].replace('\\', '')
        list_of_disjunction[i] = sorted(list_of_disjunction[i])
    for i in list_of_disjunction:
        if i != variables:
            return False
    return True


def check_KNF(formula):
    list_of_disjunction = formula[1:-1].split("/\\")
    variables = variables_in_formula(formula)
    for i in list_of_disjunction:
        if i.count('\/') != len(variables) - 1:
            return False
    return True


def remove_brackets(formula):
    for i in range(len(formula) - formula.count('!') * 2):
        if formula[i] == '!':
            formula = formula[:i - 1] + formula[i:]
            tmp = i
            while formula[tmp] != ')':
                tmp += 1
            formula = formula[:tmp] + formula[tmp + 1:]
    return formula


def check_brackets(formula):
    formula = remove_brackets(formula)
    while formula.count('(') > 0:
        left_parenthesis = 0
        right_parenthesis = 0
        for j in range(len(formula)):
            if formula[j] == '(':
                left_parenthesis = j
        for j in range(left_parenthesis, len(formula)):
            if formula[j] == ')':
                right_parenthesis = j
                break
        if right_parenthesis == len(formula) - 1 and left_parenthesis == 0:
            subnormal = formula
        elif right_parenthesis == len(formula) - 1:
            subnormal = formula[left_parenthesis:]
        elif left_parenthesis == 0:
            subnormal = formula[:right_parenthesis]
        else:
            subnormal = formula[left_parenthesis:right_parenthesis + 1]

        if len(variables_in_formula(subnormal)) != 2:
            if len(variables_in_formula(subnormal)) != 1 and subnormal.count('z') != 'z':
                return False
        formula = formula.replace(subnormal, 'z')
    if formula == 'z':
        return True


def check_grammar(formula):
    variables = variables_in_formula(formula)
    for i in range(len(formula)):
        if (formula[i] == '!' and formula[i - 1] != '(') or (formula[i] == '!' and formula[i + 1] == '('):
            return False
    for i in variables:
        if ord(i) > 90:
            return False
    for i in range(len(formula)):
        for j in variables:
            if formula[i] == f'{j}':
                if formula[i - 1] == '(' and formula[i + 1] == ')':
                    return False
                else:
                    return True
    return True


def check_SKNF(formula):
    formula = formula.replace(" ", '')
    variables = variables_in_formula(formula)
    if len(variables) == 0:
        return False
    elif len(variables) == 1:
        return True if formula == f'({variables[0]}/\(!{variables[0]}))' or \
                       formula == f'((!{variables[0]})/\{variables[0]})' or \
                       formula == f'{variables[0]}' or formula == f'(!{variables[0]})' else False
    else:
        return check_grammar(formula) and check_KNF(formula) and third_rules(formula) and second_rules(formula) \
               and first_rules(formula) and check_brackets(formula)
