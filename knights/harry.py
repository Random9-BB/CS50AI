from logic import *

Q = Symbol("Q")
P = Symbol("P")
sentence = Not(And(Q, P))



print(sentence.formula())