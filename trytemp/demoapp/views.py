from django.shortcuts import render

import datetime
def accesstemp(request):
    showtime=datetime.datetime.now().strftime('%b')
    name='vinothsha'
    dic={'timenow':showtime,'person':name}
    return render(request,'demoapp/base.html',context=dic)



# Create your views here.
