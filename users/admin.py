from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm
from .models import User
 
class CustomUserAdmin(UserAdmin):
   add_form = UserCreationForm
 
  
   list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_admin','my_country', 'fav_countries', 'creation_date', 'update_date', 'last_request' )
   list_filter = ('is_admin',)
   fieldsets = (
       (None, {'fields': ('email', 'password')}),
       ('Permissions', {'fields': ('is_admin',)}),
   )
   add_fieldsets = (
       (None, {
           'classes': ('wide',),
           'fields': ('email','password1', 'password2'),
       }),
   )
   ordering = ('email',)
   filter_horizontal = ()
 
 
# Now register the new UserAdmin...
admin.site.register(User, CustomUserAdmin)
