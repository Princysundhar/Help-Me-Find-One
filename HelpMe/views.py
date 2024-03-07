import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def log(request):
    return render(request,"index.html")

def log_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"
        if data.type == 'admin':
            return redirect('/admin_home')
        elif data.type == 'pending':
            return HttpResponse("<script>alert('wait for authentication');window.location='/'</script>")
        else:
            return redirect('/police_home')
    else:
        return HttpResponse("<script>alert('Invalid Authentication');window.location='/'</script>")

def admin_home(request):
    if request.session['lg'] == "":
        return HttpResponse("<script>alert('Session expired,Login again');window.location='/'</script>")

    return render(request,"admin/admin_index.html")

def police_home(request):
    if request.session['lg'] == "":
        return HttpResponse("<script>alert();window.location='/'</script>")
    else:
        return render(request,"police/police_index.html")

def logout(request):
    request.session['lg'] = ""
    return redirect('/')

def view_policestation(request):
    if request.session['lg'] == '':
        return HttpResponse("<script>alert('Session Expired, Login again'); window.location='/'</script>")
    else:
        data = police_station.objects.filter(LOGIN__type= 'pending')
        return render(request,"admin/view_policestation.html",{"data":data})

def view_approve_policestation(request,id):
    login.objects.filter(id=id).update(type = 'police')
    return redirect('/view_policestation#bb')

def view_rejected_policestation(request,id):
    login.objects.filter(id=id).update(type = 'reject')
    return redirect('/view_policestation#bb')

def approved_policestations(request):
    data = police_station.objects.filter(LOGIN__type= 'police')
    return render(request,"admin/view_approved_policestation.html",{"data":data})


# CRIME CATEGORY MANAGEMENT

def add_category(request):
    return render(request,"admin/add_category.html")

def add_category_post(request):
    categorys = request.POST['textfield']
    data = category.objects.filter(category_name=categorys)
    if data.exists():
        return HttpResponse("<script>alert('Already exist');window.location='/add_category#bb'</script>")
    else:

        obj = category()
        obj.category_name = categorys
        obj.save()
        return HttpResponse("<script>alert('Added Successfully');window.location='/add_category#bb'</script>")

def view_category(request):
    data = category.objects.all()
    return render(request,"admin/view_category.html",{"data":data})

def delete_category(request,id):
    category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_category#bb'</script>")

def view_wanted_details(request):
    data = wanted_details.objects.all()
    return render(request,"admin/view_wanted_details.html",{"data":data})

def view_missing_details(request):
    data = missing_details.objects.all()
    return render(request,"admin/view_missing_details.html",{"data":data})

def view_feedback(request):
    data = feedback.objects.all()
    return render(request,"admin/view_feedback.html",{"data":data})

def view_complaint(request):
    data = admin_complaint.objects.all()
    return render(request,"admin/view_complaints.html",{"data":data})

def send_reply_to_user(request,id):
    return render(request,"admin/send_reply.html",{"id":id})

def send_reply_to_user_post(request,id):
    reply = request.POST['textarea']
    reply_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    admin_complaint.objects.filter(id=id).update(reply = reply,reply_date = reply_date)
    return HttpResponse("<script>alert('Reply send to User');window.location='/view_complaint#bb'</script>")

# EMERGENCY CONTACT MANAGEMENT........

def add_emergency_contact(request):
    return render(request,"admin/add_emergency_contact.html")

def add_emergency_contact_post(request):
    name = request.POST['textfield']
    contact = request.POST['textfield2']
    data = emergency.objects.filter(name = name,emergency_contact=contact)
    if data.exists():
        return HttpResponse("<script>alert('Emergency contact already exist');window.location='/add_emergency_contact#bb'</script>")
    else:
        obj = emergency()
        obj.name = name
        obj.emergency_contact = contact
        obj.save()
        return HttpResponse("<script>alert('Emergency Contact added');window.location='/add_emergency_contact#bb'</script>")

def view_emergency_contact(request):
    data = emergency.objects.all()
    return render(request, "admin/view_emergency_contact.html", {"data":data})

def delete_emergency_contact(request,id):
    emergency.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Emergency Contact Deleted');window.location='/view_emergency_contact#bb'</script>")

################################################################################################################

#..... POLICE STATION MODULE ........

def register(request):
    return render(request,"police/Register.html")

def register_post(request):
    station_name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    email = request.POST['textfield5']
    contact = request.POST['textfield6']
    latitude = request.POST['textfield8']
    longitude = request.POST['textfield9']
    password = request.POST['textfield10']

    data = login.objects.filter(username=email)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/register#bb'</script>")
    else:
        lob_obj = login()
        lob_obj.username = email
        lob_obj.password = password
        lob_obj.type = 'pending'
        lob_obj.save()

        obj = police_station()
        obj.stationname = station_name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.contact = contact
        obj.latitude = latitude
        obj.longitude = longitude
        obj.LOGIN = lob_obj
        obj.save()
        return HttpResponse("<script>alert('Registeration Success');window.location='/register#bb'</script>")


# CRIMINAL MANAGEMENT

def add_criminal(request):
    data = category.objects.all()
    return render(request,"police/add_criminal.html",{"data":data})

def add_criminal_post(request):
    category = request.POST['select']
    name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    age = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\"+dt+'.jpg',photo)
    path = '/static/Image/'+dt+'.jpg'

    data = wanted_details.objects.filter(name=name,gender=gender,age=age,place=place,post=post,pin=pin,photo=photo,CATEGORY=category)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/add_criminal#bb'</script>")
    else:


        obj = wanted_details()
        obj.CATEGORY_id = category
        obj.name = name
        obj.gender = gender
        obj.age = age
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.photo = path
        obj.POLICESTATION = police_station.objects.get(id=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Criminal Added');window.location='/add_criminal#bb'</script>")

def view_criminal(request):
    data = wanted_details.objects.filter(POLICESTATION=police_station.objects.get(id=request.session['lid']))
    # data = wanted_details.objects.all()
    return render(request,"police/view_criminal.html",{"data":data})


def update_criminal(request, id):
    data1 = wanted_details.objects.get(id=id)
    data2 = category.objects.all()
    return render(request, "police/update_criminal.html", {"data1": data1, "data2": data2})


def update_criminal_post(request, id):
    category = request.POST['select']
    name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    age = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    if 'FileField' in request.FILES:
        photo = request.FILES['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%D")
        fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\" + dt + '.jpg', photo)
        path = '/static/Image/' + dt + '.jpg'
        wanted_details.objects.filter(id=id).update(CATEGORY=category, name=name, gender=gender, age=age, place=place,
                                                    post=post, pin=pin, photo=path)
        return HttpResponse("<script>alert('Updated Successfully');window.location='/view_criminal#bb'</script>")
    else:
        wanted_details.objects.filter(id=id).update(CATEGORY=category, name=name, gender=gender, age=age, place=place,
                                                    post=post, pin=pin)
        return HttpResponse("<script>alert('Updated Successfully');window.location='/view_criminal#bb'</script>")


def delete_criminal(request,id):
    wanted_details.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted Successfully');window.location='/view_criminal#bb'</script>")


# MISSING MANAGEMENT

def add_missing_details(request):
    return render(request,"police/add_missing_details.html")

def add_missing_details_post(request):
    name = request.POST['textfield']
    gender = request.POST['RadioGroup1']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    photo = request.FILES['fileField']
    id_proof = request.FILES['fileField2']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\" + dt + '.jpg', photo)
    fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\PROOF\\" + dt + '.pdf', id_proof)
    photo = '/static/Image/' + dt + '.jpg'
    id_proof = '/static/PROOF/' + dt + '.pdf'

    obj = missing_details()
    obj.name = name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.gender = gender
    obj.photo = photo
    obj.type = 'police'
    obj.id_proof = id_proof
    obj.status = 'pending'
    obj.POLICESTATION = police_station.objects.get(LOGIN=request.session['lid'])
    # obj.USER_id = 1
    obj.save()
    return HttpResponse("<script>alert('Missing added');window.location='/add_missing_details'</script>")

def view_missing(request):
    data = missing_details.objects.filter(POLICESTATION = police_station.objects.get(LOGIN=request.session['lid']),type='police')
    # data = missing_details.objects.filter(type = 'police')
    return render(request,"police/view_missing_details.html",{"data":data})

def update_missing(request,id):
    data = missing_details.objects.get(id=id)
    return render(request,"police/update_missing_details.html",{"data":data,"id":id})

def update_missing_post(request,id):
    try:
        name = request.POST['textfield']
        # gender = request.POST['RadioGroup1']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        photo = request.FILES['fileField']
        id_proof = request.FILES['fileField2']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\" + dt + '.jpg', photo)
        fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\PROOF\\" + dt + '.pdf', id_proof)
        photo = '/static/Image/' + dt + '.jpg'
        id_proof = '/static/PROOF/' + dt + '.pdf'
        missing_details.objects.filter(id=id).update(name = name,photo = photo,
                                                     place = place,post = post,pin = pin,id_proof = id_proof)
        return HttpResponse("<script>alert('Missing Updated');window.location='/view_missing#bb'</script>")

    except Exception as e:
        name = request.POST['textfield']
        # gender = request.POST['RadioGroup1']
        place = request.POST['textfield2']
        post = request.POST['textfield3']
        pin = request.POST['textfield4']
        missing_details.objects.filter(id=id).update(name=name, place=place, post=post, pin=pin)
        return HttpResponse("<script>alert('Missing Updated');window.location='/view_missing#bb'</script>")


def delete_missing(request,id):
    missing_details.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Missing deleted');window.location='/view_missing'</script>")


# STATUS UPDATING

def update_status_missing(request,id):
    missing_details.objects.filter(id=id).update(status = 'found')
    return redirect('/view_missing#bb')


# CAMERA MANAGEMENT

def add_camera(request):
    return render(request,"police/add_camera.html")

def add_camera_post(request):
    camera_no = request.POST['textfield']
    obj = camera()
    obj.camera_no = camera_no
    obj.POLICESTATION = police_station.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse("<script>alert('Camera Added');window.location='/add_camera#bb'</script>")

def view_camera(request):
    data = camera.objects.all()
    return render(request,"police/view_camera.html",{"data":data})

def delete_camera(request,id):
    camera.objects.get(id=id).delete()
    return redirect('/view_camera#bb')

def view_complaints_from_user(request):
    data = police_complaint.objects.filter(POLICESTATION = police_station.objects.get(LOGIN=request.session['lid']))
    return render(request,"police/view_complaints_from_user.html",{"data":data})

def send_reply(request,id):
    return render(request,"police/send_reply_to_user.html",{"id":id})

def send_reply_post(request,id):
    reply = request.POST['textarea']
    reply_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    police_complaint.objects.filter(id=id).update(reply = reply,reply_date = reply_date)
    return HttpResponse("<script>alert('Reply Sended');window.location='/view_complaints_from_user#bb'</script>")



########################################################################################################################################


# ............USER MODULE..............


def android_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        type = data[0].type
        res = user.objects.get(LOGIN=lid)
        name = res.name
        email = res.email
        photo = res.photo
        print(photo)

        return JsonResponse({"status":"ok","type":type,"lid":lid,"name":name,"email":email,"photo":photo})
    else:
        return JsonResponse({"status":None})

def android_user_registration(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['contact']
    photo = request.FILES['pic']  # Image field
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\" + dt + '.jpg', photo)
    photo = '/static/Image/' + dt + '.jpg'
    password = request.POST['password']
    data = login.objects.filter(username=email,password = password)
    if data.exists():
        return JsonResponse({"status":None})
    else:
        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.type = 'user'
        log_obj.save()

        obj = user()
        obj.name = name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.contact = contact
        obj.photo = photo
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({"status":"ok"})


def android_view_reply(request):
    lid = request.POST['lid']
    res = admin_complaint.objects.filter(USER__LOGIN= lid)

    ar = []
    for i in res:
        ar.append(
            {
                "cid" : i.id,
                "complaint" :i.complaints,
                "complaint_date" :i.complaint_date,
                "reply":i.reply,
                "reply_date":i.reply_date,
            }
        )
    print(ar)
    return JsonResponse({"status":"ok","data":ar})

def android_send_complaint(request):
    lid = request.POST['lid']
    complaint = request.POST['complaint']
    complaint_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    obj = admin_complaint()
    obj.complaints = complaint
    obj.complaint_date = complaint_date
    obj.reply = 'pending'
    obj.reply_date = '0000-00-00'
    obj.USER = user.objects.get(LOGIN= lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def android_view_police_reply(request):
    lid = request.POST['lid']
    # pid = request.POST['pid']
    res = police_complaint.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "pc_id":i.id,
                "complaint":i.complaints,
                "complaint_date":i.complaint_date,
                "reply":i.reply,
                "reply_date":i.reply_date,
                "police_info":i.POLICESTATION.stationname,
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_send_complaint_to_police(request):
    lid =request.POST['lid']
    # pid = request.POST['pid']
    complaints = request.POST['complaint']
    complaint_date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    obj = police_complaint()
    obj.complaints = complaints
    obj.complaint_date = complaint_date
    obj.reply = 'pending'
    obj.reply_date = '0000-00-00'
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    # obj.POLICESTATION_id = pid
    return JsonResponse({"status":"ok"})

def android_view_missing(request):
    res = missing_details.objects.all()
    ar= []
    for i in res:
        ar.append(
            {
                "mid" : i.id,
                "name" :i.name,
                "photo" :i.photo,
                "gender" : i.gender,
                "place" :i.place,
                "post":i.post,
                "pin":i.pin,
                "id_proof":i.id_proof,
                "type":i.type,
                "status":i.status
            }
        )
    return JsonResponse({"status":"ok","data":ar})


# MISSING REGISTERING(MANAGEMENT)

def android_add_missing(request):
    lid = request.POST['lid']
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    gender = request.POST['gender']
    file = request.FILES['id_proof']
    imgfile = request.FILES['pic']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\" + dt +'.jpg',imgfile)
    fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\PROOF\\" + dt +'.jpg',file)
    path = '/static/Image/' + dt + '.jpg'
    path1 = '/static/PROOF/' + dt + '.jpg'
    obj = missing_details()
    obj.name = name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.gender = gender
    obj.photo = path
    obj.type = 'user'
    obj.id_proof = path1
    obj.status = 'pending'
    obj.USER = user.objects.get(LOGIN=lid)
    # obj.POLICESTATION = '1'
    obj.save()
    return JsonResponse({"status":"ok"})

def android_view_missings(request):
    res = missing_details.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "mid":i.id,
                "name":i.name,
                "photo":i.photo,
                "gender":i.gender,
                "place":i.place,
                "post":i.post,
                "pin":i.pin,
                "id_proof":i.id_proof,
                "type":i.type,
                "status":i.status
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_delete_missing(request):
    mid = request.POST['mid']
    missing_details.objects.get(id=mid).delete()
    return JsonResponse({"status":"ok"})

def android_update_missing(request):

        mid = request.POST['mid']
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        gender = request.POST['gender']

        if 'file' in request.FILES:
            id_proof = request.FILES['file']
            fs = FileSystemStorage()
            d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\PROOF\\" + d + ".jpg", id_proof)
            path1 = '/static/PROOF/' + d + ".jpg"
            missing_details.objects.filter(id=mid).update(id_proof=path1)

        if 'pic' in request.FILES:
            photo = request.FILES['pic']
            fs = FileSystemStorage()
            d = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fs.save(r"C:\Users\DELL\PycharmProjects\HelpMe_FindOne\HelpMe\static\Image\\" + d + ".jpg", photo)
            path = '/static/Image/' + d + ".jpg"
            missing_details.objects.filter(id=mid).update(photo=path)
        missing_details.objects.filter(id=mid).update(name=name, place=place, post=post, pin=pin,gender=gender)

        return JsonResponse({"status":"ok"})





# VIEW EMERGENCY CONTACT

def android_view_emergency_contact(request):
    res = emergency.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "em_id":i.id,
                "name":i.name,
                "emergency_contact":i.emergency_contact
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_view_wanted_details(request):

    res = wanted_details.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "wid":i.id,
                "name":i.name,
                "gender":i.gender,
                "age":i.age,
                "place":i.place,
                "post":i.post,
                "pin":i.pin,
                "photo":i.photo,
                "category":i.CATEGORY.category_name,
                "police":i.POLICESTATION.stationname,
            }
        )
    # print(ar)
    return JsonResponse({"status":"ok","data":ar})

def android_view_missing_details(request):
    res = missing_details.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "mid":i.id,
                "name":i.name,
                "gender":i.gender,
                "place":i.place,
                "post":i.post,
                "pin":i.pin,
                "photo":i.photo,
                "id_proof":i.id_proof
            }
        )

    return JsonResponse({"status":"ok","data":ar})



