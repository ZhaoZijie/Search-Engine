#coding:utf-8
def is_palindrome(s):
	if  s == '' :
	    return True
	else:
		if s[0] == s[-1]:
			return is_palindrome(s[1:-1])
		else:
			return False

#用for循环来验证
def is_palindrome_for(s):
	for i in range(0,len(s)/2):
		if s[i] != s[-(i + 1)]:
			return False
	return True


#下面是简单的验证回文序列的方法
def is_palindrome_simple(s):
	return s == s[::-1]
