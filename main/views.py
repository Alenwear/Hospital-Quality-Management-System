from django.shortcuts import render, render_to_response
from .models import CheInfo, AgentInfo, AdmInfo
from .check import AddCheck
from django.http import HttpResponseRedirect
from django.utils import timezone


# Create your views here.

def check(request):
    if request.method == 'POST':
        form = AddCheck(request.POST)
        print(form)

        if form.is_valid():
            clean_form = form.cleaned_data
            clean_form['dt'] = timezone.now()
            print(clean_form)

            admErId = AdmInfo.objects.get(AdmInfo_id=clean_form['fk_CheInfo_admErId'])
            admEeId = AdmInfo.objects.get(AdmInfo_id=clean_form['fk_CheInfo_admEeId'])
            opId = AgentInfo.objects.get(AgentInfo_id=1)

            newcheck = CheInfo(fk_CheInfo_admErId=admErId,
                               fk_CheInfo_admEeId=admEeId,
                               fk_CheInfo_opId=opId,
                               dt=timezone.now(),
                               time=clean_form['time'],
                               type=clean_form['type'],
                               manageScore=clean_form['manageScore'],
                               personScore=clean_form['personScore'],
                               fee=clean_form['fee'],
                               reason=clean_form['reason'], )
            newcheck.save()
            return HttpResponseRedirect('success')
        else:
            print(form)
            print('数据不符合要求')
    else:
        form = AddCheck()
        # print(form)
    return render(request, 'main/check.html', {'form': form})
    # return render(request, 'main/check.html', {'form': form})


def success(request):
    return render(request, 'main/success.html')


def showchecks(request):
    checks = CheInfo.objects.order_by('-time')
    context = {'checks': checks}
    return render(request, 'main/showchecks.html', context)
