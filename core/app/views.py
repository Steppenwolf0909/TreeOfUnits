from django.shortcuts import render
from .models import Employee, Subdivision
from django.core.paginator import Paginator


def main(request, pk, page):
    parents = []
    parent = Subdivision.objects.get(id=pk)
    subdivision = parent
    childrens = Subdivision.objects.filter(parent_subdivision=parent)
    for i in range(5):
        parents.insert(0, parent)
        if parent.parent_subdivision is not None:
            parent = Subdivision.objects.filter(id=parent.parent_subdivision.id).first()
        else:
            break
    employees  = Employee.objects.filter(subdivision__id=pk)
    p = Paginator(employees, 30)
    context = {
        "childrens": childrens,
        "parents": parents,
        "subdivision": subdivision,
        "employees": p.page(page)
    }
    return render(request, 'main.html', context=context)


def get_childrens(request, pk):
    parents = []
    parent = Subdivision.objects.get(id=pk)
    childrens = Subdivision.objects.filter(parent_subdivision=parent)
    for i in range(5):
        if parent.parent_subdivision is not None:
            parent = Subdivision.objects.filter(id=parent.parent_subdivision.id).first()
            parents.insert(0, parent)
        else:
            break
    context = {
        "childrens": childrens,
        "parents": parents
    }
    return render(request, 'main.html', context=context)