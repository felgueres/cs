'''
7202025: interview at an ai lab 

You have samples in this form: 
- Sample(timestamp, ['a','b','c'])
- Sample(timestamp, ['a','b'])
 
Where the leftmost element is the outer element in the callstack.
Output the function start and end time in an Event class. 

Event(name: str, start: ts, end: ts)

If a function is still running don't yield the end token. 

'''

class Sample:
    def __init__(self, ts: float, funcs=list[str]):
        self.ts = ts
        self.funcs = funcs

class Event:
    def __init__(self, start: float , end: float, name: str):
        self.start = start 
        self.end = end 
        self.name = name

samples = [Sample(1, ["a","b","c"]), Sample(1.5, ["a","b"]) ]

"""
start 1 a
start 1 b
start 1 c
end   1.5 c
"""

print(samples)
