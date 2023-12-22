# Function的參數(parameter)應用

# 1
def add(x, y):
	print(x + y)

add(3, 4) # 印出7

# 2
def add(x=2, y=3): # 參數可以有預設值，寫法左右不用空格
	print(x + y)

add() # 執行可不給參數，代入預設值，印出5
add(10) # 可只給一個，另一個代預設值，印出13
add(y=5) # 可指定給哪個，印出7

# 3
def average(numbers):
	return sum(numbers) / len(numbers) # return回傳結果
	# numbers是清單，sum可以直接對整個清單做加總

print(average([1,2,3])) # 印出平均是2.0 因為除法會自動轉為float