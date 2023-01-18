import random


def success(prisoner, boxes):
    """
    The prisoner keeps checking boxes until he finds his
    own number or checks 50 boxes.
    """
    count = 1
    next_box = prisoner
    while count < 50 and boxes[next_box] != prisoner:
        count += 1
        next_box = boxes[next_box]
    return boxes[next_box] == prisoner  # True if he found his own number


def good_run(boxes):
    for prisoner in range(1, 101):
        if not success(prisoner, boxes):
            return False
    return True  # True only if all 100 prisoners found their number


number_of_simulations = 10_000
successful_tries = 0
for i in range(number_of_simulations):
    boxes = {}
    prisoner_numbers = list(range(1, 101))  # prisoner list, every prisoner gets his unique ID
    for j in range(1, 101):
        random_num = random.choice(prisoner_numbers)
        boxes[j] = random_num  # {box number: prisoner ID}
        prisoner_numbers.remove(random_num)
    if good_run(boxes):
        successful_tries += 1

print(f"Probability to succeed: {successful_tries / number_of_simulations}")
