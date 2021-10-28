# Exam Preparation
# 20210414-03. Problem 3
# 19:43 - 19:56 = 13 min

def flights(*args):
    flights_info = {}
    for destination, passengers in zip(args[::2], args[1::2]):
        if destination == 'Finish':
            break

        if destination not in flights_info:
            flights_info[destination] = 0

        flights_info[destination] +=int(passengers)

    return flights_info


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
