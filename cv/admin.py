from django.contrib import admin

from .models import Tag,Post,Category,Skill,Profile,Referee
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields  = ['post_title','category__category_name','tags__tag_text']
    list_filter =('category',)
    #list_filter = (
        #('post_title', admin.FieldListFilter),
    #)
    #list_display = ('post_title', 'category')

admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Referee)
