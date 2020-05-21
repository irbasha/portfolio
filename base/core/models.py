from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    profile_image = models.ImageField()
    bio = models.TextField()
    resume = models.FileField(null=True)
    facebook = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    address3 = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Person'

    def __str__(self):
        return self.name

class Profile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    dob = models.DateField()
    designation = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Profile'
    
    def __str__(self):
        return self.person.name

class Skills(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Experience(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    responsibilities = models.TextField()

    class Meta:
        verbose_name_plural = 'Experience'

    def __str__(self):
        return self.designation

class Education(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    degree = models.CharField(max_length=50)
    university = models.CharField(max_length=50)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Education'

    def __str__(self):
        return self.degree

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
