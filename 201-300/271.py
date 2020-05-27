class Solution:

    def encode(self, strs):
        encoded =""
        for word in strs:
            length = len(word)
            encoded += str(length) + "/" + word
        return encoded

    def decode(self, str):
         pos = 0
         decoded = []

         while pos < len(str):
             slash_pos = str.index("/", pos)
             length = int(str[slash_pos - 1])
             pos = slash_pos + 1

             decoded.append(str[pos: pos + length])
             pos += length
        return decoded


        
