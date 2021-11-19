# <<<<<<<<<<<<<<<<<[ Compressing  and Decompressing a file by the implementation of the huffman coding]>>>>>>>>>>>>>>>>>>>>>>>

import heapq
import os
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
        self.__reverseCodes={}
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

            # storing the codes in dictionary!!!!
            self.__codes[root.value]=current_bits

            # storing the reverse codes in the dictionary..!
            self.__reverseCodes[current_bits]=root.value


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
        file_name,file_extention = os.path.splitext(self.path)
        output_path=file_name+".bin"

        with open(self.path,'r+') as file,open(output_path,'wb') as output:
            text=file.read()
            text=text.rstrip()

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
            output.write(final_bytes)

        print("Compressed")
        return output_path

    def __removePadding(self,text):
        padded_info=text[:8]
        extra_padding=int(padded_info,2)
        text=text[8:]
        text_after_padding_removed=text[:-1*extra_padding]
        return text_after_padding_removed

    def __decodeText(self,text):
        decoded_text=""
        current_bits=""

        for bit in text:
            current_bits+=bit
            if current_bits in self.__reverseCodes:
                character=self.__reverseCodes[current_bits]
                decoded_text+=character
                current_bits=""
        return decoded_text


    def decompress(self,input_path):
        filename,file_extension=os.path.splitext(self.path)
        output_path=filename+"_decompressed"+".txt"
        with open(input_path,'rb') as file,open(output_path,'w') as output:

            # bit_string is for saving the record of the bits
            bit_string=""

            # reading 1 byte at a time so we use 1 in the file.read() funciton..!
            byte=file.read(1)

            # we do it untill the bytes become none....!!!!
            while byte:
                byte=ord(byte)
                bits=bin(byte)[2:].rjust(8,'0')
                bit_string+=bits
                byte=file.read(1)

                #removing the padding...!!!!
            actual_text=self.__removePadding(bit_string)

            decompressed_text=self.__decodeText(actual_text)
            output.write(decompressed_text)
            print("Decompressed")
        return






# path='E:\\COMPUTER LANGUAGES FOLDER\\PYTHON PROGRAMMING\\DATA STRUCTURES AND ALGORITHM IN PYTHON\\21. HUFFMAN CODING\\sample.txt'
path='E:\\COMPUTER LANGUAGES FOLDER\\PYTHON PROGRAMMING\\DATA STRUCTURES AND ALGORITHM IN PYTHON\\21. HUFFMAN CODING\\sample.txt'
h=HuffmanCoding(path)
output_path=h.compress()

h.decompress(output_path)


