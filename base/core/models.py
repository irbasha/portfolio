from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Person'

    def __str__(self):
        return self.full_name

class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    profile_bio = models.TextField()
    job_role = models.CharField(max_length=100)
    current_designation = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    resume = models.FileField()

    class Meta:
        verbose_name_plural = 'Profile'
    
    def __str__(self):
        return self.person.full_name

class Contact(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    address3 = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, null=True)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.person.full_name

class Skills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=50)
    skill_rating = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.skill_name

class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    currently_working_here = models.BooleanField(default=False)
    responsibilities = models.TextField()

    class Meta:
        verbose_name_plural = 'Experience'

    def __str__(self):
        return self.designation

    def get_start_date(self):
        return self.from_date.strftime("%m %Y")

    def get_end_date(self):
        if self.currently_working_here:
            return "Present"
        return self.from_date.strftime("%m %Y")


class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    currently_studing_here = models.BooleanField(default=False)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.degree

    def get_start_date(self):
        return self.from_date.strftime("%m %Y")

    def get_end_date(self):
        if self.currently_studing_here:
            return "Present"
        return self.from_date.strftime("%m %Y")

class Projects(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    projecttype = models.CharField(max_length=50)
    technologies = models.CharField(max_length=200)
    sourcecode = models.CharField(max_length=200, blank=True, null=True)
    hostsite = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.title
