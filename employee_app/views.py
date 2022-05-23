from django.shortcuts import render,redirect
from employee.models import *
from employee.forms import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse



# To create employee
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        pos=request.POST.get('position')
        if form.is_valid():
            try:
                if pos =='Manager':
                    form.save()
                    return redirect("/manager_details")
                else:
                    form.save()
                    return HttpResponse('Employee added Successfully')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "addemp.html", {'form':form})

#adding manager Team
def manager_details(request):
    if request.method == "POST":

        form = TeamForm(request.POST)
        Team_val= request.POST.get('TEAM')
        empl = Employee.objects.latest('id_carte')
        team_instance = Team.objects.create(TEAM=Team_val,employe=empl)
        team_instance.save()
        return HttpResponse('Employee added Successfully')
    else:
        form = TeamForm()
    return render(request, "manager_details.html",{'form':form})

# To show employee details
def showemp(request):
    employees = Employee.objects.all()
    return render(request, "showemp.html", {'employees':employees})

#To show manager's team
def showteam(request):
    teams=Team.objects.all()
    return render(request, "showteam.html", {'teams':teams})

# To delete employee details
def deleteEmp(request, id_carte):
    employee = Employee.objects.get(id_carte=id_carte)
    employee.delete() 
    return redirect("/showemp")

#To update employee details
def update(request, id_carte):
  employee = Employee.objects.get(id_carte=id_carte)
  template = loader.get_template('update.html')
  context = {
    'employee': employee,
  }
  return HttpResponse(template.render(context, request))


def updateEmp(request, id_carte):
  first = request.POST['first']
  last = request.POST['last']
  birth_date = request.POST['birth_date']
  phone = request.POST['phone']
  email = request.POST['email']
  position = request.POST['position']
  hired_date = request.POST['hired_date']
  last = request.POST['last']
  employee = Employee.objects.get(id_carte=id_carte)
  employee.name = first
  employee.Surname = last
  employee.birth_date=birth_date
  employee.Phone=phone
  employee.Email=email
  employee.position=position
  employee.hired_on=hired_date
  employee.save()
  return redirect('/showemp')