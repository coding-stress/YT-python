marks = {
    "suraj" : 90,
    "abhishek" : 80,
    "budhiya" : 100,

}

#method 1: [a.items()] returns a list of (key, value)tuple.

print(marks.items())

# method 2 : [a.keys()] and [a.values()]  Returns a list containig dictionary's keys.

print(marks.keys())
print(marks.values())

# method 3: [a.update()] used to update dictionary

marks.update({"abhishek":30, "ironman" : 40}) 
print (marks)


# Method 4: [ a.get("name") ] returns the value of the specified keys  (and value is returned  eg: "stressmindra" is returned here).

print (marks.get("abhishek2")) #this give none 

print (marks["abhishek2"]) #this give error

# if keys are not availabel in the dictionary the mark.get gives us none but 2nd one is gives us error.

#after lecture pop method and pop item