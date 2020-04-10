from django.http import HttpResponse
from django.template import loader
import mysql.connector
from .forms import NewUserForm

def index(request):

    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))


def database(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "pass",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    select dept_name as dept, min(salary) as Minimum_Salary from Instructor
group by dept_name;
"""
    cursor.execute(sql)


    template = loader.get_template("query_forum_min.html")
    context = {
        "show_id":False,
        "show_name":False,
        "show_dept":True,
        "show_salary":True,
        "data":cursor}
    return HttpResponse(template.render(context, request))
    
def database2(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "pass",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    select dept_name as dept, max(salary) as Maximum_Salary from Instructor
group by dept_name;
"""
    cursor.execute(sql)


    template = loader.get_template("query_forum_max.html")
    context = {
        "show_id":False,
        "show_name":False,
        "show_dept":True,
        "show_salary":True,
        "data":cursor}
    return HttpResponse(template.render(context, request))

def database3(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "pass",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    select dept_name as dept, avg(salary) as Average_Salary from Instructor
group by dept_name;
"""
    cursor.execute(sql)


    template = loader.get_template("query_forum_avg.html")
    context = {
        "show_id":False,
        "show_name":False,
        "show_dept":True,
        "show_salary":True,
        "data":cursor}
    return HttpResponse(template.render(context, request))
    
def database4(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "pass",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    select ID, name, dept_name as dept, salary from Instructor
order by name, dept, salary;
"""
    cursor.execute(sql)


    template = loader.get_template("query_forum_order_name.html")
    context = {
        "show_id":True,
        "show_name":True,
        "show_dept":True,
        "show_salary":True,
        "data":cursor}
    return HttpResponse(template.render(context, request))

def database5(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "pass",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    select ID, name, dept_name as dept, salary from Instructor
order by dept_name, name, salary;
"""
    cursor.execute(sql)


    template = loader.get_template("query_forum_order_dept.html")
    context = {
        "show_id":True,
        "show_name":True,
        "show_dept":True,
        "show_salary":True,
        "data":cursor}
    return HttpResponse(template.render(context, request))
    
def database6(request):

    mydb = mysql.connector.Connect(
        host = "localhost",
        user = "root",
        passwd = "pass",
        auth_plugin = "mysql_native_password",
        database = "university"
    )
    cursor = mydb.cursor(dictionary=True)

    sql = """
    select ID, name, dept_name as dept, salary from Instructor
order by salary, name, dept_name;
"""
    cursor.execute(sql)

    template = loader.get_template("query_forum_order_salary.html")
    context = {
        "show_id":True,
        "show_name":True,
        "show_dept":True,
        "show_salary":True,
        "data":cursor}
    return HttpResponse(template.render(context, request))
  


