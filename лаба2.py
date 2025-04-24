s=input ("Введите строку:")
t=input ("Введите подстроку:")
positions=[]
for i in range(len(s)-len(t)+1) :
    if s[i:i+len(t)]==t:
          positions.append (1+1)
print ("Позиции подстроки t в строке s:", *positions)


