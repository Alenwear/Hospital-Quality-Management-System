from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect

from .forms import CreateUser
from .conf import settings


# Create your views here.

def login(request):
    return render(request, 'user/login.html')


# def registration(request):
#     if request.method == 'POST':
#         form = CreateUser(request.POST)
#         print(form)
#
#         if form.is_valid():
#             clean_form = form.cleaned_data
#             print(clean_form)
#             user = User.objects.create_user(username=clean_form['username'], password=clean_form['password2'])
#             user.is_staff = True
#             user.is_active = True
#             user.is_superuser = False
#             user.save()
#             return HttpResponseRedirect('registration_complete')
#         else:
#             print(form)
#             print('数据不符合要求')
#     else:
#         form = CreateUser()
#         # print(form)
#     return render(request, 'user/registration_form.html', {'form': form})
#
#
# def registration_complete(request):
#     return render(request, 'user/registration_complete.html')


def registration(request,
                 template_name='user/registration_form.html',
                 registration_form=CreateUser,
                 registered_user_redirect_to=None,
                 post_registration_redirect=None,
                 current_app=None,
                 extra_context=None):
    # if registered_user_redirect_to is None:
    #     registered_user_redirect_to = getattr(settings, 'LOGIN_REDIRECT_URL')

    # if request.user.is_authenticated():
    #     return redirect(registered_user_redirect_to)

    if not settings.USER_REGISTRATION_OPEN:
        return render(request, 'user/registration_closed.html')
        # return HttpResponseRedirect('closed')
        # return redirect(reverse('user_registration_closed'))

    # if post_registration_redirect is None:
    #     return render(request, 'user/registration_complete.html')
    #     # post_registration_redirect = reverse('user_registration_complete')

    if request.method == 'POST':
        form = registration_form(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data
            print(clean_form)
            user = User.objects.create_user(username=clean_form['username'], password=clean_form['password2'])
            user.is_staff = True
            user.is_active = True
            user.is_superuser = False
            user.save()
            # if settings.USERS_AUTO_LOGIN_AFTER_REGISTRATION:
            # user.backend = 'django.contrib.auth.backends.ModelBackend'
            # login(request, user)
            # return redirect(post_registration_redirect)
            return render(request, 'user/registration_complete.html')
            # return HttpResponseRedirect('complete')
    else:
        form = registration_form()

    current_site = get_current_site(request)

    context = {
        'form': form,
        'site': current_site,
        'site_name': current_site.name,
        'title': 'Register',
    }
    if extra_context is not None:  # pragma: no cover
        context.update(extra_context)
    return TemplateResponse(request, template_name, context)


# def registration_complete(request,
#                           template_name='user/registration_complete.html',
#                           current_app=None,
#                           extra_context=None):
#     context = {
#         # 'login_url': resolve_url(settings.LOGIN_URL),
#         'title': 'Registration complete',
#     }
#     if extra_context is not None:  # pragma: no cover
#         context.update(extra_context)
#     return TemplateResponse(request, template_name, context)


# def registration_closed(request,
#                         template_name='user/registration_closed.html',
#                         current_app=None,
#                         extra_context=None):
#     context = {
#         'title': 'Registration closed',
#     }
#     if extra_context is not None:  # pragma: no cover
#         context.update(extra_context)
#     return TemplateResponse(request, template_name, context)
