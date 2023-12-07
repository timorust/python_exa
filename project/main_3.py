def calculate_house_cost(bricks1, bricks2, bricks3):
    total_bricks = bricks1 + bricks2 + bricks3
    average_bricks = total_bricks / 3
    brick_cost = 5.9  
    house_cost = total_bricks * brick_cost
    return total_bricks, average_bricks, house_cost

bricks1 = int(input("Enter amount of bricks for second pig1.."))
bricks2 = int(input("Enter amount of bricks for second pig2..."))
bricks3 = int(input("Enter amount of bricks for second pig3..."))

result = calculate_house_cost(bricks1, bricks2, bricks3)
print("General amount of bricks:", result[0])
print("Average amount of bricks:", result[1])
print("The cost of the house in dollars:=> $", result[2])
