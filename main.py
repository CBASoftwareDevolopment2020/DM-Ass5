from automaton import AbcdAutomaton
from log_entry import LogEntry
from itertools import product
from pprint import pprint as pp
from time import sleep, time

if __name__ == '__main__':
    auto = AbcdAutomaton()

    entries = []
    with open('logs.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            level, system, instance, action, timestamp = line.split('-')
            entries.append(LogEntry(level, system, instance, action))
            sleep(1)

    valid = []
    invalid = []
    for entry in entries:
        print('-' * 20)
        print(entry)
        state = auto.next_state(entry)
        if state:
            print('Legal action')
            valid.append(entry)
            if state.is_final:
                print('In a accepting state')
            else:
                print('In a non-accepting state')
        else:
            print('Invalid action')
            invalid.append(entry)
        # sleep(1)

    print('valid', valid)
    print('invalid', invalid)

