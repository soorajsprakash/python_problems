"""
A restaurant keeps a log of (eater_id, foodmenu_id) for all the diners.
The eater_id is a unique number for every diner and foodmenu_id is unique for every food item
served on the menu.
Write a program that reads this log file and returns the top 3 menu items consumed.
If you find an eater_id with the same foodmenu_id more than once then show an error.
(basically means one cant eat same food twice)
"""


def getTopFood(file) -> str:
	""" Returns top 3 foodmenu_id from a log file """

	try:
		with open(file) as logFile:
			eachLine = logFile.readlines()
			if len(eachLine) == 0:
				raise EOFError("Empty file")
			final = {}
			eachList = []
			for i in eachLine:
				pair = i.split(' ')
				if len(pair) != 2:
					continue

				pair[-1] = pair[-1].replace('\n', '')
				if pair[0] == pair[1]:
					continue

				if (pair not in eachList) and (pair[-1] not in final):
					eachList.append(pair)
					final[pair[-1]] = 1

				elif (pair not in eachList) and (pair[-1] in final):
					eachList.append(pair)
					final[pair[-1]] += 1

				elif pair in eachList:
					raise ValueError("eater_id with the same foodmenu_id occured more than once")

		top3 = sorted(final, key=final.get, reverse=True)[:3]
		top3AsString = ", ".join(top3)
		return top3AsString

	except EOFError:
		return "Empty file"

	except SyntaxError:
		return "Bad syntax"

	except FileNotFoundError:
		return "File not found"

	except ValueError:
		return "Duplicate entry found"

# getTopFood('logs/customers.log')
