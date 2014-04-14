#This is the main program for Project #1 EECS 837

class DisjointDict:
	def __init__(self,elementSetList):
		self = dict()
		for elementSet in elementSetList:
			for case in elementSet.cases[1:-1]:
				union(elementSet.cases[0], case)

	def union(case1, case2):
		root1 = find(case1)
		root2 = find(case2)
		self.update(root2,root1)

	def find(case):
		if(self[case] != case):
			self.update(case, find(self[case]))
		return self[case]

class ElementalSet:
	def __init__(self, case, sharedValue):
		self.sharedValue = sharedValue
		self.cases = list()
		self.cases.append(case)
	
	def __init__(self)
		self.cases = list()

class Partition:
	def __init__(self):
		self.elementalSets = list()
	
	def addToElementalSet(self, case, sharedValue):
		for elementalSet in self.elementalSets:
			if (sharedValue == elementalSet.sharedValue):
				elementalSet.cases.append(case)
				return
		self.elementalSets.append(ElementalSet(case, sharedValue))

	def splitElementalSet(self, elementalSet, case2):
		#Add new elemental set to partition, starting with case2
		self.elementalSets.append(ElementalSet())
		#Remove elements from the original set to add them to the new list.
		for case in range(elementalSet[(case2):-1]):
			self.elementalSets[-1].cases.append(elementalSet.cases.pop())
	
	def mergePartitions(self, partition2)
		disjointSet = DisjointDict(partition2)
		for elementalSet in self.elementalSets:
			for case1 in range(elementalSet.cases[0:-2]:
					for case2 in elementalSet.cases[case1:-1]:
						if disjointSet.find(case1) != disjointSet.find(case2): #distinguishable by second attribute
							splitElementalSet(elementalSet, case2)
		return self

	def isConsistent(self, decision):
			disjointSet = DisjointDict(decision)
		for elementalSet in self.elementalSets:
			for case1 in range(elementalSet.cases[0:-2]:
					for case2 in elementalSet.cases[case1:-1]:
						if disjointSet.find(case1) != disjointSet.find(case2): #conflicting cases
							return false
		return true
						

class Attribute:
	def __init__(self, attrName):
		self.name = attrName
		self.numericValue = dict()
		self.cutpoints = list()		
		self.discreteValue = dict()

	def addNumericValue(self, case, numValue):
		self.numericValue.update(case,numValue)
	
	def fromNumericToDiscrete(self):
		sortedPoints = sorted(self.cutpoints.append(sortedNumList[-1],sortedNumList[0]))
		for case, numValue in self.numericValue.iteritems():
			intervalStart = maxBelow(numValue,sortedPoints)
			discValue = "%d..%d"%(sortedPoints[intervalStart],sortedPoints[intervalStart+1])
			self.discreteValue.update(case,discValue)

	def maxBelow(value, sortedList):
		midpoint = len(sortedList)/2
		if (sortedList[midpoint] <= value and sortedList[midpoint+1] >=value):
			return midpoint
		if value > sortedList[midpoint]:
			return maxBelow(value,sortedList[midpoint:-1])
		elif value < sortedList[midpoint]:
			return maxBelow(value,sortedList[0:midpoint])
		else:
			return midpoint

	def sortedNumericList(self):
		self.sortedNumList = sorted(self.numericValue.values())
		return self.sortedNumList

	def possibleCutList(self):
		self.cutList = list()
		for x in range(len(self.sortedNumList)-1):
			avg = (self.sortedNumList[x+1] + self.sortedNumList[x])/2.0
			if (avg > self.sortedNumList[x]):
				self.cutList.append(avg)
		return self.cutList

	def addCutPoint(self, cutValue):
		self.cutpoints.append(cutValue)
	
	def bestCutPoint(self, disjointSet):
		if self.numericValue:
			minEntropy = float(inf)
			minCutpoint = 0
			cutList = self.possibleCutList
			if cutList:
				for cutpoint in self.possibleCutList():
					entropy = self.condEntropy(cutpoint, disjointSet)
					if entropy < minEntropy:
						minEntropy = entropy
						minCutpoint = cutpoint
				self.addCutpoint(cutpoint)
				self.fromNumericToDiscrete()
			else:
				return 
		else:
			return

	def condEntropy(self, disjointSet)
	#Need to finish!
		return 0

	def partition(self):
		inducedPartition = Partition()
		if self.discreteValue:
			for case, discValue in self.discreteValue.iteritems():
				inducedPartition.addToElementalSet(case, discValue)
		else:
			for case, numValue in self.numericValue.iteritems():
				inducedPartition.addToElementalSet(case, numValue)
		return inducedPartition


class DataSet:
	def __init__(self):
		self.attributeList = list()

	def partitionOfA(self):
		partitionList = list()
		for attr in self.attributeList[0:-2]:
			partitionList.append(attr.partition())
		while len(partitionList) > 1:
			partitionList[0].mergePartitions(partitionList[-1])
			partitionList.pop()
		return partitionList[0]

	def partitionOfDecision(self):
		d = self.attributeList[-1]
		return d.partition()


	def kScans(self, k):
		if k == 0:
			dominantArribute(self)
			return
		decisionDisjointSet = DisjoinDict(self.attributeList[-1].partition())
		for attribute in self.attributeList[0:-2]:
			attribute.bestCutpoint(decisionDisjointSet)
		for i in range(k-1):


def parser(inputFile):
	DataList = DataSet()
	wholeFile = inputFile.read()
	#Eliminate comments
	
	#Count number of a's
	#Figure out where d is
	#eliminate whitespace
	#Store attributes with name and if attribute is numeric or not
	#Store decision with name and it cannot be numeric
	return DataList

#Testing code:
multipleScanning('C:\...',3)





