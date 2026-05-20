#sets are unorderd
# sets re unindexed
#there is no way to change item in set 
#set cannot contain duplicate values

S= { 1,2,3,44,7 ,4.5,2 , "abhishek"}

print(S, type(S))

# Methods of set

# method 1: [ .add ()]  

S.add(555)
print(S, type(S))

#method 2: [ .remove ]
S.remove(4.5)
print(S, type(S))

# method 3 :  [ .clear ]
# Method 4 : [ .pop ]
