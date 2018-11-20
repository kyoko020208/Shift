from django,contrib,auth import login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import LoginForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        """
        Method for getting Request
        """

        context = {
            'form': LoginForm(),
        }

        #return unfilled form in login template
        return render(request, 'accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        """Method for getting POST"""

        #Create form
        form = LoginForm(request.POST)

        #Validation
        if not form.is_valid():
            #if validation fails, show the following message
            return render(request, 'accounts/login.html',{'form' : form})

        #Get User Object
        user = form.get_user()

        #login
        auth_login(request, user)

        #Redirect
        return redirect(reverse('shop:index'))

login = LoginView.as_view()