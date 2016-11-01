input = raw_input()
expression = input.split()
action = expression[0]
length_of_expression = len(expression)

class Term(object):

	def __init__(self, numeral=None, noun=None, adjective=None):
		self._numeral
        self._noun = noun
        self._adejctive = adjective

    @property
    def numeral(self):
        return self._numeral

    @numeral.setter
    def numeral(self, value):
        self._numeral = value
		
	@property
    def noun(self):
        return self._noun

    @noun.setter
    def noun(self, value):
        self._noun = value
		
	@property
    def adjective(self):
        return self._adjective

    @noun.setter
    def adjective(self, value):
        self._adjective = value

counter = 1
list_of_expressions = []
list_of_terms = []
while counter < length_of_expression:
	list_of_terms[counter] = Term(expression[counter],expression[counter+1],expression[counter+2])
	list_of_expressions.append(list_of_terms[counter])
	counter = counter + 3
	
# co zrobić, gdy przed rzeczownikiem nie ma liczebnika?