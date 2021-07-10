# Generated by Django 3.2.3 on 2021-07-07 18:09

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, help_text='Upload a product image', null=True, upload_to='images/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]