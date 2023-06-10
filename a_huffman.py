# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding

message = message.upper()
# STEP 0 - TODO
## defining our data structures
class Node: # NOT given to students
    # TODO
    
    def __init__(self, weight, letter, left, right):
        self.weight = weight
        self.letter = letter
        self.left = left
        self.right = right
        


## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letter != None: # if 'TODO': # TODO
        coding[v.letter] = path # TODO
    else:
        #go left
        retrieve_codes(v.left, path + '0') # TODO
        #go right
        retrieve_codes(v.right, path + '1') # TODO

# STEP 1
## counting the frequencies - TODO
for letter in message:
    if letter not in freq.keys():
        freq[letter] = 1
    else:
        freq[letter] += 1




# STEP 2
## initialize the nodes - TODO
nodes = list()
for letter, count in freq.items():
    nodes.append(Node(weight = count, letter = letter, left = None, right = None))



# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    combined: Node = Node(min_a.weight + min_b.weight, None, min_a, min_b) # TODO

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
newmessage = ""
for i in message:
    newmessage += coding[i]
result: str = str(newmessage) # TODO (hint coding[letter] -> code)

# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')