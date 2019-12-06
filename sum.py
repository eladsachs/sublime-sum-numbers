import sublime_plugin


class SumCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sum = 0
		line = self.view.line(self.view.sel()[0])
		lineContents = self.view.substr(line)
		for num in lineContents.split("\n"):
			sum += float(num)
		self.view.insert(edit,line.end(), '\n\n'+str(sum))
