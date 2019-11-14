from django.shortcuts import render, redirect, reverse
from .models import Dot
import markdown  # 转为html显示
from django.views import View
from django import forms
from mdeditor.fields import MDTextFormField


class MDEditorForm(forms.Form):
    question = forms.CharField()
    answer = MDTextFormField()


class MDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Dot
        fields = '__all__'


class IndexView(View):

    def get(self, request):
        dots = Dot.objects.values('id','question')
        context = {'dots':dots}
        # print(context)
        return render(request, 'share/index.html', context)


class DotView(View):
    def get(self, request, id):
        # print(id)
        try:
            dot = Dot.objects.get(id=id).answer
            answer = markdown.markdown(dot, extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',  # 语法高亮拓展
                'markdown.extensions.toc'  # 自动生成目录
            ])
        except:
            answer = '不存在'
        context = {'answer': answer}
        return render(request, 'share/dot.html', context)


class AddDotView(View):
    def get(self, request):
        form = MDEditorForm()
        context = {'form': form}
        return render(request, 'share/add.html', context)

    def post(self, request):
        # print(request.POST)
        if request.method != 'POST':
            form = MDEditorModleForm()
        else:
            form = MDEditorModleForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect(reverse('index'))

