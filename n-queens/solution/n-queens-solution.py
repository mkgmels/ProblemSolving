class Solution:
    def solveNQueens(self, n):
        initial_pos=[n*"." for _ in range(n)]
        pos_dict={i:initial_pos[i][:i]+"Q"+initial_pos[i][i+1:] for i,val in enumerate(initial_pos)}
        positions=list(pos_dict.keys())
        subset,res=[],[]
        def backtrack(i):
            #Base cases
            if len(subset)==n:
                diff=[subset[j]-j for j in range(n)]
                d=0
                while d+1<len(diff):
                    if diff[d+1]+2==diff[d]:
                        return
                    d+=1
                if len(set(subset))!=len(subset) or len(set(diff))!=len(diff):
                    return
                    
                else:
                    res.append(subset.copy())
                    return



            for i in range(n):
                subset.append(positions[i])
                backtrack(i+1)
                subset.pop()
           
        backtrack(0)
        for i in range(len(res)):
            res[i]=[pos_dict[n] for n in res[i]]


        return res
