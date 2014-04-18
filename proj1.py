#This is the main program for Project #1 EECS 837
import os,sys,math

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
	
	def findConflictingCases(self, decision):
			disjointSet = DisjointDict(decision)
		for elementalSet in self.elementalSets:
			for case1 in range(elementalSet.cases[0:-2]:
					for case2 in elementalSet.cases[case1:-1]:
						if disjointSet.find(case1) != disjointSet.find(case2): #conflicting cases
							return elementalSet.cases

class Attribute:
	def __init__(self, attrName):
		self.name = attrName
		self.numericValue = dict()
		self.cutpoints = list()		
		self.discreteValue = dict()

	def sortedPointsList(self):
		if self.numericValue:
			self.sortedPoints = sorted(self.cutpoints.append(min(self.numericValue.values()),max(self.numericValue.values())))
	
	def fromNumericToDiscrete(self):
		sortedPointsList()
		for case, numValue in self.numericValue.iteritems():
			intervalStart = maxBelow(numValue,sortedPoints)
			discValue = "%d..%d"%(self.sortedPoints[intervalStart],self.sortedPoints[intervalStart+1])
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


	def possibleCutList(self):
		self.cutList = list()
		self.sortedNumList = sorted(self.numericValue.values())
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

	def condEntropy(self,attribute,cutpoint):
		#If no numeric values, then skip cutpoint calculation
		if not attribute.numericValue:
			return float(inf)

		#Add cutpoint temporarily
		attribute.cutpoints.append(cutpoint)
		attribute.fromNumericToDiscrete()

		decision = self.attributeList[-1]

		#list cases by attribute values
		valueDict = dict()
		
		for case, value in attribute.discreteValue.iteritems():
			if valueDict.get(value):
				valueDict(value).append(case)
			else:
				valueDict(value) = list(case)

		#histogram of concepts by for each case list		
		caseListEntList = list()
		H = 0
		for value, caseList in valueDict.iteritems():
			caseListHist = conceptHistogram(caseList)
			caseListEnt = 0
			for concept, count in caseListHist.iteritems():
				caseListEnt += -1 * count/len(caseList) * math.log(count/len(caseList),2)
			caseListEntList.append(caseListEnt)
			H += len(caseList) / len(attribute.numericValue) * caseListEnt

		#Remove cutpoint
		attribute.cutpoints.pop()
		if attribute.cutpoints:
			attribute.fromNumericToDiscrete()
		else:
			attribute.discreteValue = list()

		return H

	
	def condEntropyAttribute(self,attribute):
		if not attribue.numericValue:
			return float(inf)

		decision = self.attributeList[-1]

		#list cases by attribute values
		valueDict = dict()
		
		for case, value in attribute.numericValue.iteritems(): #uses numeric values instead of discrete
			if valueDict.get(value):
				valueDict(value).append(case)
			else:
				valueDict(value) = list(case)

		#histogram of concepts by for each case list		
		caseListEntList = list()
		H = 0
		for value, caseList in valueDict.iteritems():
			caseListHist = conceptHistogram(caseList)
			caseListEnt = 0
			for concept, count in caseListHist.iteritems():
				caseListEnt += -1 * count/len(caseList) * math.log(count/len(caseList),2)
			caseListEntList.append(caseListEnt)
			H += len(caseList) / len(attribute.numericValue) * caseListEnt
		return H



	def bestCutPoint(self, attribute):
		if self.numericValue:
			minEntropy = float(inf)
			minCutpoint = 0
			cutList = self.possibleCutList()
			for cutpoint in cutList:
				entropy = condEntropy(self,attribute,cutpoint)
				if entropy < minEntropy:
					minEntropy = entropy
					minCutpoint = cutpoint
			self.addCutpoint(minCutpoint)
			self.fromNumericToDiscrete()
			return minCutpoint

	def bestCutpointSelect(self):
		cutpointDict = dict()
		for attr in self.attributeList[0:-2]:
			cutPointDict[attr] = self.bestCutPoint(attr)
		minAttr = min(cutPointDict, key= cutPointDict.get)
		return minAttr, cutPointDict[minAttr]
			

	def isConsistent(self):		
		return self.partitionOfA.isConsistent(self.attributeList[-1])

	def findInconsistentCases(self, partition):
		return self.partitionOfA.findConflictingCases(self.attributeList[-1])

	

	def mergeCutpoints(self):
		for attribute in self.attributeList:
			for cutpoint in attribute.cutpoints:
				attribute.cutpoints = set(attribute.cutpoints).difference(cutpoint)
				attribute.fromNumericToDiscrete()
				if not self.isConsistent():
					attribute.addCutpoint(cutpoint)
					attribute.fromNumericToDiscrete()
	def makeAcurr(self, caseList):
		Acurr = Dataset()
		for attr in self.attributeList[0:-2]:
			if attr.cutpoints:
				#Copy Name
				Acurr.attributeList.append(Attribute(attr.name))
				currAttr = Acurr.attributeList[-1]
				#Copy Cutpoints
				for cutpoint in attr.cutpoints:
					currAttr.cutpoints.append(cutpoint)
				#Copy numeric values for case list
				for case in caseList:
					currAttr.numericValue[case] = attr.numericValue[case]
				#make possible cut point list
				currAttr.possibleCutList()
				#make discretized values
				currAttr.fromNumericToDiscrete()

		return Acurr
			

	def dominantAttribute(self):
		if self.isConsistent():
			return
		#Find dominant attribute by conditional entropy among all attributes and all cases
		attrEntropyDict = dict()
		for attribute in self.attributelist[0:-2]:
			if attribute.numericValue:
				attrEntropyDict[attribute] = self.condEntropyAttribute(attribute)
		dominantAttribute = min(attrEntropyDict,key=attrEntropyDict.get)
		self.bestCutpoint(dominantAttribute)

		while not self.isConsistent():
			#find inconsistent cases
			caseList = findConflictingCases()
			#Make Acurr
			Acurr = self.makeAcurr(caseList)
			#find dominant attribute using conditional entropy among all attributes for conflicting cases
			attrEntropyDict.clear()
			for attribute in Acurr.attributeList[0:-2]:
				if attribute.numericValue:
					attrEntropyDict[attribute] = Acurr.condEntropy(attribute)			
			dominantAttribute = min(attrEntropyDict, key = attEntropyDict.get)
			cutPoint = (Acurr.bestCutpoint(dominantAttribute))
			#Find dominant attribute in complete table
			for attr in self.attributeList:
				if attr.name == dominantAttribute.name:
					attr.addCutpoint(cutPoint)
					attr.fromNumericToDiscrete()
					break
		return

	def multipleScans(self, k):
		if k == 0:
			self.dominantArribute(self)
			return
		for attribute in self.attributeList[0:-2]:
			self.bestCutpoint(attribute)
		k -= 1
		while (k > 0):
			if self.isConsistent():
				print("Data is consistent with " + str(k) + " scans remaining.\n")
				return
			#find inconsistent cases
			caseList = findConflictingCases()
			#Make Acurr
			Acurr = self.makeAcurr(caseList)
			#select best cutpoint for all attributes from list of inconsistent cases
			selectAttr, selectCutpoint = Acurr.bestCutpointSelect()
			#Find selected attribute in complete table
			for attr in self.attributeList:
				if attr.name == selectAttr.name:
					attr.addCutpoint(selectCutpoint)
					attr.fromNumericToDiscrete()
					break
			k -= 1
		dominantAttribute()

	def makeCutpointFile(self, inputFile):
		cutpointFilePath = os.path.dirname(inputFile)
		cutpointFileName = os.path.basename(inputFile) + '.int'
		#For every attribute list name, then intervals
		for attribute in self.attributeList:
			if attribute.numericValue:
				attribute.sortedPointsList()
				cutpointFile.write(attribute.name + ': ')
			pointNum = len(attribue.sortedPoints)
			for i in range(pointNum - 3):
				cutpointFile.write(attribute.sortedPoints[i] + '..' + attribute.sortedPoints[i+1] + ',')
			cutpointFile.write(attribute.sortedPoints[-2] + '..' + attribute.sortedPoints[-1])
			cutpointFile.write('\n')
		cutpointFile.close()

	def makeDiscretizedFile(self, inputFile):
		discretizedFilePath = os.path.dirname(inputFile)
		discretizedFileName = os.path.basename(inputFile) + '.discretized.data'
		discretizedFile = open(discretizedFilePath + discretizedFileName, 'w') 
		#write header
		discretizedFile.write('<')
		for attribute in self.attributeList[0:-2]:
			discretizedFile.write(' a')
		discretizedFile.write(' d>\n[ ')
		for attribute in self.attributeList:
			discretizedFile.write(attribute.name + ' ')
		discretizedFile.write(']\n')
		#write discretized data
		numCases = len(self.attributeList[-1].discreteValue)
		for caseCounter in range(numCases):
			for attribute in self.attributeList:
				if attribute == self.attributeList[-1]:
					discretizedFile.write(attribute.discreteValue[caseCounter] + '\n')
				else:
					if attribute.discreteValue:
						discretizedFile.write(attribute.discreteValue[caseCounter] + ' ')
					else:
						discretizedFile.write(attribute.numericValue[caseCounter] + ' ')
		return

def is_numeric(string):
	try:
		float(string)
		return true
	except	ValueError:
		return false

def is_positive_integer(string):
	try:
		int(string)
		return int(string) >=0
	except ValueError:
		return false
		

def parser(inputFile):
	
	#Eliminate ! comments
	dataLines = inputFile.readlines()
	noCommentPath = os.path.dirname(inputFile)
	noComments = open(noCommentPath + 'noComments.txt', 'w')

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
				attribute.discreteValue[caseCounter] = value
	return dataList

def getInputFile():
	inputFile = raw_input("What is the input file?")
	if os.path.isfile(inputFile):
		return inputFile
	print("Input file was not valid.\n")
	return getInputFile()

def getKvalue()
	k = raw_input("What is the value of k?")
	if k is_positive_integer():
		return k
	print("Value for k was not valid"\n)
	return getKValue

def multipleScanning(inputFile, k):
	data = parser(inputFile)
	data.multipleScans(k)
	data.mergeCutpoints()
	data.makeCutpointFile(inputFile)
	data.makeDiscretizedFile(inputFile)

#Testing code:
inputFile = getInputFile()
kValue = getKvalue()
multipleScanning(inputFile,kValue)
