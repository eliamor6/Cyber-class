#1
def HexTOdec (str):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                   'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    try:
        dec = 0
        str = str.upper()
        length= len(str)-1
        for digit in str:
            dec += hex_dict[digit] * 16 ** length
            length -= 1
        return dec
    # i replaced it to return for the second exercise works the same with print
    except:
        print("invalid hex number")
#HexTOdec("a")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#2
def HexSum (str):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    sum = 0
    temp_str =""
    str = str.upper()
    for char in str:
        if(char in hex_dict):
            temp_str += char
        else:
            sum += HexTOdec(temp_str)
            temp_str = ""
    if (temp_str != ""):
        sum += HexTOdec(temp_str)
#HexSum("10g10fke")
#print("ABRAKADABRA")
#---------------------------------------------------------------------------------------------------------------------------
#3
sum=0
counter=0
list = []
try:
    while(0 == 0):
        num = int(input("enter a number:"))
        counter += 1
        sum += num
except:
    if(counter != 0):
        print("the average is:" , sum / counter)
    else:
        print("you didnt entered any valid number")