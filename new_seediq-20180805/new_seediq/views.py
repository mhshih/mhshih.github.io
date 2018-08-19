from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

def search_form(request):
    return render(request,'search_form.htm',{})

from read_and_sort_csv import read_csv
csv_file='item_20180123_ANSI_線上編輯和預覽.tsv'
csv_header,items=read_csv(csv_file=csv_file)

from read_and_sort_csv import search
def search_result(request):
    query=request.POST['query']
    suffix=False
    try:
        choice=request.POST['choice']
        if choice=='suffix':suffix=True
    except:pass

    res=[]
    for found_item in search(items,query=query,suffix=suffix):
        res.append(found_item.itemname)#sorted(vars(found_item).items()))
    return HttpResponse('<ol><li>'+'<li>'.join(res)+'</ol>')
