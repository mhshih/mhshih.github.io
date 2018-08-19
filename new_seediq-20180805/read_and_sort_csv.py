import csv,sys

class Item:
    def __init__(self,csv_header,csv_line):
        for i in range(len(csv_header)):
            setattr(self,csv_header[i],csv_line[i])

def read_csv(csv_file='item_20180123_ANSI_線上編輯和預覽.tsv'):
    items=[]
    csv_reader=csv.reader(open(file=csv_file,mode='r',encoding='utf-8'),delimiter='\t')
    csv_lines=list(csv_reader)
    csv_header=csv_lines[0]
    for csv_line in csv_lines[1:]:
        items.append(Item(csv_header,csv_line))
    return sorted(csv_header),items

def search(items,query='zunsa',suffix=True):
    found_items=[]
    for item in items:
        if suffix==False:
            if query in item.itemname:#or itemname in item.wordroot:
                found_items.append(item)
        elif suffix==True:
            if item.itemname.endswith(query):#or itemname in item.wordroot:
                found_items.append(item)
    return found_items

def edit(items,key='yakang',**kwargs):  #key is unique for exact match; kwargs change columns to these values.
    outputs=[]
    for item in items:
        if item.itemname==key:
            item=Item(csv_header=list(vars(item).keys())+list(kwargs.keys()),csv_line=list(vars(item).values())+list(kwargs.values()))
        outputs.append(item)
    return outputs

def save_csv(items,csv_file,csv_header):	# To replace item in items, then write items into the csv database.
    f=open(file=csv_file,mode='w',encoding='utf-8')
    csv_writer=csv.writer(f,delimiter='\t')
    csv_writer.writerow(csv_header)
    for item in items:
        csv_writer.writerow([v for k,v in sorted(vars(item).items())])
    f.close()

def add(key_itemname,items,csv_header): # If existed:return None.
    for item in items:
        if key_itemname==item.itemname:
            print('Key_itemname existed:')
            print(sorted(vars(item)))
            return None
        elif key_itemname==item.variant:
            print('The following variant existed:')
            print(sorted(vars(item).items()))
            return None
    # If no existed:return updated items.
    item=Item(csv_header=csv_header+['itemname'],csv_line=[None]*len(csv_header)+[key_itemname])
    items.append(item)
    return items

if __name__=='__main__':
    csv_file=sys.argv[1]
    csv_header,items=read_csv(csv_file=csv_file)

    query='an'
    for found_item in search(items,query=query):
        print(sorted(vars(found_item).items()))

    '''
    key_itemname='anaq'
    variant='anaq'
    print('3. Search itemname="%s" before adding key_itemname="%s":' % (key_itemname,key_itemname))
    csv_header,items=read_csv(csv_file=csv_file)
    for found_item in search(items,query=key_itemname):
        print(sorted(vars(found_item).items()))
    add(key_itemname=key_itemname,items=items,csv_header=csv_header)
    '''

    '''

    itemname=wordroot='adis'
    print('4. Search wordroot="%s" before changing all itemnames with wordroot="%s":' % (itemname,wordroot))
    csv_header,items=read_csv(csv_file=csv_file)
    for found_item in search(items,query=itemname): print(sorted(vars(found_item).items()))
    #add(key_itemname=key_itemname,items=items,csv_header=csv_header)
    '''
