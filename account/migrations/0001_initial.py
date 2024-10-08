# Generated by Django 4.0.6 on 2022-09-07 21:58

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('is_resumeuser', models.BooleanField(default=True, verbose_name='Is resumeUser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.IntegerField(null=True, unique=True)),
                ('firstname', models.CharField(max_length=255, null=True)),
                ('lastname', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(default='', max_length=255, null=True)),
                ('dabadebis_dge', models.IntegerField(null=True)),
                ('dabadebis_tve', models.IntegerField(null=True)),
                ('dabadebis_weli', models.IntegerField(null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=255, null=True)),
                ('skills', models.CharField(max_length=555, null=True)),
                ('start_year', models.IntegerField(choices=[(1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], null=True)),
                ('start_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True)),
                ('end_year', models.IntegerField(choices=[(1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], null=True)),
                ('end_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True)),
                ('ganatlebis_etapi', models.CharField(max_length=255, null=True)),
                ('sad_miige_ganatleba', models.CharField(max_length=255, null=True)),
                ('sv', models.ImageField(blank=True, null=True, upload_to='resumes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GarigebisTipi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('saxeli', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lokacia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QonebisTipiCar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QonebisTipiHouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sache',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Statusi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('saxeli', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.category')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstandlastname', models.CharField(max_length=255, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('number', models.IntegerField(null=True)),
                ('profesia', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(default='', max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('skills', models.CharField(max_length=555, null=True)),
                ('shesaxeb', models.CharField(max_length=1000, null=True)),
                ('start_year', models.IntegerField(choices=[(1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], null=True)),
                ('start_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True)),
                ('end_year', models.IntegerField(choices=[(1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], null=True)),
                ('end_month', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True)),
                ('ganatlebis_etapi', models.CharField(max_length=255, null=True)),
                ('sad_miige_ganatleba', models.CharField(max_length=255, null=True)),
                ('interesebi', models.CharField(max_length=1000, null=True)),
                ('gamocdileba', models.CharField(max_length=1000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sartuli', models.IntegerField(blank=True, null=True)),
                ('sartulebi_sul', models.IntegerField(blank=True, null=True)),
                ('sadzineblebi', models.IntegerField(blank=True, null=True)),
                ('farti', models.IntegerField(blank=True, null=True)),
                ('brendi', models.CharField(blank=True, max_length=255, null=True)),
                ('modeli', models.CharField(blank=True, max_length=255, null=True)),
                ('weli', models.IntegerField(blank=True, null=True)),
                ('dzravi', models.CharField(blank=True, max_length=255, null=True)),
                ('feri', models.CharField(blank=True, max_length=255, null=True)),
                ('satauri', models.CharField(blank=True, max_length=255, null=True)),
                ('quchis_saxeli', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('telefonis_nomeri', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo2', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo3', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo4', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo5', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo6', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo7', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo8', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo9', models.FileField(blank=True, null=True, upload_to='products/')),
                ('photo10', models.FileField(blank=True, null=True, upload_to='products/')),
                ('dasturi', models.IntegerField(null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.category')),
                ('garigebis_tipi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.garigebistipi')),
                ('lokacia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.lokacia')),
                ('qonebisTipiCar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.qonebistipicar')),
                ('qonebisTipiHouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.qonebistipihouse')),
                ('sache', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.sache')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.sub_category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('comment', models.TextField(null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='account.product')),
            ],
        ),
    ]
