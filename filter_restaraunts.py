class Solution(object):
	def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
		"""
		:type restaurants: List[List[int]]
		:type veganFriendly: int
		:type maxPrice: int
		:type maxDistance: int
		:rtype: List[int]
		"""

		restaurants = [restaraunt for restaraunt in restaurants if 
			self.filterVegan(restaraunt, veganFriendly) and
			self.maxPrice(restaraunt, maxPrice) and
			self.maxDistance(restaraunt, maxDistance)]

		return self.sortedOnId(restaurants)

	def filterVegan(self, l, vegan):
		if vegan==1:
			return l[2] == 1
		else:
			return True

	def maxPrice(self, l, p):
		return l[3] <= p

	def maxDistance(self, l, d):
		return l[4] <= d

	def sortedOnId(self, restaurants):
		def idKey(restaraunt):
			return restaraunt[0]

		def ratingKey(restaraunt):
			return restaraunt[1]

		restaurants = sorted(sorted(restaurants, key=idKey, reverse=True), key=ratingKey, reverse=True)
		return [r[0] for r in restaurants]





restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 0
maxPrice = 50
maxDistance = 10


print(Solution().filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))