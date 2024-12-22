from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text



class UserResponse(models.Model):
    """مدل برای ذخیره پاسخ‌های کاربران به سوالات."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # ارتباط با سوال
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)  # ارتباط با پاسخ انتخابی
    user_ip = models.GenericIPAddressField(null=True, blank=True)  # برای ثبت آدرس IP کاربر (اختیاری)
    timestamp = models.DateTimeField(auto_now_add=True)  # زمان ثبت پاسخ

    def __str__(self):
        return f"پاسخ به '{self.question.text}' از IP: {self.user_ip}"


class UserProfile(models.Model):
    """مدل اختیاری برای ذخیره اطلاعات پروفایل کاربر."""
    skin_tone = models.CharField(max_length=50)  # مانند: روشن، متوسط، تیره
    eye_color = models.CharField(max_length=50)  # مانند: آبی، قهوه‌ای، سبز
    hair_color = models.CharField(max_length=50)  # مانند: مشکی، قهوه‌ای، بلوند
    makeup_comfort = models.CharField(max_length=50)  # مانند: راحت، نیمه راحت، ناراحت
    preferred_brands = models.TextField(blank=True)  # برندهایی که کاربر دوست دارد یا می‌خواهد امتحان کند
    skin_concerns = models.TextField(blank=True)  # مشکلات پوستی کاربر
    user_ip = models.GenericIPAddressField(null=True, blank=True)  # برای ثبت آدرس IP کاربر (اختیاری)
    created_at = models.DateTimeField(auto_now_add=True)  # زمان ثبت پروفایل

    def __str__(self):
        return f"پروفایل برای {self.user_ip}"
