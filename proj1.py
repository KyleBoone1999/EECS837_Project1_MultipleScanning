#This is the main program for Project #1 EECS 837

class Attribute:
	def __init__(self, attrName, numericBoolean):
		self.isNumeric = numericBoolean
		self.name = attrName
		self.numericValue = dict()
		self.cutpoints = list()		
		self.discreteValue = dict()

	def addNumericValue(case, numValue, self):
		if self.numericValue:
			self.numericValue.update(case,numValue)
		else:
			self.numericValue = dict((case,numValue))

	#Create sorted list to calculate possible cut values, min and max
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
		self.cutpoints.append(CutPoint(self, cutValue))
		self.cutpoints.sort(key=item.cutValue) #Look up syntax
	#Selects best cutpoint for a single attribute	
	def selectCutPoint(self):


	class CutPoint:
		def __init__(self, attribute, cutValue):
			self.name = attrName
			self.cutValue = cutValue
			self.low = attribute.sortedNumList[0]
			self.high = attribute.sortedNumList[-1]
			self.span = "%02d..%02d" %(self.low, self.high)

class DataSet:
	class casePartition:
		def __init__(self):
			self.elementalSetList = list()
			class elementalSet:
				def __init__(self):
					self.numberList = list()
					

	def __init__(self):
		self.attributeList = list()

	def partitionOfA(self):

	def partitionOfDecision(self):

	def kScans(self, k):

	def isConsistent(self, partition1, partition2):
		#for every elemental set in partition1, do the cases map to at most one set in partition2?
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





