s = "qA2"
print(any(s.isalnum() for s in s))
print(any(s.isalpha() for s in s))
print(any(s.isnumeric() for s in s))
print(any(s.islower() for s in s))
print(any(s.isupper() for s in s))
