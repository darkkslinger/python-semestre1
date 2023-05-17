print ("Ingrese su nombre y el de otra persona")
name=str(input())
name2=str(input())

if name[0]==name2[0]:
    print ("Ambos nombres empiezan por la misma letra")
elif name[-1]==name2[-1]:
    print ("Ambos nombres terminan por la misma letra")
else:
    print ("Ningun nombre de los ingresados inicia ni termina con la misma letra")