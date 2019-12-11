from django.contrib import admin
from .models import PlayerGames,Player,Game
# Register your models here.
admin.site.register(PlayerGames)
admin.site.register(Player)
admin.site.register(Game)