babesP = input('please enter the number of participants:')
babes = int(babesP) #记得要转换一下，刚输入进来就是一个chr
pool = [] #【】是list ， （）是tuple， {}是set
print('participants\' info recording process started...\n\nEnter participant\'s number first, then the numbers of boys he has a crush on...\n\nif he likes nobody, please enter 0') #转义符\， return是\n
for n in range(babes):
	print('babe' , n+1 , '\nhis number?')
	a = input()
	tempuse = input('boys he loves?\n')
	if len(tempuse) >= 1:
		onetime = tempuse.split() #没有直接输入list或者tuple的方法
	if tempuse == 0:
		onetime = []
	for b in range(len(onetime)-1): #删去其中自恋的元素
		if onetime[b] == a:
			onetime.pop(b)
	l1 = list(set(onetime)) #删去其中相同的元素
	l1.sort() #整理好顺序
	l1.insert(0 , a) #在第一位置加上标签
	print('please check:')
	print(l1, '\n') #输出
	pool.append(l1) # tuple没有append操作，一旦定义了之后，里面元素的数量就固定了；所以选用list
