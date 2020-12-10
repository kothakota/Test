def app(*kids):

    c=0
    for _ in range(len(kids)):
     print("The youngest child is " + kids[c],"\n")
     c+=1

    while True:
        print("Naveen Kothakota",c)
        c+=1
        break

 
 
 

app("Emil", "Tobias", "Linus")