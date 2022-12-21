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
    print(f"Input = {input}")
    print(f"Output = {output}")
    if output[n-1]["score"] >= input["score"]:
        # If our last (lowest) output score is greater than or equal to the input's score, don't insert and return
        pass
    else:
        # Start searching for insertion spot from the first (highest) value
        for i in range(0,n):
            if output[i]["score"] < input["score"]:
                print(f"Inputting {input['score']} over {output[i]['score']}")
                # Pop last (lowest) value, then insert our new value in-place so rest "slide down" and we keep max size `n`
                popped = output.pop()
                print(f"Popped {popped}")
                output.insert(i, input)
                break
            else:
                print("Not inserting...")
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
    exit(1)

# Setup `output` with `n` default values to get overwritten
# TODO what if n > m (lines in text)
output = []
for i in range(0,n):
    output.append({"score": -1, "id": -1})
    
# Read through file, line by line
count = 0
while True:
    line = file.readline()
    print("\n" + "-" * 150)
    print(f"Reading line \'{line}\'")
    if line == '':
        # Skip empty lines
        continue
    elif line != '\n':
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
            exit(2)
        # Try inserting `input` into `output`
        output = insertion(output, n, input)
    else:
        # Break parsing loop when done with file
        break
    
# Cleanup, print output, and exit successfully
# TODO format output
file.close()
exit(0)

