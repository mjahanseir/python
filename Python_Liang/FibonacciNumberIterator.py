class FibonacciIterator:
    def __init__(self):
        self.fn1 = 0 # Current two consecutive fibonacci numbers
        self.fn2 = 1 
    
    def __next__(self): # Define the next method
        current = self.fn1
        self.fn1, self.fn2 = self.fn2, self.fn1 + self.fn2       
        return current

    def __iter__(self):
        return self
    
def main():
    iterator = FibonacciIterator()
    # Display all Fibonacci numbers <= 10000
    for i in iterator:
        if i <= 10000: 
             print(i, end = ' ')
        else: break

main()
