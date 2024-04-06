def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return 'Error: Too many problems.'

    op1 = []
    operator = []
    op2 = []

    for problem in problems:
        ops = problem.split()
        op1.append(ops[0])
        operator.append(ops[1])
        op2.append(ops[2])

    for num in op1+op2:
        if len(num) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not num.isdigit():
            return 'Error: Numbers must only contain digits.'

    for op in operator:
        if op not in ["+","-"]:
            return "Error: Operator must be '+' or '-'."

    opline1 = []
    opline2 = []
    dashline = []
    solution = []

    for i in range(len(op1)):
        if len(op1[i]) > len(op2[i]):
            opline1.append(" "*2 +op1[i])
        else:
            opline1.append(" "*(len(op2[i])-len(op1[i])+2)+op1[i])    

    for i in range(len(op2)):
        if len(op2[i]) > len(op1[i]):
            opline2.append(operator[i] + " " + op2[i])
        else:
            opline2.append(operator[i] + " "*(len(op1[i])-len(op2[i])+1) + op2[i])

    for i in range(len(op1)):
        dashline.append("-"*(max(len(op1[i]),len(op2[i]))+2))

    if show_answers:
        for i in range(len(op1)):
            if operator[i] == "+":
                ans = str(int(op1[i])+int(op2[i]))
            else:
                ans = str(int(op1[i])-int(op2[i]))
            
            if len(ans) > max(len(op1[i]),len(op2[i])):
                solution.append(" "+ans)
            else:
                solution.append(" "*(max(len(op1[i]),len(op2[i]))-len(ans)+2) + ans)
        arranged_prob = "    ".join(opline1) + '\n'+ "    ".join(opline2) + '\n' + "    ".join(dashline) + '\n' + "    ".join(solution)                 
    else:
        arranged_prob = "    ".join(opline1) + '\n'+ "    ".join(opline2) + '\n' + "    ".join(dashline)                 
    
    return arranged_prob

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"],True)}')

