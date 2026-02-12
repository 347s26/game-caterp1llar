from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    name = models.CharField(
        max_length=20,
        unique=False,
        help_text="Enter a player name.",
    )

    games_won = models.IntegerField(
        
    )                                        

    color = ColorField(default='#FF0000') #TODO: this needs a package install

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('user-detail-view', args=[str(self.id)]) # Detail view not created yet?
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'User with the name {self.name}, represented by the color {self.color} that has won {self.games_won} games.'

class Loc(models.Model):
    x = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('loc-detail-view', args=[str(self.id)]) # Detail view not created yet?

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'Location on board at ({self.x}, {self.y})'




class Game(models.Model):
    # Fields

    player1 = models.OneToOneField(User, on_delete=models.CASCADE)
    player2 = models.OneToOneField(User, on_delete=models.CASCADE)

    head = models.OneToOneField(Loc, on_delete=models.CASCADE)
    tail = models.OneToOneField(Loc, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('game-detail-view', args=[str(self.id)]) # Detail view not created yet?

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'Caterpillar Game: {self.player1} vs. {self.player2}'


class Move(models.Model):
    start = models.OneToOneField(Loc, on_delete=models.CASCADE, null=False)
    end = models.OneToOneField(Loc, on_delete=models.CASCADE, null=False)
    player = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    time = models.DateTimeField(null=True)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, null=False)

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('move-detail-view', args=[str(self.id)]) # Detail view not created yet?
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'Current move: {self.player} moved from {self.start} to {self.end}.'

