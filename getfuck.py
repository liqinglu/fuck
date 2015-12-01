import os


def similarity1(stra, strb):
	lena = len(stra)
	lenb = len(strb)

	if lena == 0:
		if lenb == 0:
			return 0
		else:
			return lenb
	elif lenb == 0:
		if lena == 0:
			return 0
		else:
			return lena

	if stra[0] == strb[0]:
		return similarity1(stra[1:lena], strb[1:lenb])
	else:
		value1 = similarity1(stra[1:lena], strb) + 1
		value2 = similarity1(stra[1:lena], strb[1:lenb]) + 1
		value3 = similarity1(stra, strb[1:lenb]) + 1
		return min(value1, value2, value3)


def similarity2(a, b):
	n, m = len(a), len(b)
	if n > m:
		a, b = b, a
		n, m = m, n
	current = range(n+1)
	for i in range(1, m+1):
		previous, current = current, [i]+[0]*n
		for j in range(1, n+1):
			add, delete = previous[j]+1, current[j-1]+1
			change = previous[j-1]
			if a[j-1] != b[i-1]:
				change = change + 1
			current[j] = min(add, delete, change)
	return current[n]


def similarity3(first, second):
	if len(first) > len(second):
		first, second = second, first
	if len(second) == 0:
		return len(first)

	first_length = len(first) + 1
	second_length = len(second) + 1
	distance_matrix = [range(second_length) for x in range(first_length)]
	for i in range(1, first_length):
		for j in range(1, second_length):
			deletion = distance_matrix[i-1][j] + 1
			insertion = distance_matrix[i][j-1] + 1
			substitution = distance_matrix[i-1][j-1]
			if first[i-1] != second[j-1]:
				substitution += 1
			distance_matrix[i][j] = min(insertion, deletion, substitution)
	return distance_matrix[first_length-1][second_length-1]


def getlastcmd():
	hfile = "/.fuck/historycmd"
	home = os.getenv('HOME')
	absfile = home + hfile

	with open(absfile, 'r') as f:
		content = f.readlines()

	return content[-2].strip().split()[1]


def getmatchcmd(cmd):
	result = {}

	allpath = os.getenv('PATH').split(':')
	for spath in allpath:
		listfile = os.listdir(spath)
		for sfile in listfile:
			result.setdefault(similarity3(cmd,sfile), []).append(sfile)
	
	# print len(result)
	sortedkeys = sorted(result.keys())
	return sortedkeys[0], result[sortedkeys[0]]


def main():
	lastcmd = getlastcmd()
	# print "lastcmd is %s"%lastcmd
	matchcmd = getmatchcmd(lastcmd)
	if matchcmd[0] == 0:
		print "got it ---> ",
	else:
		print "you probably search ---> ",

	for cmd in matchcmd[1]:
		print cmd,

	print


def test():
	print similarity1('abcdef', 'cbceef')
	print similarity1('abcdef', 'cdrmyou')

if __name__ == "__main__":
	main()
	# test()
