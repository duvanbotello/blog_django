from django.contrib import admin
from article.models import Article
from users.models import InformationUsers

# Register your models here.

class AticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    exclude = ('user',)
    #filtra articulos segun user
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    #modifica el metodo grabar del admin
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
       


admin.site.register(Article, AticleAdmin)  
admin.site.register(InformationUsers)  