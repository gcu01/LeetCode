class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        common = [char for char in words[0]]
        #common = list(set(common))
        to_del = []
        print(common)
        for i in range(1, len(words)):
            #print("words[i]=", words[i])
            for val in common:
                #print("val = ", val)
                if val in words[i]:
                    index = words[i].find(val)
                    #print(index)
                    if index != -1:
                        words[i] = words[i][:index] + words[i][index+1:]
                    #print(words[i])                    
                else:
                    #common.remove(val)
                    #print("comon=",common)
                    to_del.append(val)
                #if common == []:
                #    return common
            #print("to_del=", to_del)
            if to_del != []:
                for litera in to_del:
                    common.remove(litera)
                to_del = []
        return common