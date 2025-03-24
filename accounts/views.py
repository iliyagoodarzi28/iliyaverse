from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect,render


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        # Log the user in after successful registration
        login(self.request, user)
        messages.success(self.request, 'ثبت‌نام با موفقیت انجام شد!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'خطایی رخ داده است. لطفاً دوباره تلاش کنید.')
        return super().form_invalid(form)

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # Log the user in
        login(self.request, form.get_user())
        messages.success(self.request, 'به حساب کاربری خود خوش آمدید!')
        
        # Redirect to the next URL or home if not provided
        next_url = self.request.GET.get('next', reverse_lazy('home'))
        return redirect(next_url)

    def form_invalid(self, form):
        messages.error(self.request, 'نام کاربری یا رمز عبور اشتباه است. لطفاً دوباره تلاش کنید.')
        return super().form_invalid(form)

    def get_success_url(self):
        # Redirect to 'home' or another page after login
        return reverse_lazy('home')

class CustomLogoutView(View):
    def get(self, request):
        # نمایش صفحه تأیید خروج
        return render(request, 'accounts/confirm_logout.html')

    def post(self, request):
        # خروج کاربر پس از تأیید
        logout(request)
        messages.info(request, 'شما با موفقیت از حساب کاربری خود خارج شدید.')
        return redirect(reverse_lazy('home'))