from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import UserUpdateForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('contact:index')
        else:
            messages.warning(request, 'Verifique os dados informados.')

    return render(request, 'contact/user_update.html', {
        'form': form
    })

def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:login')
        messages.error(request, 'Login invalido')
    return render(
        request,
        'contact/user_update.html',
        {
            'form': form
        }
    )
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seus dados foram atualizados com sucesso.')
            return redirect('contact:index')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'contact/register.html', {'form': form})

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')