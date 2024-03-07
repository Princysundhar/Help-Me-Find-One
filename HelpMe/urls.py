"""HelpMe_FindOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from HelpMe import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin_home', views.admin_home),
    path('', views.log),
    path('log_post', views.log_post),
    path('view_policestation', views.view_policestation),
    path('view_approve_policestation/<id>', views.view_approve_policestation),
    path('view_rejected_policestation/<id>', views.view_rejected_policestation),
    path('approved_policestations', views.approved_policestations),
    path('add_category', views.add_category),
    path('add_category_post', views.add_category_post),
    path('view_category', views.view_category),
    path('delete_category/<id>', views.delete_category),
    path('view_wanted_details', views.view_wanted_details),
    path('view_missing_details', views.view_missing_details),
    path('view_feedback', views.view_feedback),
    path('view_complaint', views.view_complaint),
    path('send_reply_to_user/<id>', views.send_reply_to_user),
    path('send_reply_to_user_post/<id>', views.send_reply_to_user_post),
    path('add_emergency_contact', views.add_emergency_contact),
    path('add_emergency_contact_post', views.add_emergency_contact_post),
    path('view_emergency_contact', views.view_emergency_contact),
    path('delete_emergency_contact/<id>', views.delete_emergency_contact),
    path('logout', views.logout),

#######################################################################################
    path('police_home',views.police_home),
    path('register',views.register),
    path('register_post',views.register_post),
    path('add_criminal',views.add_criminal),                            # CRIMINAL MANAGEMENT
    path('add_criminal_post',views.add_criminal_post),
    path('view_criminal',views.view_criminal),
    path('update_criminal/<id>',views.update_criminal),
    path('update_criminal_post/<id>',views.update_criminal_post),
    path('delete_criminal/<id>',views.delete_criminal),
    path('add_missing_details',views.add_missing_details),              # MISSING DETAILS MANAGEMENT
    path('add_missing_details_post',views.add_missing_details_post),
    path('view_missing',views.view_missing),
    path('update_missing/<id>',views.update_missing),
    path('update_missing_post/<id>',views.update_missing_post),
    path('delete_missing/<id>',views.delete_missing),
    path('delete_missing/<id>',views.delete_missing),
    path('update_status_missing/<id>',views.update_status_missing),
    path('add_camera',views.add_camera),                                # CAMERA MANAGEMENT
    path('add_camera_post',views.add_camera_post),
    path('view_camera',views.view_camera),
    path('delete_camera/<id>',views.delete_camera),
    path('view_complaints_from_user',views.view_complaints_from_user),
    path('send_reply/<id>',views.send_reply),
    path('send_reply_post/<id>',views.send_reply_post),

###################################################################################################################

    path('android_login',views.android_login),
    path('android_user_registration',views.android_user_registration),
    path('android_view_reply',views.android_view_reply),
    path('android_send_complaint',views.android_send_complaint),
    path('android_view_police_reply',views.android_view_police_reply),
    path('android_send_complaint_to_police',views.android_send_complaint_to_police),
    path('android_view_missing',views.android_view_missing),
    path('android_add_missing',views.android_add_missing),
    path('android_view_missings',views.android_view_missings),
    path('android_update_missing',views.android_update_missing),
    path('android_delete_missing',views.android_delete_missing),
    path('android_view_emergency_contact',views.android_view_emergency_contact),
    path('android_view_wanted_details',views.android_view_wanted_details),
    path('android_view_missing_details',views.android_view_missing_details),

]
