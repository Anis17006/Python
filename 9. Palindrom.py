class solution:
	def ispalindrom(self,x:int) -> bool:
		y=x
		n=0
		while(x>0):
			b=x%10
			n=n*10+b
			x=x//10 
		if y==n:
			return True
		else:
			return False
s=solution()

print(s.ispalindrom(123454321))
