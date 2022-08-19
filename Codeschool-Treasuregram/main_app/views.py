from django.shortcuts import render
#version 1
#from django.http import HttpResponse
#version 2 uses template views

# Create your views here.
def index(request):
#version 1
#	return HttpResponse('<hl>Hello Explorers!!!</hl>')
#version 2
#	#data
#	name = 'Gold Nugget'
#	value = 1000.0
#	#context to link to template
#	context = {'treasure_name': name,
#			   'treasure_val' : value }
#	return render(request,'index.html',context)
#version 3
	return render(request,'index.html',{'treasures' : treasures})
	
class Treasure:
	def __init__(self, name, value, material, location):
		self.name = name
		self.value = value
		self.material = material
		self.location = location

treasures = {
	Treasure('Gold Nugget', 500.0, 'gold', "Curly's Creek, NM"),
	Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
	Treasure('Coffee Can', 20.0, 'tin', 'Acme, CA')
}