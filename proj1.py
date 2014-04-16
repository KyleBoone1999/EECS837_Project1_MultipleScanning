#This is the main program for Project #1 EECS 837
import math

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
		self.cutList = set(self.cutList).difference(set(self.cutpoints))
		return self.cutList

	def addCutPoint(self, cutValue):
		self.cutpoints.append(cutValue)
	

	def partition(self):
		self.partitionObj = Partition()
		if self.discreteValue:
			for case, discValue in self.discreteValue.iteritems():
				inducedPartition.addToElementalSet(case, discValue)
		else:
			for case, numValue in self.numericValue.iteritems():
				inducedPartition.addToElementalSet(case, numValue)
		return self.partitionObj


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

	def conceptHistogram(caseList):
		conceptHist = dict()
		for case in caseList:
			concept = decision[case]
			if conceptHist.get(concept):
				conceptHist(concept) += 1
			else:
				conceptHist(concept) = 1
		return conceptHist

	def condEntropyOneCutpoint(self, attribute, cutpoint)
		decision = self[-1]
		if not attribute.numericValue:
			return
		#Separate cases into low and high
		lowValues = list()
		highValues = list()

		for case, num in attribute.numericValue().iteritems():
			if num > cutpoint:
				highValues.append(case)
			else:
				lowValues.append(case)
		
		#Histogram of concepts for high list and low list
		lowValConcepts = conceptHistogram(lowValues)
		highValConcepts = conceptHistogram(highValues)

		totalLowCases = len(lowValues)
		totalHighCases = len(highValues)
		totalCases = totalLowCases + totalHighCases


		#Entropy
		sumLow = 0
		for concept, count in lowValConcepts.iteritems():
			sumLow += -1 * count/totalLowCases * math.log(count/totalLowCases,2)

		sumHigh = 0
		for concept, count in highValConcepts.iteritems():
			sumHigh += -1 * count/totalHighCases * math.log(count/totalHighCases,2)

		H = (totalLowCases * sumLow + totalHighCases * sumHigh) / totalCases

		return H

	def bestCutPoint(self, attribute):
		if self.numericValue:
			minEntropy = float(inf)
			minCutpoint = 0
			cutList = self.possibleCutList()
			if cutList:
				for cutpoint in self.possibleCutList():
					entropy = condEntropyOneCutpoint(self,attribute,cutpoint)
					if entropy < minEntropy:
						minEntropy = entropy
						minCutpoint = cutpoint
				self.addCutpoint(minCutpoint)
				self.fromNumericToDiscrete()
			else:
				return 
		else:
			return

	def mergeCutpoints(self):
		return

	def dominantAttribute(self):
		return

	def multipleScans(self, k):
		if k == 0:
			dominantArribute(self)
			return
		for attribute in self.attributeList[0:-2]:
			bestCutpoint(attribute)
		k -= 1
		while (k > 0):
			#find inconsistent cases
				#if found, select best cutpoint
			k -= 1

def is_numeric(string):
	try:
		float(string)
		return true
	except	ValueError:
		return false



def parser(inputFile):
	
	#Eliminate ! comments
	dataLines = inputFile.readlines()
	noComments = file('\\temp.d')
	for line in dataLines:
		noComments.write(line.split('!')[0])

	#Count number of attributes
	dataList = DataSet()
	wholeFile = noComments.read()
	attributeNames = ((wholeFile.split('[')[1]).split(']')[0]).split()

	#Initialize names of attributes
	for name in attributeNames:
		dataList.append(Attribute(name))
	
	
	#Add values to attributes
	dataValues = wholeFile.split(']')[1]
	if len(dataValues) < len(dataList):
		return dataList

	#Add first value to determine if values are discrete or numeric
	for attribute in dataList[0:-2]:
		value = dataValues[attribute]
		if is_numeric(value):
			attribute.numericValue[1] = value
		else:
			attribute.discreteValue[1] = value
	
	#Decision Values are always discrete
	dataList[-1].discreteValue[1] = dataValues[len(dataList)-1]
	
	#Add the rest of the values to the attributes
	caseCounter = 1
	while (len(dataValues) >= len(dataList)):
		dataValues = dataValues[len(dataList):-1]
		caseCounter += 1
		for attribute in dataList:
			value = dataValues[attribute]
			if attribute.numericValue:
				attribute.numericValue[caseCounter] = value
			else:
				attribute.discreteValue[CaseCounter] = value
	return dataList

def multipleScanning(inputFile, k):
	data = parser(inputFile)
	data.multipleScans(k)
	data.mergeCutpoints()
	data.makeCutpointFile()
	data.makeDiscretizedFile()

#Testing code:
multipleScanning('C:\...',3)





