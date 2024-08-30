import random

restart = True
verts = {
			"vert1": "",
			"vert2": "",
			"vert3": "",
			"vert4": "",
			"vert5": "",
			"vert6": "",
			"vert7": "",
			"vert8": "",
			"vert9": ""
		}
		
horzs = {
			"horz1": "",
			"horz2": "",
			"horz3": "",
			"horz4": "",
			"horz5": "",
			"horz6": "",
			"horz7": "",
			"horz8": "",
			"horz9": ""
		}

def ch(square, row):
	h_sqr = square // 3
	return str(round((row + 1) + (3 * h_sqr)))

def cv(square, column):
	v_sqr = square % 3
	return str(round((column + 1) + (3 * v_sqr)))

def get_new_sudoku():
	restart = True
	
	while True:
		random.seed()
		
		verts = {
			"vert1": "",
			"vert2": "",
			"vert3": "",
			"vert4": "",
			"vert5": "",
			"vert6": "",
			"vert7": "",
			"vert8": "",
			"vert9": ""
		}
		
		horzs = {
			"horz1": "",
			"horz2": "",
			"horz3": "",
			"horz4": "",
			"horz5": "",
			"horz6": "",
			"horz7": "",
			"horz8": "",
			"horz9": ""
		}
		
		strng = '123456789'
		for sqr in range(9):
			nums = [i for i in strng]
			
			for row in range(3):
				
				horz = ch(sqr, row)
				cur_h = horzs["horz" + horz]
				
				h_arr = list(filter(lambda x: x not in cur_h, nums))
				
				for clmn in range(3):
					
					vert = cv(sqr, clmn)
					cur_v = verts["vert" + vert]
					cur_h = horzs["horz" + horz]
					v_arr = list(filter(lambda x: x not in cur_v, h_arr))
					
					nums_len = len(v_arr)
					
					if nums_len:
						num_idx = random.randint(0, nums_len - 1)
					else:
						num_idx = 0
					
					num = "0"
					
					if len(v_arr) > 0:
						num = v_arr[num_idx]
						verts["vert" + vert] = cur_v + num
						horzs["horz" + horz] = cur_h + num
					else:
						restart = True
					
					if num in nums:
						nums.remove(num)
					if num in h_arr:
						h_arr.remove(num)
				if restart:
					break
			if restart:
				break
		if not restart:
			result = []
			for r in list(horzs.values()):
				result.append([int(i) for i in r])
			return result
		else:
			restart = False


if __name__ == '__main__':
	print(get_new_sudoku())
