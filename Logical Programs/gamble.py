import random

def gamble_stats(initial_stake, target_goal, max_plays):
    """Simulate a gambling scenario and calculate win/loss statistics
    
    Arguments:
        initial_stake (int): Starting amount of money
        target_goal (int): Amount to reach to win
        max_plays (int): Maximum number of games to play
    
    Returns:
        tuple: (wins, win_percentage, loss_percentage)
    """
    stake = initial_stake
    wins = 0
    losses = 0
    plays = 0

    while stake > 0 and stake < target_goal and plays < max_plays:
        result = random.random()
        plays += 1
        
        if result <= 0.5:
            losses += 1
            stake -= 1
        else:
            wins += 1
            stake += 1

    if plays > 0:
        total_plays = plays 
    
    win_percent = (wins / total_plays) * 100
    loss_percent = (losses / total_plays) * 100

    return (wins,stake, win_percent, loss_percent)

stake = int(input("Enter your Stake amount: "))
goal = int(input("Enter your Goal amount: "))
play_limit = int(input("Enter your Play Limit amount: "))

if stake <= 0 or goal <= 0 or play_limit <= 0:
    print("Please enter positive values for stake, goal, and play limit")
elif stake >= goal:
    print("Stake must be less than goal")
else:
    wins,stake, win_percent, loss_percent = gamble_stats(stake, goal, play_limit)
    print(f"Number of wins: {wins}")
    print(f"Stake after the game: {stake}")
    print(f"Win Percentage: {win_percent:.2f}%")
    print(f"Loss Percentage: {loss_percent:.2f}%")