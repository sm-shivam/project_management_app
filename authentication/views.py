from django.shortcuts import render,redirect
from .models import User,Company
from django.views import View
# from .serializers import UserSerializer,CompanySerializer
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response

# # Create your views here.
# class Register(APIView):

#     def get(self,request):
#         pass

#     def post(self,request):
#         data = request.data
#         if not (data.get('email') and data.get('password') and data.get('firstname') and data.get('lastname') and data.get('mobile')):
#             return Response({'message':'Please enter all required fields !'})

#         serializer = UserSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Register(View):
    def get(self,request):
        pass

    def post(self,request):
        data = request.data
        if not (data.get('email') and data.get('password') and data.get('firstname') and data.get('lastname') and data.get('mobile')):
            return render(request,'html',{'message':'Please enter all required fields !'})
        
        user = User(email=data.get('email'),firstname=data.get('firstname'),lastname=data.get('lastname'),password=data.get('password'),mobile=data.get('mobile'))
        user.save()
        return redirect(request,'some_html',{'user_data':user})

class login(View):
    def get(self,request):
        pass
    def post(self,request):
        pass


# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         context = {'form':form}
#         if form.is_valid():
#             user = form.save()
#             created = True
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             context = {'created' : created}
#             return render(request, 'register/reg_form.html', context)
#         else:
#             return render(request, 'register/reg_form.html', context)
#     else:
#         form = RegistrationForm()
#         context = {
#             'form' : form,
#         }
#         return render(request, 'register/reg_form.html', context)


# def usersView(request):
#     users = UserProfile.objects.all()
#     tasks = Task.objects.all()
#     context = {
#         'users': users,
#         'tasks': tasks,
#     }
#     return render(request, 'register/users.html', context)

# def user_view(request, profile_id):
#     user = UserProfile.objects.get(id=profile_id)
#     context = {
#         'user_view' : user,
#     }
#     return render(request, 'register/user.html', context)


# def profile(request):
#     if request.method == 'POST':
#         img_form = ProfilePictureForm(request.POST, request.FILES)
#         print('PRINT 1: ', img_form)
#         context = {'img_form' : img_form }
#         if img_form.is_valid():
#             img_form.save(request)
#             updated = True
#             context = {'img_form' : img_form, 'updated' : updated }
#             return render(request, 'register/profile.html', context)
#         else:
#             return render(request, 'register/profile.html', context)
#     else:
#         img_form = ProfilePictureForm()
#         context = {'img_form' : img_form }
#         return render(request, 'register/profile.html', context)


# def newCompany(request):
#     if request.method == 'POST':
#         form = CompanyRegistrationForm(request.POST)
#         context = {'form':form}
#         if form.is_valid():
#             form.save()
#             created = True
#             form = CompanyRegistrationForm()
#             context = {
#                 'created' : created,
#                 'form' : form,
#                        }
#             return render(request, 'register/new_company.html', context)
#         else:
#             return render(request, 'register/new_company.html', context)
#     else:
#         form = CompanyRegistrationForm()
#         context = {
#             'form' : form,
#         }
#         return render(request, 'register/new_company.html', context)


# def invites(request):
#     return render(request, 'register/invites.html')


# def invite(request, profile_id):
#     profile_to_invite = UserProfile.objects.get(id=profile_id)
#     logged_profile = get_active_profile(request)
#     if not profile_to_invite in logged_profile.friends.all():
#         logged_profile.invite(profile_to_invite)
#     return redirect('core:index')


# def deleteInvite(request, invite_id):
#     logged_user = get_active_profile(request)
#     logged_user.received_invites.get(id=invite_id).delete()
#     return render(request, 'register/invites.html')


# def acceptInvite(request, invite_id):
#     invite = Invite.objects.get(id=invite_id)
#     invite.accept()
#     return redirect('register:invites')

# def remove_friend(request, profile_id):
#     user = get_active_profile(request)
#     user.remove_friend(profile_id)
#     return redirect('register:friends')