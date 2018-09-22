from bs4 import BeautifulSoup
from getpass import getpass
import requests
import mechanize
import csv

# command to run : python -W ignore crawler.py

user = raw_input("Username : ")
pwd = getpass("Password : ")
destination = "./SPOJ_Codes"

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.13) Gecko/20101206 Ubuntu/10.10 (maverick) Firefox/3.6.13")]
base = "http://www.spoj.com/"

sign_in = br.open(base+"login")
br.select_form(nr = 0) #accessing form by their index. Since we have only one form in this example, nr =0.
br["login_user"]=user
br["password"]=pwd
log_in = br.submit()
login_check = log_in.read()
# print login_check
br.open(base+"myaccount")
soup = BeautifulSoup(br.response().read())

questions = []

for link in soup.find_all('a'):
    #if len(link.contents) > 0:
    #    print link.contents[0]
    url = link["href"]
    if "/," not in url and ","+user in url:
        questions.append(base+url)

answers = []
information = []

general = [];
general.append("Problem")
general.append("Solution ID")
general.append("Date of Submission")
general.append("Status if Submission")
general.append("Time of Execution")
general.append("Memory Required")
general.append("Language Used")
general.append("Problem Link")
information.append(general)

for link in questions:
    br.open(link)
    soup = BeautifulSoup(br.response().read())
    my_info = []
    status = soup.find("td", class_="statusres")
    if status is not None:
        status = status.strong
    if status is not None:
        status = status.contents
    if status is not None and len(status) > 0:
        status = status[0]
    id = soup.find("a", class_="sourcelink")
    if id is not None:
        id = id.contents
    if id is not None and len(id) > 0:
        id = id[0][3:]
    date = soup.find("td", class_="status_sm")
    if date is not None:
        date = date.span
    if date is not None:
        date = date.contents
    if date is not None and len(date) > 0:
        date = date[0]
    name = soup.find("td",class_="sproblem")
    if name is not None:
        name = name.a
    reference = base+name["href"]
    if name is not None:
        name = name.contents
    if name is not None and len(name) > 0:
        name = name[0]
    time = soup.find("td", class_="stime")
    if time is not None:
        time = time.a
    if time is not None:
        time = time.contents
    if time is not None and len(time) > 0:
        time = time[0][3:-2]
    memory = soup.find("td", class_="smemory")
    if memory is not None:
        memory = memory.contents
    if memory is not None and len(memory) > 0:
        memory = memory[0][10:-6]
    lang = soup.find("td", class_="slang")
    if lang is not None:
        lang = lang.span
    if lang is not None:
        lang = lang.contents
    if lang is not None and len(lang) > 0:
        lang = lang[0]
    if name is not None:
        name = name.encode("utf8")
    my_info.append(name)
    if id is not None:
        id = id.encode("utf8")
    my_info.append(id)
    if date is not None:
        date = date.encode("utf8")
    my_info.append(date)
    if status is not None:
        status = status.encode("utf8")
    my_info.append(status)
    if time is not None:
        time = time.encode("utf8")
    my_info.append(time)
    if memory is not None:
        memory = memory.encode("utf8")
    my_info.append(memory)
    if lang is not None:
        lang = lang.encode("utf8")
    my_info.append(lang)
    if reference is not None:
        reference = reference.encode("utf8")
    my_info.append(reference)
    '''
    print "name: ",name, len(name)
    print "id: ",id, len(id)
    print "date: ",date, len(date)
    print "status: ",status, len(status)
    print "time: *", time,"*", len(time)
    print "memory: *",memory,"*", len(memory)
    print "language: ",lang, len(lang)
    print "reference: ", reference, len(reference)
    '''
    code = reference.split('/')
    code = code[-2]
    if code is not None:
        code = code.encode("utf8")
    my_info.append(code)
    information.append(my_info)
    # print "code: ",code, len(code)
    print "url: ",base+'submit/'+code+"/id="+id
    answers.append(base+'submit/'+code+"/id="+id)

with open("information.csv","w+") as file:
    wr = csv.writer(file)
    wr.writerows(information)

for i in range(len(answers)):
    link = answers[i]
    br.open(link)
    soup = BeautifulSoup(br.response().read())
    #print soup.prettify().encode("utf8")
    source_code = soup.find("textarea")
    lang = information[i][-3]
    if lang == "C" or lang == "c":
        extension = ".c"
    elif lang == "CPP" or lang == "Cpp" or lang == "C++":
        extension = ".cpp"
    elif lang == "JAVA" or lang == "java" or lang == "Java":
        extension = ".java"
    elif lang == "Python" or lang == "PYTHON" or lang == "python":
        extension = ".py"
    else:
        extension = ".txt"

    file = open(destination+"/"+information[i][-1]+extension,"w+")
    solution = source_code.contents[0].encode("utf8")
    file.write(solution)
    file.close()
    print solution
