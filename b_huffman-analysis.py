# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
MYSTERIOUS_DESTINY = 'Bayonetta, you mystery (Who...) You came along with a destiny (...Are you) This is your life A battlefield telling you who you are (A mystery) Bayonetta, this is your time (Hold tight) You gonna sparkle, You gonna shine (Moonlight) Girl when you fight, it looks like a dance You are magic, youre magic (Youre dancing beautifully) Cmon, cmon Come on, theres only one way. Your way. Cmon Come on, you know theres only one way. Your way. Dance, fight. Spin around, spin around. Dance, fight Fly higher, fly higher, fly higher. Bayonetta, you bury your loneliness deep down in your eyes (Beautiful, beautiful, so powerful, so lonely). Sadness lies in your smile (Lonely heart) But victory shines in your eyes. (You will find it) Youre still alive (Deep, deep-deep, deep down) (Deep down inside, victory) Ooooh...'
AL_FINE = 'Awoken by whispers of destiny I reach for you as youre calling out my name Longing for your touch to bring me back to life Only you can save me, rekindle this flame A hundred miles away I hear your heart It beats for me, we can never be apart This is the time I knew I knew you could be the only one to (We are one, fate has come now) Come and take away darkness (In this great moment) I know youll miss me when Im gone (Magic surrounds you) Save your tears, this is where we belong (Our, our love is true!) My desire, my Achilles heel Youve tamed this cursed beast The sorrow released I spread my wings We will fly into far away galaxies just you and I And when this ends Hold on tight to our memories Dont let them end I fall weak, I tremble to speak (Like stars, we glow) As I take my last breaths, Im the happiest Ive ever been (Shine on, shine on) Ocean blue, I look into your eyes (Trust, we are here now) I know that you will be here, by my side, (Theres no one else but you) My Cheshire'
TOMORROW_IS_MINE = 'You awoke me (Fight fire) Unleashed the fire in my heart (With fire) I will dance and Ill defeat them (My flames) Through the light and the dark (More bright) Your mistake was to (The moon) Underestimate my power (Is my fuel) Wont let go of the fight (Get lost) Til tomorrows mine (In my tide) I will ignite Dancin through the fire around me Ill never stop Youd better hide Now Im in the mood for a fight (Better watch out here I come) You wont know what hit you When I spin around Leave you in my dust Then bang bang Down down again Its my desire Going for the win Tomorrow Is Mine You better run (Better run) Dont wait here I come no (Grab your gun... Fire) The fuel in my fire wont run dry (Endless supply) It burns bright And you better hide (Take a hike) I came for a fight, yeah (Truth youll find is) Until Tomorrow Is Mine (Victorys mine) Dont miss me too much'
# DATA - mantras
RA_CHANT = 'O great beast of the sky, please hear my cry. Transform thyself from orb of light and me victory in this fight. I beseech thee, grace our humble game. But first, I shall call out thy name! WINGED DRAGON OF RA!'
SAVAGE_WOLF_FURY = 'O brilliant blade of coldest steel, rend the infinite darkness, and crush my enemies to nothing! SAVAGE WOLF FURY!'
ANCIENT_CATASTROPHE = 'O power that lies at the root of all creation, o memory inscribed in ages past, hear my call and arise before me! ANCIENT CATASTROPHE'
# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

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
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Peregrin Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## POKEMON
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = MYSTERIOUS_DESTINY[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(range(1, MAX_N), ratios, linestyle = '-.' , color = 'r', label='Mysterious Destiny')


## JIGGLE JIGGLE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = AL_FINE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(range(1, MAX_N), ratios, linestyle = '-.', color = 'g', label='Al Fine')

## ALPHABET
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = TOMORROW_IS_MINE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(range(1, MAX_N), ratios, linestyle = '-.', color = 'b', label='Tomorrow is Mine')

plt.xlabel('Message Length')
plt.ylabel('Compression Ratio')
plt.legend()

# PLOT 2
plt.subplot(2, 1, 2)

## Ra chat
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = RA_CHANT[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(range(1, MAX_N), ratios, linestyle = '-.' , label= 'Ra Chant')
plt.legend()

## GREEN LATERN'S OATH
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = SAVAGE_WOLF_FURY[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(range(1, MAX_N), ratios, linestyle = '-.' , label= 'Savage Wolf Fury')
plt.legend

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = ANCIENT_CATASTROPHE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)
plt.plot(range(1, MAX_N), ratios, linestyle = '-.' , label='Ancient Catastrophe')
plt.xlabel('length of message')
plt.legend()

plt.show()
