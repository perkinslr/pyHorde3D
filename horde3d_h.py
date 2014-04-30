#  horde3d_h.py
#  
#  Copyright 2014 Logan Perkins <perkins@gentoo-flip>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the Eclipse Public License 1.0
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
#  
#  

import os
os.system('gcc -E %s/Horde3DUtils.h -DDLL='' > horde3d.h'%os.environ.get('HORDE3DINCLUDE',os.getcwd()))

with open('horde3d.h') as f:
	data=f.read()

import re
structs=re.compile('struct ([a-zA-Z0-9]+).*?\n{*(\n*?.*?)*? enum [a-zA-Z]*.*?\n.*\n?([ 0-9a-zA-Z=,\n]+)?')

s={}

for struct in structs.findall(data):
	attrs=struct[2].replace(',','').replace(' ','').strip().split('\n')
	attrs1=[]
	values=[]
	for attr in attrs:
		if '=' in attr:
			attrs1.append(attr.split('=')[0])
			values.append(int(attr.split('=')[1]))
		else:
			if not values:
				values.append(0)
			else:
				values.append(values[-1]+1)
			attrs1.append(attr)
	values=iter(values)
	d={a:values.next() for a in attrs1}
	globals()[struct[0]]=type(struct[0],(),d)
	s[struct[0]]=globals()[struct[0]]



import cffi
ffi=cffi.FFI()
ffi.cdef(structs.split(data)[0])

cdefs=structs.split(data)[-1].replace('''};
};
''','\n').replace('\n ','\n')


cdefs=re.sub(' [a-zA-Z0-9]+::[a-zA-Z0-9]+ ',' int ',cdefs)

print >> open('out.txt','w'), cdefs

ffi.cdef(cdefs)


def getfunctions(lib):
	functions={}
	for f in re.findall('\n[a-zA-Z*]+ ([a-zA-Z0-9]+)\(',cdefs):
		try:
			functions[f]=getattr(lib,f)
		except:
			pass
	return functions

