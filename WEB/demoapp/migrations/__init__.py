from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('name', models.CharField(max_length=50, null=False)),
                ('age', models.IntegerField(null=False)),
                ('gender', models.CharField(max_length=1, null=False)),
                ('doctor', models.CharField(max_length=50, null=False)),
                ('date',  models.IntegerField(null=False))
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]