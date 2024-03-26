PERCENTAGE = 0.13

agent_name = input("What is your name: ")
agent_sales = int(input(f"{agent_name}, What is your total sales amount: "))

print(f"{agent_name}, your commission for this month is {round(agent_sales * PERCENTAGE, 2)}")