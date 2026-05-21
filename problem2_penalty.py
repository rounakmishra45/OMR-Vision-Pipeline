/*a_fill=7
b_fill=9
c_fill=12
d_fill=7

marks_count= 0

if a_fill>75:
    marks_count += 1
if b_fill>75:
    marks_count += 1
if c_fill>75:
    marks_count += 1
if d_fill>75:
    marks_count += 1

if marks_count>1:
    print("invalid: double marked - 0 points")
elif marks_count==0:
    print("invalid: no marks - 0 points")
else:
    if a_fill>75:
        print("selected A")
    elif b_fill>75:
        print("selected B")
    elif c_fill>75:
        print("selected C")
    elif d_fill>75:
        print("selected D")