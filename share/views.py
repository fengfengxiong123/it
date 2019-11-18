from django.shortcuts import render, redirect, reverse
from .models import Dot
import markdown  # 转为html显示
from django.views import View
from django import forms
from mdeditor.fields import MDTextFormField
import re


class IndexView(View):

    def get(self, request):
        dots = Dot.objects.values('id', 'question', 'summary', 'date_time_last', 'user__nickname', 'user__username')
        context = {'dots': dots}
        context['keywords'] = '免费学习，前端，后端，服务器，开发，部署，python，centos，linux，nginx，uwsgi'
        context['description'] = '这是分享知识的平台，可以免费、系统学习知识，获得优质答案'
        context['title'] = '哦啦分享网'
        return render(request, 'share/index.html', context)


class DotsFontView(View):
    def get(self, request, arg):
        context = {}
        desc_str = '分享IT知识，免费学习{}知识，{}'
        if arg == 'font':
            dots = Dot.objects.filter(font=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
            context['keywords'] = '前端，html，css，JavaScript，JS，Vuew，React，免费学习'
            context['description'] = desc_str.format('前端', '找到问题的答案')
            context['title'] = '前端知识学习分享-哦啦分享网'
        elif arg == 'backend':
            dots = Dot.objects.filter(backend=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
            context['keywords'] = '后端，python，django，爬虫，java，c，分享知识，免费学习'
            context['description'] = desc_str.format('后端', '找到后端，python，django，爬虫等问题的答案')
            context['title'] = '后端知识学习分享-哦啦分享网'
        elif arg == 'server':
            dots = Dot.objects.filter(server=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
            context['keywords'] = '服务器命令，服务器知识，mysql安装，redis安装，nginx安装，uwsgi安装，依赖安装nginx配置，mysql配置，uwsgi配置，免费学习'
            context['description'] = desc_str.format('linux，centos服务器', '找到优质答案')
            context['title'] = '服务器知识学习分享-哦啦分享网'
        elif arg == 'dev':
            dots = Dot.objects.filter(dev=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
            context['keywords'] = '开发流程，开发思路，数据库设计，表设计，开发环境，依赖'
            context['description'] = desc_str.format('开发', '学习开发思维，找到优质答案')
            context['title'] = 'IT开发-哦啦分享网'
        elif arg == 'product':
            dots = Dot.objects.filter(product=1).values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
            context['keywords'] = '服务器，命令，报错，依赖，linux，centos，前端，后端，node，免费学习'
            context['description'] = desc_str.format('部署', '部署流程，报错解决方案，找到优质答案')
            context['title'] = '项目部署-生产环境部署-哦啦分享网'
        else:
            dots = Dot.objects.values('id', 'question', 'summary', 'date_time_last', 'user__nickname')
            context['keywords'] = '免费学习，前端，后端，服务器，开发，部署，python，centos，linux，nginx，uwsgi'
            context['description'] = '分享知识，免费学习知识，获得优质答案'
            context['title'] = '哦啦分享网'
        context['dots'] = dots
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


class MDEditorForm(forms.Form):
    question = forms.CharField(label='文章标题')
    answer = MDTextFormField(label='答')
    summary = forms.CharField(label='摘要')
    font = forms.BooleanField(label='前端', required=False)
    backend = forms.BooleanField(label='后端', required=False)
    server = forms.BooleanField(label='服务器', required=False)
    dev = forms.BooleanField(label='开发', required=False)
    product = forms.BooleanField(label='部署', required=False)


class MDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Dot
        fields = '__all__'


class AddDotView(View):

    def get(self, request):
        form = MDEditorForm()
        print(form)
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
