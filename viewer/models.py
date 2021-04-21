from django.db.models import (
    CharField, Model, DateField, DateTimeField, ForeignKey, TextField, IntegerField, DO_NOTHING
)


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=170)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.released.year}) - {self.genre.name}'

    def __repr__(self):
        return f'{self.title} ({self.released.year}) - {self.genre.name}'

    # def save(self):
    #     self.title = self.title.capitalize()
    #     super(Movie, self).save()


