
def put_parenthesis(exp):

    if len(exp) < 2:
        return

    if exp[0] == 'T' or exp[0] == 'F':
        s = '('+exp[0:3] + ')' + exp[3:]
        print(s)
        
        put_parenthesis(s)
    else:
        s = '(' + exp[0:3] + ')' + exp[3:]
        put_parenthesis(s)




def get_expression(symbol, operator, answer, choose_symbol):

    if len(symbol) == 0:
        print(answer)
        return

    if choose_symbol:

        if len(symbol) > 0:
            t = symbol.copy()
            s = t[0]
            t.remove(s)
            a = answer.copy()
            a.append(s)
            get_expression(t, operator, a, False)

        if len(symbol) > 1:
            t = symbol.copy()
            s = t[1]
            t.remove(s)
            a = answer.copy()
            a.append(s)
            get_expression(t, operator, a, False)

    else:

        if len(operator) > 0:
            t = operator.copy()
            s = t[0]
            t.remove(s)
            a = answer.copy()
            a.append(s)
            get_expression(symbol, t, a, True)

        if len(operator) > 1:
            t = operator.copy()
            s = t[1]
            t.remove(s)
            a = answer.copy()
            a.append(s)
            get_expression(symbol, t, a, True)

        if len(operator) > 2:
            t = operator.copy()
            s = t[2]
            t.remove(s)
            a = answer.copy()
            a.append(s)
            get_expression(symbol, t, a, True)



symbol = ['T', 'F', 'T']
operators = ['&', '^']
answer = []

get_expression(symbol, operators, answer, True)
