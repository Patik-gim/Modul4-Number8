from django.contrib import admin
from .models import Advertisemens

# Register your models here.
class AdvertisemensAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_at','auction']
    list_filter = ['auction','created_at']
    auction = ['make_auction_as_false', 'make_auction_as_True']
    fieldsets = (
        ('Общее', {
            'fields' :('title','description'),
        }),
        ('Финансы',{
            'fields' :('price','auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать возвожность торга')
    def make_auction_as_false(self,request,queryest):
        queryest.update(auction=False)
    
    @admin.action(description='Добавить возвожность торга')
    def make_auction_as_True(self,request,queryest):
        queryest.update(auction=True)
       

admin.site.register(Advertisemens,AdvertisemensAdmin)