class solution:
	def twosum(self,nums:list[int],target:int):
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[i]+nums[j]== target:
					return [i,j]
s1=solution()
x=s1.twosum([2,7,3,5],9)
print(x)