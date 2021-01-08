string=str(input())
alpha=" "

for character in string:
    if character.isalnum()!=character.isspace():
            alpha+=character
            
            
print(alpha) 
