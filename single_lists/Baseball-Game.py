class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        out = []
        idx = -1

        for i in range(len(operations)):
            if operations[i].startswith('-') or operations[i].isdigit():
                idx += 1
                out.append(int(operations[i]))
                #print(out)
            elif operations[i].isalpha() == 1:
                if operations[i] == "D":                                       
                    out.append(2*out[idx])
                    idx += 1
                    #print("out[i] = ",out[idx])
                elif operations[i] == "C":
                    idx -= 1
                    out.pop()
                #print(out)
            else:
                if operations[i] == "+":                    
                    out.append(out[idx-1] + out[idx])
                    idx += 1
                #print(out)
        #print(out)
        return sum(out)        

