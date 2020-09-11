data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # 每讀1,000筆印一次進度(長度) # %是用來求"餘數"
			print(len(data))
print('檔案讀取完畢 , 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])