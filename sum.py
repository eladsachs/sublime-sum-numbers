import sublime_plugin


class SumCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sum = 0
		line = self.view.line(self.view.sel()[0])
		lineContents = self.view.substr(line)
		table = lineContents.maketrans('','',',$£₹₱₩¥₾') #construct translate table
		lineContents = lineContents.translate(table) #remove characters from table
		for num in lineContents.split("\n"):
			sum += typeConvert(num)
		self.view.insert(edit,line.end(), '\n\n'+str(sum))


def typeConvert(str):
	try:
		return int(str)
	except ValueError:
		return float(str)
