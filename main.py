"""
Дана строка 'Break an Continue operators '
Выведите на экран данную строку до символа 'p' включительно, пропуская при этом каждый третий символ.
"""
s= 'Break and continue operators'

for i in range (0, len(s)):
    if s[i] == 'p':
        if (i+1)%3!=0:
            print(s[i], end='')
        break
    if i >0 and (i+1)%3==0:
        continue
    print(s[i], end='')

