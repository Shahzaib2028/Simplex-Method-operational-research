import numpy as np
from scipy.optimize import linprog

print("-----------SIMPLEX METHOD-------------")
print("Select simplex method of \n1) Maximization\n2) Minimization")
select = int(input("Enter 1 or 2 for selection "))


def Maximization():
    print("-----------You selected MAXIMIZATION SIMPLEX METHOD-------------")
    print("")

    # Create objective function
    C = []
    z_n = int(input("Enter size of objective function "))

    for i in range(z_n):
        z_input = eval(input("Enter coefficeints of objective function ")) * -1
        C.append(z_input)
    C = np.array(C)

    print(" Coefficient of your objective function are ", C)
    print("")

    # Create contrains and take only coefficeints of contrains
    a_n = int(input("Enter number of contrains "))
    A = []
    for i in range(a_n):
        temp = []
        print("")
        print("Constraint number ", i)
        for j in range(z_n):
            a_input = eval(input("Enter coefficeint of constranis "))
            temp.append(a_input)
        A.append(temp)

    A = np.array(A)

    b = np.identity(z_n, dtype=int)
    b = b * -1
    Z = np.concatenate((A, b))
    print("Coefficients of your constraints are ", Z)

    # Take contants(b) of the the contrains
    B = []
    print("")
    for i in range(a_n):
        b_input = int(input("Enter contants value "))
        B.append(b_input)

    for i in range(z_n):
        B.append(0)

    B = np.array(B)
    print("Constants of your constraints are ", B)

    # Solving for simplex method
    res = linprog(C, A_ub=Z, b_ub=B)

    # Print results
    print("")
    print('Optimal value:', round(res.fun * -1, ndigits=2),
          '\nx values:', res.x,
          '\nSlack values', res.slack[:a_n],
          '\nNumber of iterations performed:', res.nit)


def Minimization():
    print("-----------You selected MINIMIZATION SIMPLEX METHOD-------------")
    print("")

    # Create objective function
    C = []
    z_n = int(input("Enter size of objective function "))

    for i in range(z_n):
        z_input = eval(input("Enter coefficeints of objective function "))
        C.append(z_input)
    C = np.array(C)

    print(" Coefficient of your objective function are ", C)
    print("")

    # Create contrains and take only coefficeints of contrains
    a_n = int(input("Enter number of contrains "))
    A = []
    for i in range(a_n):
        temp = []
        print("")
        print("Constraint number ", i)
        for j in range(z_n):
            a_input = eval(input("Enter coefficeint of constranis ")) * -1
            temp.append(a_input)
        A.append(temp)

    A = np.array(A)

    b = np.identity(z_n, dtype=int)
    b = b * -1
    Z = np.concatenate((A, b))
    print("Coefficients of your constraints are ", Z)

    # Take contants(b) of the the contrains
    B = []
    print("")
    for i in range(a_n):
        b_input = int(input("Enter contants value ")) * -1
        B.append(b_input)

    for i in range(z_n):
        B.append(0)

    B = np.array(B)
    print("Constants of your constraints are ", B)

    # Solving for simplex method
    res = linprog(C, A_ub=Z, b_ub=B, method='simplex', )

    # Print results
    print("")
    print('Optimal value:', round(res.fun, ndigits=2),
          '\nx values:', res.x,
          '\nSlack values', res.slack[:a_n],
          '\nNumber of iterations performed:', res.nit)


if select == 1:
    Maximization()
elif select == 2:
    Minimization()
else:
    print("Please Enter correct number for selection")
