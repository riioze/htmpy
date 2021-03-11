from htmpy.html import *
from htmpy.css import *
from htmpy.htmlautomations import *
from htmpy.cssautomations import *



###########
# classes #
###########

class webTemplate:
	""" template to create a website """
	def __init__(self,title=None):
		""" creates the template """
		self.page,self.head,self.body = createEmptyPage(title)
		attrs = {}
		attrs['rel']='stylesheet'
		attrs['type']='text/css'
		attrs['href']='style.css'
		styleTag = tag('link',attrs)
		self.head.add(styleTag)
		self.sheet = styleSheet()

	def addRuleBatch(self,batch):
		"""to add a batch of rules to the template"""
		self.sheet.addList(batch)

	def addQuery(self,q):
		"""to add a query"""
		self.sheet.addQuery(q)

	def get(self):
		return self.page,self.sheet

	def save(self):
		self.page.save('index.html')
		self.sheet.save('style.css')

if __name__ == '__main__':
	webTemplate().save()