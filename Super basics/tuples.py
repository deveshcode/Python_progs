tupl = {"a","b","c","f","z"}
tupl[0] = "s"
for i in tupl:
    print(i)


# PS D:\ALL COURSES and TUTs\PYTHON ML COURSE\COde\Super basics> python .\tuples.py
# Traceback (most recent call last):
#   File ".\tuples.py", line 2, in <module>
#     tupl[0] = "s"
# TypeError: 'set' object does not support item assignment