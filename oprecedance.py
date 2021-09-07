#We will talk about operator precedence
#The order of precedence is () > ** > *,/ > +,- 
print((5 + 4) * 10 / 2) #45.0

print(((5 + 4) * 10) / 2) #45.0

print((5 + 4) * (10 / 2)) #45.0

print(5 + (4 * 10) / 2) #25.0

print(5 + 4 * 10 // 2) #25
