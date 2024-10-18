from django.contrib import admin
from .models import Participant,Reservation
# Register your models here.
class ReservationInline(admin.TabularInline):
    model=Reservation
    extra=1
    can_delete=True
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('cin', 'email', 'first_name', 'last_name', 'username','created_at','update_at')
    list_filter = ('cin','username','last_name',)
    search_fields = ('cin', 'first_name','last_name','username')
    autocomplete_fields = ('reservations',)
    list_per_page = 2
    readonly_fields = ('created_at', 'update_at')
    exclude = ('created_at', 'update_at',) 
    fieldsets = (
        ('Login Information', {
            'fields': ('username', 'email'),
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'cin'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'update_at'),
        }),
    )
    inlines = [ReservationInline]
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        print(queryset)
        return queryset.order_by('-is_superuser', 'username')

class ReservationAdmin(admin.ModelAdmin):
    list_display=['reservation_date', 'conference' , 'participant' , 'confirmed']
    actions = ['confirmed']
    def confirmed (self,request,queryset):
        queryset.update(confirmed =True)
        self.message_user(request,"Les reservations sont confirmes")
    confirmed.short_description = "Reservation a non confirmes"
    def unconfirmed (self,request,queryset):
        queryset.update(confirmed =False)
        self.message_user(request,"Les reservations ne sont pas confirmes")
    unconfirmed.short_description = "Reservation a  confirmes"
   
admin.site.register(Participant,ParticipantAdmin)
admin.site.register(Reservation,ReservationAdmin)
