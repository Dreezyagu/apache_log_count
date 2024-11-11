import sys
byte_size = 0
current_count = 0
count_map = {}
gb_in_bytes = 1024*1024*1024

for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip()
    # parse the input we got from mapper.py
    size, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
        size = int(size)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    current_count+=1
    size_in_gb = size/gb_in_bytes
    byte_size += size_in_gb

print(f"Total requests: {current_count}")
print(f"Total request cost (no * 0,001): {current_count*0.001}\n\n")

print(f"Total byte size: {byte_size}")
print(f"Total cost per GB(size * 0,08): {byte_size*0.08}\n\n")

print(f"Total cost: {(byte_size*0.08) + (current_count*0.001)}")