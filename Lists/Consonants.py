str1 = "My name is Arpit Mallick"
def consonants(letter):
    vowel = "aeiou"
    return letter.isalpha() and letter.lower() not in vowel
conso = [i for i in str1 if consonants(i)]
# print(conso)

n = [10,2,98,-34,-56,-21,-89,765,8910]
def number(no):
    return no if no > 0 else 'negative number'
new_list = [number(i) for i in n]
print(new_list)