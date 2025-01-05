# quiz/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Question, Answer

# Landing Page View
class LandingPageView(TemplateView):
    template_name = "landing_page.html"

# Question View
# quiz/views.py

class QuestionView(TemplateView):
    template_name = "question.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     question = Question.objects.get(step=self.kwargs['step'])
    #     context['question'] = question
    #     context['answers'] = question.answers.all()  # دسترسی به پاسخ‌ها از طریق related_name
    #     return context


    def post(self, request, *args, **kwargs):
        # ذخیره پاسخ کاربر
        selected_answer = request.POST.get('answer')
        # می‌توانید لاجیک بیشتری برای ذخیره و بررسی پاسخ‌ها اضافه کنید

        # هدایت به سوال بعدی
        next_question = Question.objects.filter(pk__gt=self.kwargs['pk']).first()
        if next_question:
            return redirect('question', pk=next_question.pk)
        return redirect('login')  # در صورت اتمام سوالات به صفحه ورود هدایت می‌شود

# Login View
class LoginView(TemplateView):
    template_name = "login.html"

# Purchase View
class PurchaseView(TemplateView):
    template_name = "purchase.html"
