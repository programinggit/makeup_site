from django.core.management.base import BaseCommand
from beauty.models import Question, Answer

class Command(BaseCommand):
    help = 'سوالات و پاسخ‌ها را پر کنید'

    def handle(self, *args, **kwargs):
        # تعریف سوالات و پاسخ‌ها
        questions_answers = {
            "رنگ پوست شما چیست؟": [
                "روشن",
                "متوسط",
                "تیره",
                "زیتونی",
            ],
            "رنگ چشم شما چیست؟": [
                "آبی",
                "قهوه‌ای",
                "سبز",
                "عسلی",
            ],
            "رنگ موی شما چیست؟": [
                "مشکی",
                "قهوه‌ای",
                "بلوند",
                "قرمز",
            ],
            "چقدر با آرایش راحت هستید؟": [
                "خیلی راحت",
                "نیمه راحت",
                "ناراحت",
                "آرایش نمی‌کنم",
            ],
            "کجا خرید می‌کنید؟": [
                "فروشگاه‌های دارویی",
                "فروشگاه‌های بزرگ",
                "آنلاین",
                "فروشگاه‌های تخصصی زیبایی",
            ],
            "چند وقت یکبار می‌خواهید محصولات چشم و لب را دریافت کنید؟": [
                "روزانه",
                "هفتگی",
                "ماهیانه",
                "هرگز",
            ],
            "چه رنگ‌هایی را ترجیح می‌دهید اگر این محصولات را دریافت کنید؟": [
                "رنگ‌های گرم",
                "رنگ‌های سرد",
                "رنگ‌های خنثی",
                "بدون ترجیح",
            ],
            "چند وقت یکبار می‌خواهید محصولات پوست و ناخن را دریافت کنید؟": [
                "روزانه",
                "هفتگی",
                "ماهیانه",
                "هرگز",
            ],
            "چند وقت یکبار می‌خواهید محصولات مراقبت از پوست را دریافت کنید؟": [
                "روزانه",
                "هفتگی",
                "ماهیانه",
                "هرگز",
            ],
            "چند وقت یکبار می‌خواهید محصولات مراقبت از مو و بدن را دریافت کنید؟": [
                "روزانه",
                "هفتگی",
                "ماهیانه",
                "هرگز",
            ],
            "به طور کلی، چه عطرهایی را ترجیح می‌دهید؟": [
                "گلی",
                "میوه‌ای",
                "چوبی",
                "تازه",
            ],
            "کدام یک از برندهای زیبایی را دوست دارید (یا دوست دارید امتحان کنید)؟": [
                "برند الف",
                "برند ب",
                "برند ج",
                "برند د",
            ],
            "مشکلات پوستی خود را چگونه توصیف می‌کنید؟": [
                "خشک",
                "چرب",
                "حساس",
                "معمولی",
            ],
            "موی شما را چگونه توصیف می‌کنید؟": [
                "راست",
                "موج دار",
                "فر",
                "فرفری",
            ],
        }

        # ایجاد سوالات و پاسخ‌های مربوطه
        for question_text, answers in questions_answers.items():
            question = Question.objects.create(text=question_text, question_type='چند گزینه‌ای')
            for answer_text in answers:
                Answer.objects.create(question=question, text=answer_text)

        self.stdout.write(self.style.SUCCESS('سوالات و پاسخ‌ها با موفقیت پر شدند.'))
