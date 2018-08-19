#-*-coding:utf8-*-

#word_boundary=' '
sent_boundary=['.','。','!','！','?','？',';','；']#共8個)。

punctuations=''.join([  '，',   '。',   '？',   '！',   '：',   '；',   '（',   '）',   '「',   '』',
                        ',',    '.',    '?',    '!',    ':',    ';',    '(',    ')',    "'",    '"',    '“',    '”',   '~',    '/',    '-']) #共18個.
ENCODING='UTF-8-SIG'

#Build and print item and meaning dict:
Items=dict() #{itemname:Item}

#OUTPUTS:
SENT_NUM=WORD_NUM=OOV=0 #COVERAGE=(WORD_NUM-OOV)/WORD_NUM*100%

class Item:
    def __init__(self,wordroot,focus,wordclass,meaning,sentence,variant,modified=False):
        self.wordroot=wordroot
        self.focus=focus
        self.wordclass=wordclass
        self.meaning=meaning
        self.sentence=sentence
        self.variant=variant
        self.modified=modified

#Build item root dictionary.
from collections import defaultdict
import csv

def build_Items_dict(dict_item='item_utf8.csv'):
    Items=dict() #{itemname:Item}
    for line in csv.reader(open(dict_item,encoding='utf8')):
        itemid,itemname,ucode,toda,truku,isroot,notsure,wordroot,focus,todar,trukur,hasbranch,wordclass,mainMeaningWordclass,meaning,meaningEn,sentence,sentenceCh,sentenceEn,idom,idomCh,idomEn,source,remark,culture,book,variant=line[:27]
        itemname=itemname.lower()
        if itemname[-1].isdigit():
            Items[itemname.strip(' 1234567890')]=Item(wordroot,focus,wordclass,meaning,sentence,variant,modified=True)
        else:Items[itemname]=Item(wordroot,focus,wordclass,meaning,sentence,variant,modified=False)
#Add new entry (including root information) for every variant.
        for v in variant.split(';'):
            Items[v.strip()]=Item(wordroot,focus,wordclass,meaning,sentence,variant,modified=True)
    return Items

import re
def split_by_word_boundary(text):#,word_boundary):
    #Pre-process: to reserve only alphanumeric characters for Seediq words.
    return re.sub(pattern='[^a-zA-Z]',repl=' ',string=text,flags=re.ASCII).split()#word_boundary)

def split_by_sent_boundary(text,sent_boundary):
    for boundary in sent_boundary:
        text=text.replace(boundary,'.') #or consider repl=\n.
    return text.split('.')[:-1] #rm 1 element after final .

#Read text and accumulate item/root frequency.
from collections import defaultdict
from os import listdir
def read_dir_and_count_item_root_freq(Items,input_dir='seediq_corpus/'):
    global SENT_NUM,WORD_NUM,OOV
    
    word_freq=defaultdict(int) #{word:freq}
    root_freq=defaultdict(int) #{root:freq}

    for filename in listdir(input_dir):

        text=open(input_dir+filename,encoding=ENCODING).read()

        WORD_NUM+=len(split_by_word_boundary(text))#,word_boundary))

        SENT_NUM+=len(split_by_sent_boundary(text,sent_boundary))
                         
        for line in open(input_dir+filename,encoding='utf8'): #Python2
            for word in split_by_word_boundary(line):#,word_boundary):
                itemname=word.lower().strip(punctuations)
                if itemname!='':
                    word_freq[itemname]+=1
                    if itemname in Items: #If root info available, freq++.
                        root_freq[Items[itemname].wordroot]+=1
                    else:OOV+=1
                    
    print('WORD_NUM: %d words,' % WORD_NUM)
    print('SENT_NUM: %d sentences,' % SENT_NUM)
    print('COVERAGE:',(WORD_NUM-OOV)/WORD_NUM*100,'% .')

    #Output seediq_corpus item frequency as csv file.
    output_tsv=input_dir.strip('/')+'_word_freq_root_freq_focus_wordclass_variant_modified_UTF8.csv'
    f=open(output_tsv,'w',encoding='utf8')
    delimiter=','
    f.write(delimiter.join(['itemname','item_freq','wordroot','root_freq','focus','wordclass','variant','modified'])+'\n')
    for word,freq in word_freq.items():
        wordroot,focus,wordclass,variant,r_freq,modified='NoRoot','NoFocus','NoWordClass','NoVariant',0,False
        if word in Items: #If root info available, output root info and freq; if variants are available, also add one new entry (including root info) for each one variant.
            item=Items[word]
            wordroot,focus,wordclass,variant,modified=item.wordroot,item.focus,item.wordclass,item.variant,item.modified
            r_freq=root_freq[wordroot]
        f.write(delimiter.join([word,str(freq),wordroot,str(r_freq),focus,wordclass,variant,str(modified)])+'\n')
    f.close()



#Build and print item and meaning dict:
Items=build_Items_dict(dict_item='item_utf8.csv')

#Output word frequency.tsv according to the built Items...
read_dir_and_count_item_root_freq(Items,input_dir='seediq_corpus/')
input('Pree enter to continue.')
