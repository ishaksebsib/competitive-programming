class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		res=0
		p=0
		hashmap={0:1}

		for num in nums:
			p = p + num

			if p-k in hashmap:
				res = res + hashmap[p-k]

			if p not in hashmap:
				hashmap[p] = 1
			else:
				hashmap[p] = hashmap[p]+1

		return res
        
