from django.contrib import admin

# Register your models here.
# a new import
from blogging.models import Post, Category, custm_CategoryModel


# and a new admin registration

class category_inline(admin.TabularInline):
    model = custm_CategoryModel

class PostAdmin(admin.ModelAdmin):
    inlines = [category_inline,]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(custm_CategoryModel, category_inline)
