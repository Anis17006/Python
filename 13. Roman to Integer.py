class solution:
	def romantoint(self, s:str):
		value={'M':1000, 'D':500, 'C':100, 'L':50,'X':10, 'V':5, 'I':1}
		num=0
		for i in range (len(s)-1):
			if value[s[i]]>=value[s[i+1]]:
				num+=value[s[i]]
			else:
				num-=value[s[i]]
		num=num+value[s[len(s)-1]]
		return num
sol=solution()
print(sol.romantoint("MCMXCIV"))
