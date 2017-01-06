
class Stack:
     def __init__(self):
        self.items = []

     def isEmpty(self):
        return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Sintactico:

    #TS = { # (Regla, NToken): (Consecuente de la Regla, NRegla)

    def __init__(self, p_lexic, p_symTable):
        self.lexic = p_lexic
        # self.semantic = p_semantic // Semantico en un futuro
        self.symTable = p_symTable
    #INICIALIZAR PILA Y CADENA
        self.pila.push("$") 
        self.pila.push("A") 
        a=AL.get_token()
        X="A"
        while(X!="$")
            X=sel.pila.pop() 
            if X in Term:
                #PR
                if (X=="true" && a[0]==19 && a[1]==0):        
                    a=AL.get_token()
                elif (X=="false" && a[0]==19 && a[1]==1):
                    a=AL.get_token()
                elif (X=="if" && a[0]==19 && a[1]==2):
                    a=AL.get_token()
                elif (X=="while" && a[0]==19 && a[1]==3):
                    a=AL.get_token()
                elif (X=="var" && a[0]==19 && a[1]==4):
                    a=AL.get_token()
                elif (X=="bool" && a[0]==19 && a[1]==5):
                    a=AL.get_token()
                elif (X=="char" && a[0]==19 && a[1]==6):
                    a=AL.get_token()
                elif (X=="int" && a[0]==19 && a[1]==7):
                    a=AL.get_token()
                elif (X=="function" && a[0]==19 && a[1]==8):
                    a=AL.get_token()
                elif (X=="prompt" && a[0]==19 && a[1]==9):
                    a=AL.get_token()
                elif (X=="write" && a[0]==19 && a[1]==10):
                    a=AL.get_token()
                elif (X=="return" && a[0]==19 && a[1]==11):
                    a=AL.get_token()
                #Resto
                elif (X=="numero" && a[0]==14):
                    a=AL.get_token()
                elif (X=="cadena" && a[0]==15):
                    a=AL.get_token()
                elif (X=="id" && a[0]==18):
                    a=AL.get_token()
                elif (X=="eof" && a[0]==1):
                    a=AL.get_token()
                elif (X=="cr" && a[0]==2):
                    a=AL.get_token()
                elif (X=="," && a[0]==3):
                    a=AL.get_token()
                elif (X==";" && a[0]==4):
                    a=AL.get_token()
                elif (X=="-" && a[0]==5):
                    a=AL.get_token()
                elif (X=="(" && a[0]==6):
                    a=AL.get_token()
                elif (X==")" && a[0]==7):
                    a=AL.get_token()
                elif (X=="==" && a[0]==8):
                    a=AL.get_token()
                elif (X=="=" && a[0]==9):
                    a=AL.get_token()
                elif (X=="!=" && a[0]==10):
                    a=AL.get_token()
                elif (X=="||" && a[0]==11):
                    a=AL.get_token()
                elif (X=="+=" && a[0]==12):
                    a=AL.get_token()
                elif (X=="+" && a[0]==13):
                    a=AL.get_token()
                elif (X=="{" && a[0]==16):
                    a=AL.get_token()
                elif (X=="}" && a[0]==17):
                    a=AL.get_token()
                else:
                      # TODO: Tratar Error
                      continue
            else:
                # ya se hace un X=self.pila.pop() arriba
                var = M.has_key([X,a[0]])
                if var is True:                
                    for elem in M[X,a[0]]: #for elem in range(len(M)):
                        stack.push(elem)
        #cuando termina el while
        if a is  "$":
            return
#M (NoTerminal,Terminal,valor):(Token ordenado alrevés)
    M = { 
        ("A",2 ,) : ("A", "cr"),#2:cr
        ("A",1 ,) : ("eof") ,#eof
        ("A",18,): ("A", "cr", "B"),#18:id
        ("A",19, 2): ("A", "cr", "B"),#19:PR, 2:if
        ("A",19, 3): ("A", "cr", "B"),#19:PR, 3:while
        ("A",19, 4): ("A", "cr", "B"),#19:PR, 4:var
        ("A",19, 8): ("A", "cr", "C"),#19:PR, 8:function
        ("A",19, 9): ("A", "cr", "B"),#19:PR, 9:prompt
        ("A",19, 10): ("A", "cr", "B"),#19:PR, 10:write
        ("A",19, 11): ("A", "cr", "B"),#19:PR, 11:return

        ("B",18,): ("D"),#18:id 
        ("B",19, 2): ("D", ")", "i", "(", "if"),#19:PR, 2:if
        ("B",19, 3): ("c", "E", "B", "E", "o", "E", ")", "L", "(", "while"),#19:PR, 3:while
        ("B",19, 4): ("id", "T", "var"),#19:PR, 4:var
        ("B",19, 9): ("D"),#19:PR, 9:prompt
        ("B",19, 10): ("D"),#19:PR, 10:write
        ("B",19, 11): ("D"),#19:PR, 11:return

        ("C",19, 8): ("c", "E", "B", "E", "o", "E", ")", "N", "(", "id" "T"),#19:PR, 8:function

        ("D",18,): ("G", "id"),#18:id
        ("D",19, 9): (")", "id", "(", "prompt"),#19:PR, 9:prompt
        ("D",19, 10): (")", "I", "(", "write"),#19:PR, 10:write
        ("D",19, 11): ("L", "return"),#19:PR, 11:return                 
        ("D",19, 11): ("L", "return"),#19:PR, 11:return     

        ("E",2,): ("E", "cr"),#2:cr
        ("E",16,): ("lambda"),#16:abrir llave           
        ("E",17,): ("lambda"),#17:cerrar llave
        ("E",18,): ("lambda"),#18:id
        ("E",19,): ("lambda"),#19:PR
        ("E",19, 3): ("lambda"),#19:PR, 3:while
        ("E",19, 4): ("lambda"),#19:PR, 4:var
        ("E",19, 9): ("lambda"),#19:PR, 9:prompt
        ("E",19, 10): ("lambda"),#19:PR, 10:write
        ("E",19, 11): ("lambda"),#19:PR, 11:return

        ("G",6,): (")", "LL", "("),#abrir parentesis
        ("G",9,): ("I","="),#9:igual 

        ("I",19,0):("IP", "II"),      
        ("I",19,1):("IP", "II"),
        ("I",15, ):("IP", "II"),
        ("I",18, ):("IP", "II"), 
        ("I",14, ):("IP", "II"),

        ("II",19,0):("IIP", "III"),      
        ("II",19,1):("IIP", "III"),
        ("II",15, ):("IIP", "III"),
        ("II",18, ):("IIP", "III"), 
        ("II",14, ):("IIP", "III"),
        ("III",19,0):("IIIP","IV"),      
        ("III",19,1):("IIIP","IV"),
        ("III",15, ):("IIIP","IV"),
        ("III",18, ):("IIIP","IV"), 
        ("III",14, ):("IIIP","IV"),

        ("IIIP",7):("lambda"),
        ("IIIP",3):("lambda"),
        ("IIIP",17):("lambda"),
        ("IIIP",2):("lambda"),
        ("IIIP",10):("lambda"),
        ("IIIP",8):("lambda"),
        ("IIIP",11):("IIIP", "IV", "or"),
        
        ("IIP",7):("lambda"),
        ("IIP",3):("lambda"),
        ("IIP",17):("lambda"),
        ("IIP",2):("lambda"),
        ("IIP",10):("desigual","III","IP"),
        ("IIP",8):("lambda"),        

        ("IP",7):("lambda"),
        ("IP",3):("lambda"),
        ("IP",17):("lambda"),
        ("IP",2):("lambda"),        
        ("IP",8):("IP", "II", "dobleigual"),

        ("IV",19,0):("IVP", "V"),
        ("IV",19,1):("IVP", "V"),
        ("IV",15, ):("IVP", "V"),
        ("IV",18, ):("IVP", "V"),
        ("IV",14, ):("IVP", "V"),

        ("IVP",7,):("lambda"),
        ("IVP",13,):("IVP", "V", "+"),
        ("IVP",3,):("lambda"),
        ("IVP",17,):("lambda"),
        ("IVP",2,):("lambda"),
        ("IVP",10,):("lambda"),
        ("IVP",8,):("lambda"),
        ("IVP",11,):("lambda"),   

        ("L",7, ):("lambda"),
        ("L",19,0):("I"),      
        ("L",19,1):("I"),
        ("L",17, ):("lambda"),
        ("L",15, ):("I"),
        ("L",2, ):("lambda"),
        ("L",18, ):("I"),
        ("L",14, ):("I"),

        ("LL",7, ):("lambda"),
        ("LL",19,0):("Q","I"),
        ("LL",19,1):("Q","I"),
        ("LL",15, ):("Q","I"),
        ("LL",18, ):("Q","I"),
        ("LL",14, ):("Q","I"),


        ("N",7, ):("lambda"),      
        ("N",19,5 ):("NN", "id", "TT"),
        ("N",19,6 ):("NN", "id", "TT"),
        ("N",19,7 ):("NN", "id", "TT"),


        ("NN",7, ):("lambda"),
        ("NN",3, ):("NN", "id", "TT", ","),

        ("Q",7, ):("lambda"),      
        ("Q",3, ):("Q", "I", ","),

        ("T",18,):("lambda"),
        ("T",19,5 ):("bool"),
        ("T",19,6 ):("chars"),
        ("T",19,7 ):("int"),

        ("U",6, ):(")","LL","("),      
        ("U",7, ):("lambda"),
        ("U",13, ):("lambda"),
        ("U",3, ):("lambda"),
        ("U",5, ):("lambda"),
        ("U",17, ):("lambda"),      
        ("U",2, ):("lambda"),
        ("U",10, ):("lambda"),
        ("U",8, ):("lambda"),
        ("U",11, ):("lambda"),

        ("V",19,0):("VP", "VI"),      
        ("V",19,1):("VP", "VI"),
        ("V",15, ):("VP", "VI"),
        ("V",18, ):("VP", "VI"),
        ("V",14, ):("VP", "VI"),
        
        ("VI",19,0):("booleano"),
        ("VI",19,1):("booleano"),
        ("VI",15, ):("cadena"),
        ("VI",18, ):("id"),
        ("VI",14, ):("numero"),

        ("VP",7):("lambda"),
        ("VP",13):("lambda"),
        ("VP",3):("lambda"),
        ("VP",5):("VP","VI"),
        ("VP",17):("lambda"),
        ("VP",2):("lambda"),
        ("VP",10):("lambda"),
        ("VP",8):("lambda"),
        ("VP",11, ):("lambda")#or
    }
    




    
