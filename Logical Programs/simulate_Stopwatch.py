import time


def stopwatch():
    """
    This function starts the timer when function executes and when user clicks 'Enter' the code saves the end time

    Arguments : None

    Output: The code returns the difference off  the start and end time
    """

    print("Stopwatch started... (Press Enter to stop)")
    start_time = time.time()

    input()

    end_time = time.time()

    return end_time - start_time


response = stopwatch()

print(f"Elapsed Time is {response}")
