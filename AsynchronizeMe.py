import threading
import Queue

## AsynchronizeMe ##
class AsynchronizeMe(object):
	async_queue = Queue.Queue()
	
	@staticmethod
	def _callback_exec_(func,callback,*args):
		async_wrapper = threading.Thread(target=AsynchronizeMe()._callback_wrapper_,args=(func,callback,args))
		async_wrapper.start()
		
	@staticmethod
	def _callback_wrapper_(func,callback,*args):
		async_func = threading.Thread(target=func,args=(args[0][0]))
		async_func.start()
		async_func.join()
		async_callback = threading.Thread(target=AsynchronizeMe()._async_callback_,args=((callback,)))
		async_callback.start()
	    
	@staticmethod
	def _async_callback_(callback):
		callback(AsynchronizeMe().async_queue.get())


## Function Test ##
def fibonacci(*args):
	fib = [1,1]
	for i in xrange(2,args[0]): fib.append(fib[i-1]+fib[i-2])
	AsynchronizeMe().async_queue.put(fib[args[0]-1])

## Callback Test ##
def callback_report(x):
	print "\n"+str(x)+"\n"

## Main programme ##
def init():
	print "pppp\n"
	AsynchronizeMe()._callback_exec_(fibonacci,callback_report,[2000])
	print "xxxx\n"
	AsynchronizeMe()._callback_exec_(fibonacci,callback_report,[1800])
	print "tttt\n"
	fibonacci(200)
	print "\n"+str(AsynchronizeMe().async_queue.get())+"\n"
	
if __name__ == "__main__":
	init()
