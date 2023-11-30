class Node:
    def __init__(self, freq, char, left=None, right=None):
        self.char = char
        self.freq = freq
        # left el node
        self.left = left
        # right el node
        self.right = right
        # el huffman code 0/1
        self.huff_code = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def calcFreq(data):
    # H2ra el data w a3rf frequencies el characters w a store them fe dictionary
    # 3shan a map el data fe shakl char:freq
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print(frequency)
    for c, f in frequency.items():
        freq.append([c, f])

# func 3shan assign kol char bl huffman code bta3o
def storeHuffCodes(root, val=''):
    curr_node = root
    # tagmee3t el huffman codes bta3t el node elly ana feha
    newVal = val + str(curr_node.huff_code)

    # lw kan el node lsa leha children, h traverse feha
    if(curr_node.left):
        storeHuffCodes(curr_node.left, newVal)
    if(curr_node.right):
        storeHuffCodes(curr_node.right, newVal)

    # lw wslt ll leaf, h print el huffman code elly gm3tha
    if(not curr_node.left and not curr_node.right):
        huff_codes[curr_node.char] = newVal

# func b iterates fe el encodedString 3shan t7wl el huffman codes l characters
def decodeHuffCodes(root, encodedString):
    curr_node = root
    ans = ''
    for i in range(len(encodedString)):
        # lw el encodedString[i] = 0 -> yroo7 ll node el shmal
        # lw el encodedString[i] = 1 -> yroo7 ll node el ymeen
        if encodedString[i] == '0':
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

        # wslt ll leaf node, azwd el character fe le ans
        if(not curr_node.left and not curr_node.right):
            ans += curr_node.char
            # hrg3 ll root tany w abd2 mno 3shan a3rf el code elly b3deh
            curr_node = root
    return ans

# b2ra mn el text file
file = open('Data.txt', 'r')
data = file.readline()
file.close()
print(data)

encodedString, decodedString = "", ""
# list feha el nodes elly h create
nodes = []
# 3shan a map kol character l huffman code bta3o
huff_codes = {}
# frequencies el characters
freq = []
calcFreq(data)

# el node_data hta5od sets individual of two elements, el char w el freq
for node_data in freq:
    nd = Node(node_data[1], node_data[0])
    # hb3t ll func node el two elements dol 3shan a create node
    nodes.append(nd)

# Build el huffman tree
while len(nodes) != 1:
    # H sort el nodes in ascending order 3la 2sas el frequency
    nodes.sort()
    for i in range(len(nodes)):
        print(f'{nodes[i].char}: {nodes[i].freq}')

    # Ha5od as8r 2 nodes by frequency
    left = nodes.pop(0)
    right = nodes.pop(0)

    # A assign el huff codes. left node = 0, right node = 1
    left.huff_code = 0
    right.huff_code = 1

    # H combine kol 2 smallest nodes 3shan a create node tanya
    newNode = Node(left.freq + right.freq, left.char + right.char, left, right)

    # hrg3 a push el new combined node
    nodes.append(newNode)
print(f'{nodes[0].char}: {nodes[0].freq}')

print("\nFrequencies:")
for node_data in sorted(freq):
    print(f'{node_data[0]} -> {node_data[1]}')

print("\nHuffman codes:")
storeHuffCodes(nodes[0])
for key in huff_codes:
    print(f'{key} -> {huff_codes[key]}')

print("\nEncoded Huffman data:")
for i in data:
    encodedString += huff_codes[i]
print(encodedString)

print("\nDecoded Huffman data:")
decodedString = decodeHuffCodes(nodes[0], encodedString)
print(decodedString)