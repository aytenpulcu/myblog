from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect
from post.models import Blog_post,Comment
from .forms import MessageModelForm
from .models import Page
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


#user

def index(request):
    return render(request,"index.html")

def about(request):
    context=dict()
    return render(request,"about.html",context)

def page_show(request, page_slug):
    context = dict()
    context['page']= get_object_or_404(Page, slug=page_slug)
    return render(request, 'page.html', context)

def contact_us(request):
    context=dict()
    context['form'] = MessageModelForm()
    if request.method == 'POST':
        form = MessageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request,"contact.html",context)

def see_all(request):
    context=dict()
    items = Blog_post.objects.filter(
        status='published',
    )
    num = (items.all().count())/2
    round(num)
    context['left'] = items[:num]
    context['right'] = items[num:]
    return render(request,"all_posts.html",context)

def sign_in(request):
    context = dict()
    alerts=[]
    context['form'] = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            alerts.append("Kayıt başarılı giriş yapabilirsiniz.")
            return redirect('/hesap/giris/',context)
        else:
            username_check = User.objects.filter(
                username=request.POST['username']
            )
            if len(username_check) != 0:
                alerts.append("Kullanıcı adı uygun değil")
            elif request.POST['password1'] != request.POST['password2']:
                alerts.append("Şifreler aynı değil")
            elif len(request.POST['password1']) < 8:
                alerts.append("Şifre minimum 8 karakter olmalıdır.")
            else:
                alerts.append("Kayıt tamamlanamadı! Şifrenizin kullanıcı adı ile benzer olmamasına dikkat ediniz.")
            context['messages']=alerts
            return render(request,"accounts/sign.html",context)
    else:
        return render(request,"accounts/sign.html",context)
        

def log_in(request):
    context=dict()
    alerts=[]
    context['form'] = AuthenticationForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            alerts.append("Başarıyla giriş yapıldı.") 
        else:
             alerts.append("Girilen bilgilere göre kullanıcı bulunamadı.")
            
    context['messages'] =alerts
    return render(request,"accounts/login.html",context)
    
def log_out(request):
    context=dict()
    context['messages'] = ["Oturum Kapatıldı."]
    logout(request)
    return HttpResponseRedirect('/',context)
 
def see_cmnt(request):
    context=dict()
    items= Comment.objects.filter(
        user=request.user,
        status="published",
    )
    if len(items)==0:
        context['messages']=["Hiç yorum yapmadınız."]
    else:
        context['comments']=items
    return render(request,"accounts/comment.html",context)
