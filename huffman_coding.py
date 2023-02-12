import heapq

class Node:
    def __init__(self, freq, char, left=None, right=None):
         self.freq = freq
         self.char = char
         self.left = left
         self.right = right
         self.code = ''

    def __lt__(self, next):
        return self.freq < next.freq

############################# print mapping and storing the mapping in a dictionary ###########################

def print_nodes(node, val=''):
    codeword = val + str(node.code)

    if(node.left):
        print_nodes(node.left, codeword)
    if(node.right):
        print_nodes(node.right, codeword)
    if(not node.left and not node.right):
        print(node.char + "->" + codeword)
        huffman_encode[node.char] = codeword

##################### Reading text file with frequency distribution ###################################

file = open("text_freq", "r")
letters_with_freq = file.readlines()
chars = []
freqs = []
for line in letters_with_freq:
    char, freq = line[:-1].replace(r'\n', '\n').split("-")
    chars.append(char)
    freqs.append(float(freq))
file.close()

#######################################################################################################

nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, Node(freqs[x], chars[x]))

while len(nodes) > 1:

    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    left.code = 0
    right.code = 1

    int_node = Node(left.freq + right.freq, left.char + right.char, left, right)

    heapq.heappush(nodes, int_node)

huffman_encode = {}

print_nodes(nodes[0])

print(huffman_encode)
print(chars)

############################## Encoding the message in the text file ##################################

bit_string = ''

file = open('message', 'r')

while True:

    char = file.read(1)
    if not char:
        break
    
    # print(huffman_encode[char], end='')
    bit_string += huffman_encode[char]

file.close()

################################# Writing the bit string into a file ####################################

file = open('message_encode', 'wb')

i = 0

while i < len(bit_string):

    data = bytes([int(bit_string[i: i+8], 2)])
    # print(bit_string[i: i+8], data)
    if len(bit_string[i: i+8]) < 8:
        data = bytes([int(bit_string[i: i+8] + '0'*(8-len(bit_string[i: i+8])), 2)])
    file.write(data)

    i += 8


file.close()


################ Decoding the encoded message and writing original message in a file #######################

file = open('message_encode', 'rb')

bit_msg = ''

while (byte := file.read(1)):
    # print(byte, format(int.from_bytes(byte, byteorder='big'), '08b'))
    # print(byte)
    bit_msg += format(int.from_bytes(byte, byteorder='big'), '08b')

file.close()

# for i in range(0, len(bit_msg), 8):
#     print(bit_msg[i: i+8], bit_string[i: i+8])


file = open('message_decode', 'w')

curr = nodes[0]

for j in range(len(bit_string)):
    if bit_msg[j] == '0' and curr.left:
        curr = curr.left
    if bit_msg[j] == '1' and curr.right:
        curr = curr.right
    if not curr.left and not curr.right:
        # print(curr.char, end="")
        file.write(curr.char)
        curr = nodes[0]

file.close()