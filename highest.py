import sys
import json
import collections
import re

def insertion(output, n, input):
    """ Given `output` of length `n` and input candidate `input`, 
        insert `input` in the correct place in `output` such that
        `output` is in descending order, not exceeding length `n`
    Args:
        output (List(Dict)): A List of Dictionaries 
        n (Int): Max size of `output`
        input (Dict): Potential dict to be inserted in `output`
    """
    if output[n-1]["score"] > input["score"]:
        # If our input's score is lower than the lowest (last) output score, pass
        pass
    else:
        # Do insertion whenever possible
        for i in range(0,n):
            if output[i]["score"] < input["score"]:
                print(f"Inputting {input['score']} over {output[i]['score']}")
                # Pop last (lowest) value, then insert our new value in-place so rest "slide down" and we keep max size `n`
                output.pop()
                output.insert(i, input)
                print(output)
                break
            else:
                print("Not inserting...")
    return output


## Parse CLI args
if len(sys.argv) != 3:
    print("ERROR: Improper input")
    print("e.g. `python highest.py file.txt 10`")
    exit(1)
file_name = sys.argv[1]
n = int(sys.argv[2])
file = open(file_name, 'r')
if not file:
    print(f"ERROR: Failed to read {file_name}")
    exit(1)
    
## Setup `output` to fixed size `n` with default values to get overwritten
output = collections.deque(maxlen=n)
for i in range(0,n):
    output.append({"score": -1, "id": -1})
    
## Read through file, line by line
count = 0
while True:
    line = file.readline()
    if line != '\n':
        # parse non-empty String `line` into Dict `input` according to spec
        m = re.search("^[\d]+", line)
        score = m.group(0)
        m = re.search("\{.*\}", line)
        d = json.loads(m.group(0))
        if not d or not score:
            print("ERROR: Improper line format")
            exit(2)
        id = d["id"]
        input = {"score": int(score), "id": id}
        # Try inserting `input` into `output`
        output = insertion(output, n, input)
    else:
        break
