from django.shortcuts import render,redirect
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
import datetime
# Create your views here.
def index(request):
    if request.method=="POST":
        expense = ExpenseForm(request.POST)
        if expense.is_valid():
            expense.save()

    #GET REQUEST
    expenses = Expense.objects.all()     
    total_expenses = expenses.aggregate(Sum("amount"))['amount__sum']   
    print(total_expenses)
    expense_form = ExpenseForm()

    #Logic to calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365)
    data = Expense.objects.filter(date__gt=last_year)
    yearly_sum = data.aggregate(Sum('amount'))['amount__sum']

    #Monthly sum
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))['amount__sum']

    #Weekly sum
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))['amount__sum']

    #Calculating daily sum
    daily_sums  = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
    print('daily sums',daily_sums)


    # Sums per category
    categorical_sums = Expense.objects.filter().values('category').annotate(sum=Sum('amount'))
    

    return render(request,'myapp/dark-modern-index.html',{'expense_form':expense_form,'expenses':expenses,'total_expenses':total_expenses,'yearly_sum':yearly_sum,'monthly_sum':monthly_sum,'weekly_sum':weekly_sum,'daily_sums':daily_sums,'categorical_sums':categorical_sums})


def edit(request,id):
    expense= Expense.objects.get(id=id)
    expense_form = ExpenseForm(instance=expense)
    if request.method=="POST":
        form = ExpenseForm(request.POST,instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'myapp/modern-edit.html',{'expense_form':expense_form})

def delete(request,id):
    if request.method=="POST":
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('index')