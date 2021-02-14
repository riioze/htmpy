
#########
# Const #
#########
ETAGLIST = ['area',
			'base',
			'basefont',
			'br',
			'col',
			'frame',
			'hr',
			'img',
			'input',
			'isindex',
			'link',
			'meta',
			'param',
			'source'
			]

#########
# Class #
#########
class tag:
	"""tag element"""
	def __init__(self,_type,attributes={}):
		"""generate a tag element
		attributes correspond to the html attributes
		_type corresponds to the tag name"""
		self.attributes = attributes
		self.type = _type
		self.emptytag = False
		if self.type in ETAGLIST:
			self.emptytag=True
		self.children = []

	def generate_attributes(self):
		"""generate a string with all the attributes
		like this : attrname = \"value\""""
		r = ' '

		if self.attributes == {}:
			return ''

		for attn,value in self.attributes.items():
			r+= attn + " = \"" + value + "\" "


		return r

	def render(self,d=0):
		"""generate the tag as a string with chidrens and text inside"""
		r = ''
		if self.type == 'html':
			r+='<!DOCTYPE html>\n'
		r+='<'+self.type
		r+=self.generate_attributes()
		r+='>\n'
		if not self.emptytag:
			for c in self.children:
				r+='\t'*(d+1)
				if type(c) == tag:
					r+=c.render(d=d+1)
				else:
					r+=str(c)
				r+='\n'
			r+='\t'*d
			r+='</'+self.type+'>'
		return r

	def add(self,toadd):
		"""add a new children. It can be a tag or text"""
		self.children.append(toadd)

#############
# Fonctions #
#############

def createEmptyPage(title=None,header = False,footer=False):
	"""create an empty page with a head and a body
	optinal : title,header,footer
	returns the root, the head and the body and present : header and/or footer"""
	root = tag('html')
	head = tag('head')
	body = tag('body')
	root.add(head)
	root.add(body)
	r = [root,head,body]
	if title:
		titleTag = tag('title')
		titleTag.add(title)
		head.add(titleTag)
	if header:
		headerTag = tag('header')
		body.add(headerTag)
		r.append(headerTag)
	if footer:
		footerTag = tag('footer')
		body.add(footerTag)
		r.append(footerTag)
	return tuple(r)

##################
# body for tests #
##################
if __name__ == '__main__':
	
	root,head,body,header,footer = createEmptyPage('testpage',True,True)


	print(root.render())