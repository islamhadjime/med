from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Post, Category
from .forms import PhoneForm,FormEmail



def persion(request):
    context = {
        'dark':True,
        "form":FormEmail(),
    }
    return render(request,'posts/person.html',context)

def home(request):
  return render(request,'posts/home.html',{'categorys':'',"form":FormEmail(),})

def about(request):
    context = {
        'dark':True,
        "form":FormEmail(),
    }
    return render(request,'posts/about.html',context)

def servicarse(request):
    isActiv = False
    if request.method == 'POST':
        form = FormEmail(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd["name"],
            tel = cd["tel"],
            question = cd["des"]
            send_mail(
                'Сообщение от {}'.format(name),
                'Имя пользователя: {}   сообщения: {}   контакт:{} '.format(name,question,tel),
                'от кого <{}>'.format(settings.EMAIL_HOST_USER),
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            isActiv = True
            context = {
                'categorys':Category.objects.all(),
                'dark':True,
                "form":FormEmail(),
                "isActiv":isActiv
            }
            return render(request,'apps/services.html',context)
    else:
        context = {
            'categorys':'',
            'dark':True,
            "form":FormEmail(),
            "isActiv":isActiv
        }
        return render(request,'posts/services.html',context)

def detail_all(request,pk):
    category = Category.objects.get(pk=pk)
    if category == '':
      pkID = '' 
    pkID     = category.post.all()[0].pk
    return redirect('detail',pk=pkID)

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    isActivPhone= False
    isActivEmail = False

    if request.method == 'POST':
        phone = PhoneForm(request.POST,prefix='form1')
        form = FormEmail(request.POST,prefix='form2')

        if phone.is_valid():
            isActivPhone = True
            cd = phone.cleaned_data
            tel = cd['tel']
            send_mail(
                'Консультация названия  поста  {}'.format(post.title),
                'Пользователь хочет получит консультацию : {}    контакт:{} '.format(post.title,tel),
                'от кого <{}>'.format(settings.EMAIL_HOST_USER),
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            context ={
                'post':post,
                'dark':True,
                'phone':phone,
                'form':form,
                'isActivPhone':isActivPhone,
                'isActivEmail':isActivEmail,
            }
        elif form.is_valid():
            isActivEmail = True
            cd = form.cleaned_data

            name = cd["name"],
            tel = cd["tel"],
            question = cd["des"]
            
            send_mail(
                'Новый Заказ на   {}'.format(post.title),
                'Имя пользователя: {}   сообщения: {}   контакт:{} '.format(name,question,tel),
                'от кого <{}>'.format(settings.EMAIL_HOST_USER),
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            context ={
                'post':post,
                'dark':True,
                'phone':phone,
                'form':form,
                'isActivPhone':isActivPhone,
                'isActivEmail':isActivEmail,
            }
        return render(request, 'posts/detail_post.html',context)
    else:
        phone = PhoneForm(prefix='form1')
        form = FormEmail(prefix='form2')
    context ={
        'post':post,
        'dark':True,
        'phone':phone,
        'form':form,
        'isActivPhone':isActivPhone,
        'isActivEmail':isActivEmail,
    }
    return render(request, 'posts/detail_post.html',context)