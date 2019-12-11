from django.db import models

# Create your models here.
class Player(models.Model):
    user_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    winPercentage = models.IntegerField()
    lossPercentage = models.IntegerField()
    drawPercentage = models.IntegerField()
    whiteWinPercentage = models.IntegerField()
    blackWinPercentage = models.IntegerField()
    def __str__(self):
        return self.user_name
class Game(models.Model):
    url = models.CharField(max_length=50)
    pgn = models.TextField()
    timeClass = models.CharField(max_length=30)
    rules = models.CharField(max_length=30)
    whiteResult = models.CharField(max_length=25)
    blackResult = models.CharField(max_length=25)
    def __str__(self):
        return self.url
class PlayerGames(models.Model):
    whitePlayer = models.ForeignKey(Player,related_name='White', on_delete=models.CASCADE)
    blackPlayer = models.ForeignKey(Player,related_name='Black', on_delete=models.CASCADE)
    gameUrl = models.ForeignKey(Game, on_delete=models.CASCADE)
    gameNum = models.CharField(max_length=50,default='25')
    def __str__(self):
        return self.gameNum
    