# def inverter_string (s):
#     inverter = ""
#     for i in s:
#         inverter = i + inverter
#     print(inverter)      
        
# inverter_string ("Raphaela")

#OUTRO JEITO

def inverter_string (s):
    inverter = ""
    for i in range(len(s) -1, -1, -1):
        inverter += s[i]
    print(inverter)      
        
inverter_string ("Raphaela")


    