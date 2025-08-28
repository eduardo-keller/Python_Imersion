import sys

def	downcase_it(s : str) -> str:
	"""transform al chars in lowercase"""
	return(s.lower())

def call_downcase(s : list[str]) -> int:
	"""iterates over list and calls downcase"""
	if len(s) == 1:
		print("None")
		return(0)
	for i in range(1, len(sys.argv)):
		print(downcase_it(sys.argv[i]))
	return(0)

if __name__=="__main__":
	call_downcase(sys.argv)
