# <<<<<<<<<<<<<<<<<<<[ IMPLEMENTAION OF HUFFMAN CODING]>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import heapq

class BinarytreeNode:
    def __init__(self,value,frequency):
        self.value=value
        self.frequency=frequency
        self.left=None
        self.right=None

    # overloading less than operator function..!
    def __lt__(self, other):
        return self.frequency<other.frequency


#    overloading equal to operator function..!
    def __eq__(self, other):
        return self.frequency==other.frequency



class HuffmanCoding:
    def __init__(self,path):
        self.path=path
        self.__heap=[]
        self.__codes={}
        #heap is maintained as the list...!!!


    def __make_frequency_dict(self,text):
        freq_dict={}
        for char in text:
            # freq_dict[char]=freq_dict.get(char,0)+1

            if char not in freq_dict:
                freq_dict[char]=0
            freq_dict[char]+=1

        return freq_dict

    def __buildHeap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            binary_tree_node=BinarytreeNode(key,frequency)
            heapq.heappush(self.__heap,binary_tree_node)
            print(self.__heap)


    def __builtTree(self):
        while len(self.__heap)>1:
            binary_tree_node_1=heapq.heappop(self.__heap)
            binary_tree_node_2=heapq.heappop(self.__heap)
            freq_sum=binary_tree_node_1.frequency+binary_tree_node_2.frequency
            combinational_node=BinarytreeNode(None,freq_sum)
            combinational_node.left=binary_tree_node_1
            combinational_node.right=binary_tree_node_2
            heapq.heappush(self.__heap,combinational_node)
        return

    def __buildCodesHelper(self,root,current_bits):
        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value]=current_bits

        self.__buildCodesHelper(root.left,current_bits+"0")
        self.__buildCodesHelper(root.right,current_bits+"1")

    def __buildCodes(self):
        # heap k last element hi binary tree ka root hoga.........!!!
        root=heapq.heappop(self.__heap)
        self.__buildCodesHelper(root,"")

    def __get_EncodedText(self,text):
        encoded_text=""
        for char in text:
            encoded_text+=self.__codes[char]
        return encoded_text

    def __getPaddedEncodedText(self,encoded_text):
        padded_amount=8-(len(encoded_text)%8)
        for i in range(padded_amount):
            encoded_text+="0"

        # logic of this format in the notes..!
        padded_info="{0:08b}".format(padded_amount)

        padded_encoded_text=padded_info+encoded_text
        return padded_encoded_text

    def __getBytesArray(self,padded_encoded_text):
        array=[]
        for i in range(0,len(padded_encoded_text),8):
            byte=padded_encoded_text[i:i+8]
            array.append(int(byte,2))
            # note:---int(value,base).....! second argument base of the number hota h...!

        return array

    def compress(self):
        # get file from the path
        # read text form the file"
        text="fasbsajfhbsafjhbashf"

        #make frequency dictionary using the text
        freq_dict=self.__make_frequency_dict(text)

        # construct the heap from the frequency_dict
        self.__buildHeap(freq_dict)

        #construct the binary tree from the heap
        self.__builtTree()

        # construct the codes from the binary tree
        self.__buildCodes()

        # creating encoded text using the codes
        encoded_text=self.__get_EncodedText(text)

       # pad the encoded text.!
        padded_encoded_text=self.__getPaddedEncodedText(encoded_text)

        # get the bytes array...!!!
        bytes_array=self.__getBytesArray(padded_encoded_text)

        #return this binary file as output
        final_bytes=bytes(bytes_array)

        #put this bytes into the binary file






        pass
