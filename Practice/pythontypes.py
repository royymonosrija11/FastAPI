def add(fname :str | None,lname :str =None):
    if(fname!=None):
        return fname.capitalize() + " " + lname

name="Monosrija"
surname="Roy"
print(add(name,surname))