#coding:utf-8

def hash_string(keyword,buckets):
	h = 0
	for c in keyword:
		h = (h + ord(c)) % buckets
	return h


#this is test
def test_hash_function(func,keys,size):
	results = [0] * size
	keys_used = []
	for w in keys:
		if w not in keys_used:
			hv = func(w,size)
			results[hv] += 1
			keys_used.append(w)
	return results
