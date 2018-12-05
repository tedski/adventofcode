from collections import Counter
import os
import re
from typing import List, Tuple


curdir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curdir, 'input.txt')
with open(input_file, 'r') as fp:
    puzzle_input = fp.read().splitlines()


def predictable_guard(guard_logs: List[str]) -> Tuple[int, int]:
    guard_logs.sort()

    sleep_account = {}
    guard_on_duty = None
    start_minute = None
    stop_minute = None

    for log_entry in guard_logs:
        activity_pattern = re.compile(r'.*\d{2}:(\d{2})] (\w+)')
        match = activity_pattern.match(log_entry)

        if match.group(2) == 'Guard':
            guard_id_pattern = re.compile(r'.*(#\d+)')
            guard_id_match = guard_id_pattern.match(log_entry)
            guard_on_duty = guard_id_match.group(1)
            if guard_on_duty not in sleep_account:
                sleep_account[guard_on_duty] = Counter()
        elif match.group(2) == 'falls':
            start_minute = int(match.group(1))
        elif match.group(2) == 'wakes':
            stop_minute = int(match.group(1))
            for minute in range(start_minute, stop_minute):
                sleep_account[guard_on_duty].update({minute: 1})
    
    sleepiest_guard_id = max(sleep_account, key=lambda key: sum(sleep_account[key].values()))
    frequent_minute = sleep_account[sleepiest_guard_id].most_common(1)[0][0]
    
    return int(sleepiest_guard_id.lstrip('#')), frequent_minute


def test_prediction():
    guard_logs = [
     '[1518-11-01 00:00] Guard #10 begins shift',
     '[1518-11-01 00:25] wakes up',
     '[1518-11-01 00:30] falls asleep',
     '[1518-11-01 00:55] wakes up',
     '[1518-11-01 23:58] Guard #99 begins shift',
     '[1518-11-02 00:40] falls asleep',
     '[1518-11-03 00:05] Guard #10 begins shift',
     '[1518-11-01 00:05] falls asleep',
     '[1518-11-03 00:24] falls asleep',
     '[1518-11-03 00:29] wakes up',
     '[1518-11-04 00:02] Guard #99 begins shift',
     '[1518-11-02 00:50] wakes up',
     '[1518-11-04 00:36] falls asleep',
     '[1518-11-04 00:46] wakes up',
     '[1518-11-05 00:03] Guard #99 begins shift',
     '[1518-11-05 00:45] falls asleep',
     '[1518-11-05 00:55] wakes up',
    ]
    assert predictable_guard(guard_logs) == (10, 24)

if __name__ == "__main__":
    guard_id, minute = predictable_guard(puzzle_input)
    print(f'Guard {guard_id} sleeps for {minute}, giving an answer of: {guard_id * minute}')