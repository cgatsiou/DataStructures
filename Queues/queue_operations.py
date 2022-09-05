#User function Template for python3

class Solution:
    '''
    Function Arguments :
    		@param  : q (given list on which queue is implemented)
    		@param  : x (value to be used accordingly)
    		@return : None
    '''
    
    #Function to push an element in queue.
    def enqueue(self,q, x):
        # code here
        q.append(x)
    
    #Function to remove front element from queue.
    def dequeue(self,q):
        # code here
        q.pop(0)
    
    #Function to find the front element of queue.
    def front(self,q):
        # code here
        return q[0]
    
    #Function to find an element in the queue.
    def find(self,q, x):
        q_copy=q[:]
        while len(q_copy):
            if q_copy.pop() == x:
                return True
            
        return False
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(str,input().strip().split()))
        queue = [] # our queue to be implemented
        ob=Solution()
        i = 0 #current index
        while i < len(a):
            if a[i]=='i':
                ob.enqueue(queue,a[i+1])
                i+=1
            elif a[i] == 'f' :
                if(ob.find(queue,a[i+1])):
                    print("Yes")
                else:
                    print("No")
                i+=1
            elif a[i] == 'r' :
                (ob.dequeue(queue))
            else:
                print(ob.front(queue))
            i+=1
# } Driver Code Ends
