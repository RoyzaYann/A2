# DO NOT EDIT

# Assignment for 15zy23

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (~R|(S|~P))
s2 = ((~P|R)&(~P|~R))
s3 = ((~P|S)&(~P|~S))
s4 = (R|(P|~S))

s5 = ((R>>T)>>((T&~R)|S))
s6 = ((~T>>(S&~R))|~(R|~T))
