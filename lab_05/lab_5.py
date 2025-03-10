limits = {"red": 12, "green": 13, "blue": 14}
total = 0

with open("input_5_1.txt") as file:
    for line in file:
        game_id, rounds = line.split(": ")
        game_id = int(game_id.split()[1])
        possible = True
        
        for round in rounds.split("; "):
            for cube in round.split(", "):
                num, color = cube.split()
                if int(num) > limits[color]:
                    possible = False
                    break
            if not possible:
                break
        
        if possible:
            total += game_id

print("Result:", total)  

#Result : 2810