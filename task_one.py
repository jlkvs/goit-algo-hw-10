from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Maximize_Production", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat='Continuous')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Continuous')

model += lemonade + fruit_juice, "Total_Products"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

model += 1 * lemonade <= 50, "Sugar_Constraint"

model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

model.solve()

print(f"Кількість виробленого лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість вироблених продуктів: {lemonade.varValue + fruit_juice.varValue}")
