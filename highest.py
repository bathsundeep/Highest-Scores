import sys
import json
import re

def insertion(output, n, input):
    """ Given `output` of length `n` and candidate `input`, consider
        inserting `input` in the correct place in `output` such that
        `output` is in descending order, not exceeding length `n`
    Args:
        output (List): A List of Dictionary inputs
        n (Int): Max length of `output`
        input (Dict): Potential dict to be inserted in `output`
    """
    if output[n-1]["score"] >= input["score"]:
        # If our last (lowest) output score is greater than or equal to the input's score, don't insert and return
        pass
    else:
        # Start searching for insertion spot from the first (highest) value
        for i in range(0,n):
            if output[i]["score"] < input["score"]:
                # Pop last (lowest) value, then insert our new value in-place so rest "slide down" and we keep max size `n`
                output.pop()
                output.insert(i, input)
                break
            else:
                # Maybe next time...
                continue
    return output

# Parse CLI args, catch any exceptions
try:
    file_name = sys.argv[1]
    n = int(sys.argv[2])
    if len(sys.argv) != 3:
        raise Exception
except Exception as e:
    print("Error: Invalid input")
    print("e.g. `python highest.py file.txt 10`")
    exit(1)

file = open(file_name, 'r')
if not file:
    print(f"ERROR: Failed to read {file_name}")
    file.close()
    exit(1)

# Setup `output` with `n` default values to get overwritten
output = []
for i in range(0,n):
    output.append({"score": -1, "id": -1})
    
# Read through file, line by line
while True:
    line = file.readline()
    if line == '\n':
        # Skip empty lines
        continue
    elif line == '':
        # EOF
        break
    # parse non-empty String `line` into Dict `input` according to spec
    try:
        m = re.search("^[\d]+", line)
        score = m.group(0)
        m = re.search("\{.*\}", line)
        d = json.loads(m.group(0))
        id = d["id"]
        input = {"score": int(score), "id": id}
    except Exception as e:
        print(f"ERROR: Improper line format: {e}")
        file.close()
        exit(2)
    # Try inserting parsed `input` into `output`
    output = insertion(output, n, input)

    
# Cleanup, print output, and exit Success
file.close()
for line in output:
    print(line)
exit(0)

