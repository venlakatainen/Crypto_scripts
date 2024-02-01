from itertools import combinations

# Help to solve plain text when knowing 10 ciphertexts encrypted with the stream cipher with the same nonce. 

def possible_combos(l):
    return list(combinations(l, 2))


# message to decimal

def message_to_dec (msg):
    message_as_dec = []
    for i in range(0,len(message1),2):
        message_as_dec.append(int(msg[i]+msg[i+1],16))

    return message_as_dec

def dec_to_char (list_dec):
    chars = ""
    for i in range(len(list_dec)):
        chars = chars + chr(list_dec[i])

    return chars

def plain_message_to_dec (msg):
    message_as_dec = []
    for i in range(0,len(msg)):
        message_as_dec.append(ord(msg[i]))

    return message_as_dec

# xor two cipher texts to get xor of plain texts
def xor_of_msgs (msg1, msg2):    
    xorred_plain = [] 
    for i in range(0,len(msg1)):
        xorred_plain.append(msg1[i]^msg2[i])

    return xorred_plain


# find combinations of characters that xorred together are same as plain texts xorred
def find_letter_combos (xor_plain):
    mes = {}

    for i in range(len(xor_plain)):
        tuples = []
        for j in range(len(combos)):
            if combos[j][0]^combos[j][1] == xor_plain[i]:
                tuples.append((chr(combos[j][0]),chr(combos[j][1])))
                
        mes[xor_plain[i]] = tuples

    return mes


# find letter combinations from dictionary where is only one combo 
def only_one_combo_found (combs,xorred):
    plain_1 = ["-"] * 50 

    plain_2 = ["-"] * 50

    for key in combs:
        if len(combs[key]) == 1:
            index = xorred.index(key)
            plain_1[index] = combs[key][0][0]
            plain_2[index] = combs[key][0][1]

    return plain_1, plain_2


message1 = "c893b56d652e0fadc4f945e99e0aef6f634880c27b68979b2329805fa3e34ecb209f11bebce48f9e46a9c741a1a5e21ea910"
message2 = "c495f03a77295da58ff259e7d916f326725389c3352c818b6d339a10acb34fcf25cb18f0b0ad88d640e1cd43eea8fc17f30b"
message3 = "c483b5736a2940ec8cf244a09b10fe2e7353cccf352c978c23258819ade1488238d050b5aba79a8646a9d045abe6ff04e502"
message4 = "8190fc74607d5ca08deb47e59d42ea3a694487ca222c828a712f9b18aab348ca299f17bcb9b788d647e6cb5fbde6e60ba911"
message5 = "c884e17576240fa185f544e9960ce86f744f83d33c64d68c6c34ce0eb7fa5fc920c650b5b6ab8e914ba9d042eeb6fb08ff02"
message6 = "cf93b57b242e58a596f717ef9f42fc3d695398df7b6883917760880dadfe1cc722cb15a2b1aa9cd642e5cb43a9e6fe04fd0f"
message7 = "818ffc7770354aec8cfa5bec8e03e26f734a89ca2f2c998423228116aef658822fde12b2b9a39ed642e7c00da1aaed4dfb06"
message8 = "c6c7f87b702e0fad90bb58ee9c42fe21640783c07b6582c262608d10aefc49d029db50a0b7b78f9351a9d042a1e6e50cfb00"
message9 = "c4c7f375767d46a280f458f2d906f23c704b8ddf7b64978623228b1aacb348c32fd415b4f8b094d657e1c10db9a7e501a90e"
message10 = "d5c7f17f74344cb881ff17f3900feb2379078dc87b69988d712d810ab1b35ac32fda50bdb7b69ed657e1c543eea7a900ec13"


possible_chars = "abcdefghijklmnopqrstuvwxyz"

#chars to dec
char_list = []
for i in range(0,len(possible_chars)):
    char_list.append(ord(possible_chars[i]))

# append space dec
char_list.append(ord(" "))


# all possible 2 length combinations of characters
combos = possible_combos(char_list)


mes1 = message_to_dec(message1)
mes2 = message_to_dec(message2)
mes3 = message_to_dec(message3)
mes4 = message_to_dec(message4)
mes5 = message_to_dec(message5)
mes6 = message_to_dec(message6)
mes7 = message_to_dec(message7)
mes8 = message_to_dec(message8)
mes9 = message_to_dec(message9)
mes10 = message_to_dec(message10)



xorred_cipher_message_1 = xor_of_msgs(mes1, mes2)
xorred_cipher_message_2 = xor_of_msgs(mes1, mes3)
xorred_cipher_message_3 = xor_of_msgs(mes1, mes4)
xorred_cipher_message_4 = xor_of_msgs(mes1, mes5)
xorred_cipher_message_5 = xor_of_msgs(mes1, mes6)
xorred_cipher_message_6 = xor_of_msgs(mes1, mes7)
xorred_cipher_message_7 = xor_of_msgs(mes1, mes8)
xorred_cipher_message_8 = xor_of_msgs(mes1, mes9)
xorred_cipher_message_9 = xor_of_msgs(mes1, mes10)


mes_dic_1 = find_letter_combos(xorred_cipher_message_1)
mes_dic_2 = find_letter_combos(xorred_cipher_message_2)
mes_dic_3 = find_letter_combos(xorred_cipher_message_3)
mes_dic_4 = find_letter_combos(xorred_cipher_message_4)
mes_dic_5 = find_letter_combos(xorred_cipher_message_5)
mes_dic_6 = find_letter_combos(xorred_cipher_message_6)
mes_dic_7 = find_letter_combos(xorred_cipher_message_7)
mes_dic_8 = find_letter_combos(xorred_cipher_message_8)
mes_dic_9 = find_letter_combos(xorred_cipher_message_9)


combs1, combs2 = only_one_combo_found(mes_dic_1, xorred_cipher_message_1)

combs3, combs4 = only_one_combo_found(mes_dic_2, xorred_cipher_message_2)

combs5, combs6 = only_one_combo_found(mes_dic_3, xorred_cipher_message_3)

combs7, combs8 = only_one_combo_found(mes_dic_4, xorred_cipher_message_4)

combs9, combs10 = only_one_combo_found(mes_dic_5, xorred_cipher_message_5)

combs11, combs12 = only_one_combo_found(mes_dic_6, xorred_cipher_message_6)

combs13, combs14 = only_one_combo_found(mes_dic_7, xorred_cipher_message_7)

combs15, combs16 = only_one_combo_found(mes_dic_8, xorred_cipher_message_8)

combs17, combs18 = only_one_combo_found(mes_dic_9, xorred_cipher_message_9)

            
print(combs1)
print(combs2)
print("\n")
print(combs3)
print(combs4)
print("\n")
print(combs5)
print(combs6)
print("\n")
print(combs7)
print(combs8)
print("\n")
print(combs9)
print(combs10)
print("\n")
print(combs11)
print(combs12)
print("\n")
print(combs13)
print(combs14)
print("\n")
print(combs15)
print(combs16)
print("\n")
print(combs17)
print(combs18)

# plain message 1 solved with previous lists

plain1 = "it was a bright cold day in april and the clocks w"
plain_1 = plain_message_to_dec(plain1)


# to found the rest of the messages -> xor the plain text one with the xor of the xorred cipher texts

plain2 = xor_of_msgs(xorred_cipher_message_1, plain_1)
plain3 = xor_of_msgs(xorred_cipher_message_2, plain_1)
plain4 = xor_of_msgs(xorred_cipher_message_3, plain_1)
plain5 = xor_of_msgs(xorred_cipher_message_4, plain_1)
plain6 = xor_of_msgs(xorred_cipher_message_5, plain_1)
plain7 = xor_of_msgs(xorred_cipher_message_6, plain_1)
plain8 = xor_of_msgs(xorred_cipher_message_7, plain_1)
plain9 = xor_of_msgs(xorred_cipher_message_8, plain_1)
plain10 = xor_of_msgs(xorred_cipher_message_9, plain_1)


plain2 = dec_to_char(plain2)
plain3 = dec_to_char(plain3)
plain4 = dec_to_char(plain4)
plain5 = dec_to_char(plain5)
plain6 = dec_to_char(plain6)
plain7 = dec_to_char(plain7)
plain8 = dec_to_char(plain8)
plain9 = dec_to_char(plain9)
plain10 = dec_to_char(plain10)

# print messages
print(plain1)
print(plain2)
print(plain3)
print(plain4)
print(plain5)
print(plain6)
print(plain7)
print(plain8)
print(plain9)
print(plain10)