
my_points = {
    "X": 1,  
    "Y": 2,  
    "Z": 3  
}

game_results = {
    ("A", "X"): 3,  
    ("A", "Y"): 6,  
    ("A", "Z"): 0,  
    ("B", "X"): 0,  
    ("B", "Y"): 3,  
    ("B", "Z"): 6, 
    ("C", "X"): 6,  
    ("C", "Y"): 0,  
    ("C", "Z"): 3   
}

total = 0  

with open("input_6.txt") as file:
    for line in file:
        opponent, me = line.split()
        total += my_points[me] + game_results[(opponent, me)]

print("Score:", total)  

#Result: 8933