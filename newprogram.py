User_input="One person announce a war in his village."
User_input=User_input.split(" ")
bad_words=["Bomb","gun","bullet","attack","war","dirty","pistol"]
for word in User_input:
    for w in bad_words:
        if (word.lower()==w.lower()):
            print("bad word")
        
        
        
