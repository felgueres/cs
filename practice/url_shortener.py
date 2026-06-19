"""
Build a url shortener

Requirements

Func (what)
- Ability to shorten a url
- Ability to access the original url

Non Func (how)
- ensure uniqueness for short codes 
- redirection should be <100ms
- reliable 99%
- scale to support 1B shortened urls and 100m dau


"""

DOMAIN = "mybitly.com"
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_encode(n:int):
    if n == 0:
        return "0"
    result = []
    while n > 0:
        n,remainder = divmod(n,62)
        result.append(ALPHABET[remainder])
    return "".join(reversed(result))

class Shortener():

    def __init__(self):
        """ In memory implementation of a url shortener"""
        self.links = {} 
        self.counter_id = 0

    def generate(self, url: str) -> str:
        # problem here is that we only have 16 ^ 6 unique combinations 
        self.counter_id +=1 
        cur_id = base62_encode(self.counter_id)
        s_url = f"{DOMAIN}/{cur_id}"
        self.links[s_url] = url 
        return s_url
    
    def retrieve(self, s_url:str) -> str:
        return self.links.get(s_url, None)

s = Shortener()

url_1 = "https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly" 
url_2 = "https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly1" 
url_3 = "https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly2"
url_4 = "https://www.hellointerview.com/learn/system-design/problem-breakdowns/bitly3" 

print(s.generate(url_1))
print(s.generate(url_2))
print(s.generate(url_3))
print(s.generate(url_4))
