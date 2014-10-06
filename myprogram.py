from AsynchronizeMe import AsynchronizeMe

## Function Test ##
def fibonacci(*args):
	try:
		fib = [1,1]
		for i in xrange(2,args[0]): fib.append(fib[i-1]+fib[i-2])
		AsynchronizeMe().async_queue.put(fib[args[0]-1])
	except MemoryError as me: print "Memory overflow risk, aborted."
	except: print "Aborted."

## Callback Test ##
def callback_report_fibonacci(*args):
	print "\nFibonacci: "+str(args[0])+"\n"
	
def callback_report_list(*args):
	print "\nList: " + str(args) + "\n"
	
## Function 2 Test ##
def return_more_than_one_value(*args):
	new_list = [x for x in args if x%2==0]
	AsynchronizeMe().async_queue.put(new_list)
		
## Main programme ##
def init():
	print "pppp\n"
	## Try func-callback permutations ##
	AsynchronizeMe()._callback_exec_(fibonacci,callback_report_fibonacci,[50000])
	AsynchronizeMe()._callback_exec_(fibonacci,callback_report_fibonacci,[18000])
	AsynchronizeMe()._callback_exec_(fibonacci,callback_report_list,[15000])
	print "xxxx\n"
	print "tttt\n"
	## Try func-callback permutations ##
	AsynchronizeMe()._callback_exec_(return_more_than_one_value,callback_report_list,[i for i in range(0,3000,3)])
	AsynchronizeMe()._callback_exec_(return_more_than_one_value,callback_report_fibonacci,[i for i in range(0,1000,3)])
	for i in range(0,500,30): print i if i%2==0 else ""
	
	
if __name__ == "__main__":
	init()
