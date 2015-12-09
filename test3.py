def func(x):
	print('x is',x)
	x=2
	print('Changed local x to',x)

x=int(input('Enter x:'))
func(x)
print('Globle x is still',x)