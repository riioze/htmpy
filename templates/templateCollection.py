from webTemplate import *


#####################
# templates classes #
#####################

class wikiTemplate(webTemplate):
	""" a template to create a page of wiki"""
	def __init__(self,title,bgcolor='white'):
		webTemplate.__init__(self,title)
		self.header = tag('header')
		self.body.add(self.header)
		self.sheet.add(rule('background-color',bgcolor,'html'))
		mainFlex = createBatch('#top',[('display','flex'),('flex-direction','horizontal')])
		self.sheet.addList(mainFlex)
		self.sheet.addList(createBatch('#menu',[('width','20%'),('padding-right','20px')]))
		maintitle = tag('h1')
		maintitle.add(title)
		self.body.add(maintitle)		
		self.divmenu = tag('div',{'id':'menu'})
		self.menu = tag('ol')
		self.top = tag('div',{'id':'top'})
		self.body.add(self.top)
		self.top.add(self.divmenu)
		self.divmenu.add(self.menu)
		self.article = tag('article')
		self.body.add(self.article)

		self.sections = {}

	def addIntro(self,intro):
		""" add an intro placed just beside the menu """
		divIntro = tag('div',{'id':'intro'})
		divIntro.add(intro)


		self.top.add(divIntro)

	def addAside(self,aside,bgcolor='white',bordercolor='black'):
		""" add an aside beside the intro 
		aside : tuple with the aside and the styleSheet
		/!\\ call before addIntro
		"""
		asideTag,sheet = aside
		self.top.add(asideTag)
		self.sheet.rules+=sheet.rules
		self.sheet.medias+=sheet.medias
		self.sheet.addList(createBatch('#intro',[('width','50%'),('padding-right','20px')]))
		self.sheet.addList(createBatch('aside',[('background-color',bgcolor),('border',('1px',bordercolor))]))


	def addSection(self,_id,sectionName,parentid=None):
		"""creates a section with an id and a section name
		if parentid creates the section as a child of the section with th id parentid
		else creates the section as independant of the other ones
		"""
		section = tag('div',{'id':sectionName})
		inMenu = tag('li')
		link = tag('a',{'href':'#'+sectionName})
		link.add(sectionName)
		inMenu.add(link)
		childlist = tag('ol')
		inMenu.add(childlist)

		
		if parentid!=None:
			if parentid in self.sections.keys():
				psection,pmenu,pdepth = self.sections[parentid]
				psection.add(section)
				pmenu.add(inMenu)
				depth = pdepth+1
				
			else: return -1
		else:
			self.menu.add(inMenu)
			self.article.add(section)
			depth = 0

		self.sections[_id]=(section,childlist,depth)
		stitle = tag('h'+str(depth+2))
		stitle.add(sectionName)
		section.add(stitle)
			


class Aside:
	def __init__(self,title=''):
		self.main = tag('aside')
		self.tTag = tag('h2')
		self.table = tag('table')
		self.tRow = tag('row')

		self.main.add(self.table)
		self.table.add(self.tRow)
		self.tTh = tag('th')
		self.tTh.add(self.tTag)
		self.tRow.add(self.tTh)
		self.tTag.add(title)
		self.sheet = styleSheet()

	def addSection(self,stitle,content):
		tr = tag('tr')
		self.table.add(tr)
		td = tag('td')
		tr.add(td)
		td.add(stitle)
		td.add(tag('br'))
		td.add(content)

		print([child.type for child in self.table.children])

	def get(self):
		return self.main, self.sheet
	








if __name__ == '__main__':
	
	wiki = wikiTemplate('wiki')

	wiki.addIntro('sqmojqsjcmwjcjlwbxcjqsouqskxohdqopjfqsopjcop')

	aside = Aside('test')
	aside.addSection('test2','qsdhskqcnlkjxcsojm<br>ôeij')

	wiki.addAside(aside.get())

	wiki.addSection(0,'patate')
	wiki.addSection(1,'carottes')



	wiki.addSection(2,'patates de terre',0)

	wiki.save()

