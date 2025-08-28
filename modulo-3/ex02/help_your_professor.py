# class_3B = {
# "marine": 18,
# "jean": 15,
# "coline": 8,
# "luc": 9
# }
# class_3C = {
# "quentin": 17,
# "julie": 15,
# "marc": 8,
# "stephanie": 13
# }

# class_3A = {
# "quentin": 2,
# "julie": 2,
# "marc": 2,
# "stephanie": 2
# }

# class_30 = {}


def average(school_class: dict[str, int]) -> float:
	"""returns the average grade of the class"""
	grades = 0
	if not school_class:
		return 0
	for v in school_class.values():
		grades += v
	return (grades/len(school_class.values()))


# if __name__=="__main__":
# 	print(average(class_30))
