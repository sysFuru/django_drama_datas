from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from drama_datas.forms import DramaDataForm, CompanyForm, CastForm, ActorForm
from django.views.decorators.http import require_safe, require_http_methods

from drama_datas.models import DramaData, Company, Cast, Actor

import datetime

# Create your views here.
@require_safe
def top(request):
    drama_datas = DramaData.objects.order_by('year', 'title')
    #drama_datas = Cast.objects.filter(role=1)#.select_related('title')
    casts = Cast.objects.all()
    
    context = {"drama_datas": drama_datas, "casts": casts}
    return render(request, "drama_datas/top.html", context)
    #return HttpResponse(request, "drama_datas/top.html")

@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def drama_data_new(request):
    if request.method == 'POST':
        form = DramaDataForm(request.POST)
        if form.is_valid():
            drama_data = form.save(commit=False)
            drama_data.created_by = request.user
            drama_data.save()
            return redirect(drama_data_detail, drama_data_id=drama_data.pk)
    
    else:
        form = DramaDataForm()

    return render(request, "drama_datas/drama_data_new.html", {'form': form})

    # return HttpResponse('スニペットの登録')


@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def drama_data_edit(request, drama_data_id):
    drama_data = get_object_or_404(DramaData, pk=drama_data_id)
    if drama_data.created_by_id != request.user.id:
        return HttpResponseForbidden("このドラマデータの編集は許可されていません")

    if request.method == "POST":
        form = DramaDataForm(request.POST, instance=drama_data)
        if form.is_valid():
            form.save()
            return redirect('drama_data_detail', drama_data_id=drama_data_id)
    
    else:
        form = DramaDataForm(instance=drama_data)
    
    return render(request, 'drama_datas/drama_data_edit.html', {'form': form})
    # return HttpResponse('スニペットの編集')

@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def drama_data_delete(request, drama_data_id):
    drama_data = get_object_or_404(DramaData, pk=drama_data_id)
    drama_data.delete()
    return redirect('/')


def drama_data_detail(request, drama_data_id):
    drama_data = get_object_or_404(DramaData, pk=drama_data_id)
    casts = Cast.objects.filter(title=drama_data_id)
    return render(request, 'drama_datas/drama_data_detail.html', {'drama_data': drama_data, 'casts': casts})
    #return HttpResponse('スニペットの詳細閲覧')

@require_safe
def all_actors(request):
    actors = Actor.objects.order_by("birthday")
    #drama_datas = Cast.objects.filter(role=1)#.select_related('title')
    #print(actors)

    ages = []
    for actor in actors:
        if actor.birthday:
            #print(actor.birthday.year)
            ages.append(age(actor.birthday.year, actor.birthday.month, actor.birthday.day))
        else:
            ages.append("")

    ziplist = zip(actors, ages)
    context = {"ziplist": ziplist}
    #context = {"actors": actors, "ages":ages}
    return render(request, "drama_datas/all_actors.html", context)
    #return HttpResponse(request, "drama_datas/top.html")

@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def actor_new(request):
    page_name = "俳優登録"

    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            actor = form.save(commit=False)
            actor.created_by = request.user
            actor.save()

        return redirect('all_actors')
    else:
        form = ActorForm()

    return render(request, "drama_datas/form_new.html", {'page_name': page_name, 'form': form})


@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def actor_edit(request, actor_id):
    page_name = "俳優データ編集"
    actor = get_object_or_404(Actor, pk=actor_id)
    # if actor.created_by_id != request.user.id:
    #     return HttpResponseForbidden("この俳優データの編集は許可されていません")

    if request.method == "POST":
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('all_actors')
    
    else:
        form = ActorForm(instance=actor)
    
    return render(request, 'drama_datas/form_edit.html', {'page_name': page_name, 'form': form})

@require_safe
def all_companies(request):
    companies = Company.objects.all()
    #drama_datas = Cast.objects.filter(role=1)#.select_related('title')
    
    context = {"companies": companies}
    return render(request, "drama_datas/all_companies.html", context)
    #return HttpResponse(request, "drama_datas/top.html")

@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def company_new(request):
    page_name = "会社名登録"

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = request.user
            company.save()
            return redirect('company_detail', company_id=company.pk)
    
    else:
        form = CompanyForm()

    return render(request, "drama_datas/form_new.html", {'page_name': page_name, 'form': form})

@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def company_edit(request, company_id):
    page_name = "会社名編集"
    company = get_object_or_404(Company, pk=company_id)

    if company.created_by_id != request.user.id:
        return HttpResponseForbidden("このデータの編集は許可されていません")

    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_detail', company_id=company_id)
    
    else:
        form = CompanyForm(instance=company)
    
    return render(request, 'drama_datas/form_edit.html', {'form': form})
    # return HttpResponse('スニペットの編集')

def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'drama_datas/company_detail.html', {'company': company})


@login_required
@require_http_methods(["GET", "POST", "HEAD"])
def cast_new(request, drama_data_id):
    page_name = "キャスト登録"
    print(drama_data_id)
    drama_data = get_object_or_404(DramaData, pk=drama_data_id)

    if request.method == 'POST':
        form = CastForm(request.POST)
        if form.is_valid():
            cast = form.save(commit=False)
            cast.title = drama_data
            cast.created_by = request.user
            cast.save()
            return redirect('drama_data_detail', drama_data_id=drama_data_id)
    
    else:
        form = CastForm()

    return render(request, "drama_datas/form_new.html", {'page_name': page_name, 'form': form})


def age(year, month, day):
    today = datetime.date.today()
    birthday = datetime.date(year, month, day)
    return (int(today.strftime("%Y%m%d")) - int(birthday.strftime("%Y%m%d"))) // 10000