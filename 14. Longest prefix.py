class solution:
	def longestcommonprefix(self,strs:[str]):
		strs.sort(key = len)
		prefix=""
		for i in range(len(strs[0])):
			for j in range(1,len(strs)):
				if strs[0][i]==strs[j][i]:
					flag=1
				else:
					flag=0
					break
			if flag==1:
				prefix+=strs[0][i]
			else:
				prefix='""'
				break
		
		return prefix
solve=solution()
y=solve.longestcommonprefix(["lower","flow","flight"])
print(y)