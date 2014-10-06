from threading import Thread
from Queue import Queue

## AsynchronizeMe ##
class AsynchronizeMe(object):
	async_queue = Queue() ## Synchronized queue, it's not necessary to implement a monitor to protect concurrent acces to it ##
	
	@staticmethod
	## Call _callback_exec_ to execute asynchronously a function $func, with a callback $callback, *args are $func params ##
	def _callback_exec_(func,callback,*args):
		## Thread to run concurrent wrapper ##
		try: Thread(target=AsynchronizeMe()._callback_wrapper_,args=(func,callback,args)).start()
		except Exception: print "[X] Error running thread with func: " + func.__name__ + " , args: " + str(args) + ", callback: " + callback.__name__; exit(0)
		
	@staticmethod
	def _callback_wrapper_(func,callback,*args):
		try:
			## Run func concurrently ##
			async_func = Thread(target=func,args=(args[0][0]))
			async_func.start()
			## The thread waits for results in async_queue ##
			async_func.join()
			## Run concurrently callback for not to wait if the callback uses E/S ## 
			Thread(target=AsynchronizeMe()._async_callback_,args=((callback,))).start()
		except Exception as e: raise e
	    
	@staticmethod
	def _async_callback_(callback):
		## Executes callback with args = [results] of $func asynchronized ##
		try: callback(AsynchronizeMe().async_queue.get())
		except Exception as e: raise e
