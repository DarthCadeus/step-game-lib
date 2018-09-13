class Step:
	def __init__(self, prompt, choices=None, options=None):
		self.choices = choices  # should be a dictionary
		# like this
		# choices = {
		#     "1": Step object,
		#     "2": Step object
		# }
		# or None
		# that indicates a leaf
		self.options = options
		self.prompt = prompt

	def __call__(self):
		if self.choices:
			for opt in self.options:
				print(self.options[opt], ":", opt)
			answer = input(self.prompt)
			while not answer in self.choices:
				print("Not a choice, man!")
				answer = input(self.prompt)
			self.choices[answer]()  # call that choice
		else:
			print(self.prompt)  # the result, the leaf node
