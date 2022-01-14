# StringMatching

```python
from StringMatching.matcher import Sunday,Horspool

pattern='hello'
text='say hello to you!'

matcher=Sunday(pattern) #Horspool(pattern)
print(matcher.match(text)) #[4]

