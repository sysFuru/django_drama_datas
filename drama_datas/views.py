from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from drama_datas.forms import DramaDataForm, CompanyForm, CastForm
from django.views.decorators.http import require_safe, require_http_methods

from drama_datas.models import DramaData, Company, Cast

# Create your views here.
@require_safe
def top(request):
    drama_datas = DramaData.objects.all()
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