letter = ''' Dear <|Name|>,
            you are selected!
            <|Date|> '''

print(letter.replace("<|Name|>","CodingStress").replace("<|Date|>","2027") )