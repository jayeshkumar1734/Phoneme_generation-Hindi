import math
import re
vowels=["ा","ि","ी","ु","ू","ृ","े","ै","ो","ौ","ँ",'ं','ॆ',"ː","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ","औ","अः","अं"]
full_consonants=["क","ख","ग","घ","ङ","च","छ","ज","झ","ञ","ट","ठ","ड","ढ","ण","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","ळ","व","श","ष","स","ह"]
special_vowels=["ः","ं","ँ"]
mapping={}
mapping["अ"]="ə"
mapping["आ"]="a:"
mapping["इ"]="ɪ"
mapping["ई"]="i:"
mapping["उ"]="ʊ"
mapping["ऊ"]="u:"
mapping["ऋ"]="ɻ̩"
mapping["ए"]="e:"
mapping["ऐ"]="ɛ:"
mapping["ओ"]="o:"
mapping["औ"]="ɔ:"
#mapping["अँ"]="/ə̃/"
#mapping["अः"]="/əɦə/"
mapping["अं"]="əm"
#mapping["ऑ"]="/ɒ/"


mapping["ा"]="a:"
mapping["ि"]="ɪ"
mapping["ी"]="i:"
mapping["ु"]="ʊ"
mapping["ू"]="u:"
mapping["ृ"]="ɻ̩"
mapping["े"]="e:"
mapping["ै"]="ɛ:"
mapping["ो"]="o:"
mapping["ौ"]="ɔ:"
#mapping["ँ"]="/ə̃/"
#mapping["ː"]="/əɦə/"
mapping['ं']="əm"
mapping["ॆ"]="e:"

mapping["क"+"्"]="k"
mapping["ख"+"्"]="kʰ"
mapping["ग"+"्"]="g"
mapping["घ"+"्"]="gʰ"
mapping["ङ"+"्"]="ŋ"
mapping["च"+"्"]="tʃ"
mapping["छ"+"्"]="tʃʰ"
mapping["ज"+"्"]="dʒ"
mapping["झ"+"्"]="dʒʰ"
mapping["ञ"+"्"]="ɲ"
mapping["ट"+"्"]="ʈ"
mapping["ठ"+"्"]="ʈʰ"
mapping["ड"+"्"]="ɖ"
mapping["ढ"+"्"]="ɖʰ"
mapping["ण"+"्"]="ɳ"
mapping["त"+"्"]="t̪"
mapping["थ"+"्"]="t̪ʰ"
mapping["द"+"्"]="d̪"
mapping["ध"+"्"]="d̪ʰ"
mapping["न"+"्"]="n"
mapping["प"+"्"]="p"
mapping["फ"+"्"]="pʰ"
mapping["ब"+"्"]="b"
mapping["भ"+"्"]="bʰ"
mapping["म"+"्"]="m"
mapping["य"+"्"]="j"
mapping["र"+"्"]="ɾ"
mapping["ल"+"्"]="l"
mapping["व"+"्"]="ʋ"
mapping["स"+"्"]="s"
mapping["श"+"्"]="ʃ"
mapping["ष"+"्"]="ʂ"
mapping["ह"+"्"]="ɦ"
mapping["ळ"+"्"]="ɭ̆ɭ̆"
mapping[" "]="SIL"

# for t in range(2):
#     file_name="./text_"+str(t)+".txt"
#     file1=open(file_name,"r")
#     #file1=open("./text.txt","r")
text="नमस्कार नमस्कार नमस्कार \n नमस्कार नमस्कार"
line=text.split("\n")
for i in range(len(line)):
  line[i]=line[i].strip()
print(line)
b=[]

for k in range(len(line)):
  x=str(b)+str("_")+str(k)
  x=[]
  a=line[k]
  a_1=re.split(" ",a)
  #print(a_1)
  
  for i in range(len(a_1)):
    for j in range(len(a_1[i])):
    
      #print(a_1[i])
      x.append(a_1[i][j])
    x.append("  ")
  b.append(x)

for i in range(len(b)):
  for j in range(len(b[i])):
    if b[i][j]=="अ" and b[i][j+1] in special_vowels:
      b[i][j]="अ"+b[i][j+1]
      b[i][j+1]="."
  if "." in b[i]:
    b[i].remove(".")

for i in range(len(b)):
  for j in range(len(b[i])):
    if b[i][j]=="्":
      #print(b[i-1],i)
      b[i][j-1]=b[i][j-1]+b[i][j]
      b[i][j]=""

for i in range(len(b)):
  for j in range(3*len(b[i])):
    if j < len(b[i]):
      if b[i][j] in full_consonants and b[i][j+1] not in vowels:
        b[i][j]=b[i][j]+"्"
        b[i].insert(j+1,"अ")

  if b[i][len(b[i])-2] in full_consonants:
    b[i][len(b[i])-2]=b[i][len(b[i])-2]+"्"
    b[i].insert(len(b[i])-1,"अ")

c=[]
indices=[]
for i in range(len(b)):
  y=str(c)+str("_")+str(i)
  y=[]
  for j in range(len(b[i])):
    if b[i][j]!="":
      y.append(b[i][j])
  c.append(y)


for k in range(len(c)):
  for i in range(1,len(c[k])):
    if c[k][i] in vowels and c[k][i-1] not in vowels:
      c[k][i-1]=c[k][i-1]+"्"

phones=[]

for i in range(len(c)):
  z=str(phones)+str("_")+str(i)
  z=[]
  values=''
  for char in c[i]:  
    if char=='  ':
      z.append(values)
      values=''
      
    else:
      for key,value in mapping.items():
        if char == key:
          values=values+value+" "
    
    
  phones.append(z)

phones_final=[]
for i in range(len(phones)):
  z=str(phones_final)+str("_")+str(i)
  z=[]
  for j in range(len(phones[i])):
    if len(phones[i][j])==0:
      break
    else:
      z.append(phones[i][j])
  
  phones_final.append(z)
for j in range(len(phones_final)):
  for i in range(1,5*len(phones_final[j]),2):
    if i<len(phones_final[j]):
      phones_final[j].insert(i,"SIL")
print(phones_final)
# phonemes=[]
# for i in range(len(phones_final[0])):
#   for j in range(len(phones_final[0][i])):
#     phonemes.append(phones_final[0][i][j].split(" "))
phonemes=[]
temp_pho=[]
for j in range(len(phones_final)):
  a=[]
  for i in range(len(phones_final[j])):
    a.append(phones_final[j][i])
  temp_pho.append(a)
print(temp_pho)
for j in range(len(temp_pho)):
  x=[]
  for i in range(len(temp_pho[j])):
    temp_pho[j][i]=temp_pho[j][i].strip()
    x.append(temp_pho[j][i].split(" "))
  phonemes.append(x)
print(phonemes)
phonemes_final=[]
for i in range(len(phonemes)):
  y=[]
  for j in range(len(phonemes[i])):
    for k in range(len(phonemes[i][j])):
      y.append(phonemes[i][j][k])
  phonemes_final.append(y)
print(phonemes_final)

# temp_1=[]
# for i in range(len(phonemes_final)):
#   for j in range(len(phonemes[i])):
#     temp_1.append(phonemes[i][j])
# vocab = set(phonemes_final)
vocab=[]
for key,values in mapping.items():
  vocab.append(values)
word_to_ix = {word: i+1 for i, word in enumerate(vocab)}

word_to_ix

phonemes_num=[]
for j in range(len(phonemes_final)):
  a=[]
  for i in range(len(phonemes_final[j])):
    # print([word_to_ix[w] for w in phonemes_final[i]])
    a.append(word_to_ix[phonemes_final[j][i]])
  phonemes_num.append(a)

print(phonemes_num)

