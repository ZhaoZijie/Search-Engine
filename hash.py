def hashtable_updata(htable,key,value):
	bucket = hashtable_get_bucket(htable,key)
	for entry in bucket :
		if entry[0] == key:
			entry[1] = value
			return 
	bucket.append([key,value])


def hashtable_add(htable,key,value):
	bucket = hashtable_get_bucket(htable,key)
	for entry in bucket :
		if entry[0] == key :
			return entry[1]
	return None



def hashtable_get_bucket(htable,keyword):
	return htable[hash_string(keyword,len(htable))]


def hash_string(keyword,buckets):
	out = 0
	for s in keyword:
		out = (out + ord(s)) % buckets
	return out

def make_hashtable(nbuckets):
	tabel = []
	for unused in range(0,nbuckets):
		tabel.append([])
	return table