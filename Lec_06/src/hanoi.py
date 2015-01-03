def hanoi(n,f,t,s):
	hanoi.counter += 1
	if n == 1:
		print "(", hanoi.counter, ")" +'move from ' +f +' = ' +t 
	else:
		hanoi(n-1,f,s,t)
		hanoi(1,f,t,s)
		hanoi(n - 1,s,t,f)
hanoi.counter = 0


hanoi(2,'f','t','s')