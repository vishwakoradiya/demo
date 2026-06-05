import pulp
# product = pulp.LpProblem("Simple_LP_Problem", pulp.LpMaximize)
# x = pulp.LpVariable('a', lowBound=0)
# y = pulp.LpVariable('b', lowBound=0)

# product += 40 * x + 30 * y

# product += 2 * x + 1 * y <= 100

# product.solve()

# print(f"Status: {pulp.LpStatus[product.status]}")
# print(f"x = {pulp.value(x)}")
# print(f"y = {pulp.value(y)}")
# print(f"Objective = {pulp.value(product.objective)}")



    # protien
# product = pulp.LpProblem("Simple_LP_Problem", pulp.LpMinimize)
# x = pulp.LpVariable('a', lowBound=0)
# y = pulp.LpVariable('b', lowBound=0)

# product += 20 * x + 10 * y

# product += 10 * x + 5 * y >=50
# product += 200 * x + 100 * y >= 800
# product.solve()

# print(f"Status: {pulp.LpStatus[product.status]}")
# print(f"x = {pulp.value(x)}")
# print(f"y = {pulp.value(y)}")
# print(f"Objective = {pulp.value(product.objective)}")


    # calories
# product = pulp.LpProblem("Simple_LP_Problem", pulp.LpMinimize)
# x = pulp.LpVariable('a', lowBound=0)
# y = pulp.LpVariable('b', lowBound=0)

# product += 20 * x + 10 * y

# product += 200 * x + 100 * y >= 800
# product.solve()

# print(f"Status: {pulp.LpStatus[product.status]}")
# print(f"x = {pulp.value(x)}")
# print(f"y = {pulp.value(y)}")
# print(f"Objective = {pulp.value(product.objective)}")


    #budget
# product = pulp.LpProblem("Simple_LP_Problem", pulp.LpMaximize)
# x = pulp.LpVariable('a', lowBound=0)
# y = pulp.LpVariable('b', lowBound=0)
# z = pulp.LpVariable('c', lowBound=0)
# product += 100 * x + 150 * y + 120 * z

# product += 40 * x + 60 * y + 50 * z <= 100

# product.solve()

# print(f"Status: {pulp.LpStatus[product.status]}")
# print(f"x = {pulp.value(x)}")
# print(f"y = {pulp.value(y)}")
# print(f"z = {pulp.value(z)}")
# print(f"Objective = {pulp.value(product.objective)}")


    #stuf
# product = pulp.LpProblem("Simple_LP_Problem", pulp.LpMinimize)
# x = pulp.LpVariable('a', lowBound=0)
# y = pulp.LpVariable('b', lowBound=0)
# z = pulp.LpVariable('c', lowBound=0)
# product += 500 * x + 600 * y + 800 * z

# product += x >= 10
# product += y >= 8
# product += z >=6

# product +=  x +  y +  z <=15

# product.solve()

# print(f"Status: {pulp.LpStatus[product.status]}")
# print(f"x = {pulp.value(x)}")
# print(f"y = {pulp.value(y)}")
# print(f"z = {pulp.value(z)}")
# print(f"Objective = {pulp.value(product.objective)}")