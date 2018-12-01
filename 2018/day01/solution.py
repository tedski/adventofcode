import os

curdir = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(curdir, 'input.txt')
freq = 0
end_freq = None
repeat_freq = None
known_freqs = set()
iteration = 0

while not repeat_freq:
    with open(input_file, 'r') as f:
        for line in f:
            num = line.rstrip('\n')
            freq += int(num)

            if not repeat_freq and freq in known_freqs:
                repeat_freq = freq
            else:
                known_freqs.add(freq)
            
        if not end_freq:
            end_freq = freq
            print(f'End frequency: {end_freq:>10}')

        if repeat_freq:
            print(f'First repeat freq: {repeat_freq:>10}')
