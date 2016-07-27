from django.shortcuts import render
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from .forms import FormularioDeLogin

# Create your views here.
#
def login(request):
    if request.method == 'POST':
        form = FormularioDeLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    django_login(request, user)
                    # return sucesso
                    return render(request, 'adm/adm_login.html', {})
                else:
                    # return usuário não ativo
                    return render(request, 'adm/adm_login.html', {})
            else:
                # erro de credenciais inválidas
                return render(request, 'adm/adm_login.html', {'errors': True, 'form': form})

    else:
        if request.user.is_authenticated() and request.user.is_active:
            # página administrativa
            return render(request, 'adm/adm_login.html', {})

    # return # página de login
    return render(request, 'adm/adm_login.html', {})

def logout(request):
    django_logout(request)
    return render(request, 'adm/adm_login.html', {})