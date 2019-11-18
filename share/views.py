from django.shortcuts import render, redirect, reverse
from .models import Dot
import markdown  # 转为html显示
from django.views import View
from django import forms
from mdeditor.fields import MDTextFormField
import re


class MDEditorForm(forms.Form):
    question = forms.CharField(label='文章标题')
    answer = MDTextFormField(label='答')
    summary = forms.CharField(label='摘要')
    labelone = forms.CharField(label='标签一')
    labeltwo = forms.CharField(label='标签二')
    labelthree = forms.CharField(label='标签三')
    labelfour = forms.CharField(label='标签四')
    labelfive = forms.CharField(label='标签五')


class MDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Dot
        fields = '__all__'


class IndexView(View):

    def get(self, request):
        dots = Dot.objects.values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        context = {'dots': dots}
        return render(request, 'share/index.html', context)


class DotsFontView(View):
    def get(self, request, arg):
        if arg == 'font':
            dots = Dot.objects.filter(font=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        elif arg == 'backend':
            dots = Dot.objects.filter(backend=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        elif arg == 'server':
            dots = Dot.objects.filter(server=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        elif arg == 'dev':
            dots = Dot.objects.filter(dev=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        elif arg == 'product':
            dots = Dot.objects.filter(product=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        else:
            dots = Dot.objects.values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
        context = {'dots': dots}
        return render(request, 'share/index.html', context)


class DotView(View):
    def get(self, request, id):
        # print(id)
        try:
            dot = Dot.objects.get(id=id)
            dot_anser = dot.answer
            dot_question = dot.question

            answer = markdown.markdown(dot_anser, extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',  # 语法高亮拓展
                'markdown.extensions.toc'  # 自动生成目录
            ])
        except:
            answer = '不存在'
            dot_question = '不存在'
        context = {'answer': answer, 'question': dot_question}

        return render(request, 'share/dot.html', context)


class AddDotView(View):

    def get(self, request):
        form = MDEditorForm()
        context = {'form': form}
        return render(request, 'share/add.html', context)

    def post(self, request):
        auth_user_id = request.session.get('_auth_user_id')
        post_dict = request.POST.copy()
        html = request.POST['id_answer-wmd-wrapper-html-code'][:200]
        pattern = re.compile(r'<[^>]+>', re.S)
        result = pattern.sub('', html)
        post_dict['summary'] = result
        post_dict['user'] = auth_user_id
        form = MDEditorModleForm(post_dict)
        if form.is_valid():
            form.save()
        return redirect(reverse('share:index'))
