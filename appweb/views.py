from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from datetime import datetime
from .models import Course
from .forms import CourseForm

# Views ini terinspirasi dari Tugas Kelompok saya

def create(request):
    matkul_form = CourseForm()
    if request.method == "POST":
        matkul_form = CourseForm(request.POST)
        if matkul_form.is_valid():
            matkul_form.save()
            return redirect('appweb:list')
      
    context = {
        'matkul_form'   : matkul_form,
        'title'         : "Tambah Matkul"
        }
    return render(request, 'appweb/matkul_create.html', context)

def update(request,update_id):
	matkul_update = Course.objects.get(id=update_id)
	
	data_matkul = {
		'nama'	    : matkul_update.nama,
		'dosen'	    : matkul_update.dosen,
		'sks'	    : matkul_update.sks,
        'semester'  : matkul_update.semester,
        'tahun'     : matkul_update.tahun,
        'ruang'     : matkul_update.ruang,
        'deskripsi' : matkul_update.deskripsi,
	}
	matkul_form = CourseForm(request.POST or None, initial=data_matkul, instance=matkul_update)

	if request.method == 'POST':
		if matkul_form.is_valid():
			matkul_form.save()

		return redirect('appweb:list')

	context = {
		"title":"Update Matkul",
		"matkul_form":matkul_form,
	}

	return render(request,'appweb/matkul_update.html',context)


def list(request):
    all_matkul = Course.objects.all()

    context = {
        'title' : 'List Matkul',
        'all_matkul' : all_matkul
    }
    return render(request, 'appweb/matkul_list.html', context)


def delete(request, delete_id):
    Course.objects.filter(id=delete_id).delete()
    return redirect('appweb:list')


def detail(request, detail_id):
    matkul_detail = Course.objects.get(id=detail_id)

    context = {
        "title" : "Detail Matkul",
        "matkul_detail": matkul_detail,
    }
    return render(request, "appweb/matkul_detail.html", context)

