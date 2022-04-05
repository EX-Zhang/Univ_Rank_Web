from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

from pyecharts.charts import Pie
from pyecharts import options as opts

import goslate

from Univ.models import UnivRank

import mysql.connector as MySQL

# Create your views here.

def index(request):

    template = loader.get_template('Univ/index.html')

    data = get_Univ_Data(0,10)['data']

    context = {

        'univ_data' : data,
        
    }

    return HttpResponse(template.render(context,request))

def get_Univ_Data(start,end):

    result = UnivRank.objects.raw('select Univ_ID, Univ_Reign as Reign, count(Univ_ID) as Amount from univ_rank GROUP BY Univ_Reign ORDER BY Amount DESC')

    if min(start,end) < 0 or max(start,end) >= len(result):

        return {'statue': 'Invalid', 'data':{}}

    pie = Pie()

    data = []

    for cur in result[start:end]:

        data.append([cur.Reign,cur.Amount])

    pie.add("",data)

    pie.set_global_opts(title_opts=opts.TitleOpts(title="University Rank", subtitle="Reign and Amount"))

    return {'statue': 'Valid', 'data': pie.dump_options()} 

def requestData(request):

    if request.method == "GET":

        request_data = request.GET

        start = int(request_data.get('start',default='1')) - 1 

        end = int(request_data.get('end',default='10'))

        print(request_data.get('lang')) 

        if request_data.get('data_type') == 'table':

            return JsonResponse(generate_HTML_Table(start,end,request_data.get('lang')))

        elif request_data.get('data_type') == 'pie_chart':

            return JsonResponse(get_Univ_Data(start,end))


def generate_HTML_Table(start,end,lang):
 
    tabel_data = {'header': ["Rank", "Name", "Country/Reign", "Score"], 'data': []}
    
    result = UnivRank.objects.raw('select Univ_ID, Univ_Rank, Univ_Name, Univ_Reign, Univ_Score from univ_rank')

    if min(start,end) < 0 or max(start,end) >= len(result):

        start = 0

        end = 10

    for cur in result[start:end]:

        Name = cur.univ_name

        Reign = cur.univ_reign

        index = len(Name) - 1 

        while index >= 0 and Name[index] != ' ':

            index = index - 1

        if(lang == "zh-cn"):

            Name = Name[index+1:]

        else:

            Name = Name[0:index]

            gs = goslate.Goslate()
            
            #Reign = gs.translate(Reign,'en')

        tabel_data['data'].append([cur.univ_rank,Name,Reign,cur.univ_score])

    return {'statue': 'Valid', 'data': tabel_data}
