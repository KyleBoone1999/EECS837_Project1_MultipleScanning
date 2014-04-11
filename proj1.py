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

class Partition:
	def __init__(self):
		self.elementalSets = list()
	
	def addToElementalSet(self, case, sharedValue):
		for elementalSet in self.elementalSets:
			if (sharedValue == elementalSet.sharedValue):
				elementalSet.cases.append(case)
		self.elementalSets.append(ElementalSet(case, sharedValue))
	
	def mergePartition(self, partition2)
		disjointSet = DisjointDict(partition2)
		for elementalSet in self.elementalSets:
			for case1 in elementalSet.cases:#needs more work


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
			return maxLow(value,sortedList[midpoint:-1])
		elif value < sortedList[midpoint]:
			return maxLow(value,sortedList[0:midpoint])
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
		partitionD = Partition()
		for case, concept in d.discreteValue.iteritems():
			partitionD.addToElementalSet(case, concept)
		return partitionD




	def kScans(self, k):

	def isConsistent(self, partition1, partition2):
		#for every elemental set in partition1, do the cases map to exactly one set in partition2?
		return consistentBoolean

	def condEntropy(self):
		return entropyValue

	#For a given dataset, returns the best cutpoint among multiple attributes
	def cutpointSelect(self):	

def multipleScanning(inputFile, k):
	
	dataset = parser(inputFile)
	d = dataset.decision

	#Algorithm for Multiple Scanning
	
	#Find the best k-cutpoints for each attribute using minimal conditional entropy
		discretizedTable = kScans(dataset, k)

	#Determine if discretized values are inconsistent with data
	while(not isConsistent(discretizedTable, d)):
	
		#Find the dominant attribute using all indistguishable blocks with conflicting cases
		subTable = conflictingCases(discretizedTable,d)
		domAttr = dominantAttribute(subTable) #domAttr is the dict object containing all original attr. values
	
		#Find the best cutpoint for the dominant attribute using minimal conditional entropy
		AddCutpoint(domAttr,discretizedTable,d))

	return discretizedTable

def parser(inputFile):
	DataList = DataSet()
	array = inputFile.read()
	#Eliminate comments
	#Count number of a's
	#Figure out where d is
	#eliminate whitespace
	#Store attributes with name and if attribute is numeric or not
	#Store decision with name and it cannot be numeric
	return DataList

#Testing code:
multipleScanning('C:\...',3)





