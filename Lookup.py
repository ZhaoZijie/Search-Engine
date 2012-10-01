def Lookup(index,word):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]

	return []