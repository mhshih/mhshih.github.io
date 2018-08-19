import csv

f=open('dict_sentences.txt',mode='w',encoding='utf8')

for line in csv.reader(open('extra_meaning_utf8.csv',encoding='utf8')):
    meaningid,itemname,meaningno,sentenceno,meaning,meaningEn,sentence,sentenceCh,sentenceEn,wordclass=line
    if sentence>'':f.write(sentence.strip('\n')+'\n')

for line in csv.reader(open('item_utf8.csv',encoding='utf8')):
    itemid,itemname,ucode,toda,truku,isroot,notsure,wordroot,focus,todar,trukur,hasbranch,wordclass,mainMeaningWordclass,meaning,meaningEn,sentence,sentenceCh,sentenceEn,idom,idomCh,idomEn,source,remark,culture,book,variant=line[:27]
    if sentence>'':f.write(sentence.strip('\n')+'\n')
      
f.close()
