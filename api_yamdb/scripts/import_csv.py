from reviews.models import (Category, Genre, User, Title,
                            Review, Comment, GenreTitle)
import csv


def run():
    with open('api_yamdb/static/data/category.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        Category.objects.all().delete()

        for row in reader:
            print(row)

            category = Category(id=row[0],
                                name=row[1],
                                slug=row[2])
            category.save()

    with open('api_yamdb/static/data/genre.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        Genre.objects.all().delete()

        for row in reader:
            print(row)

            genre = Genre(id=row[0],
                          name=row[1],
                          slug=row[2])
            genre.save()

    with open('api_yamdb/static/data/users.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        User.objects.all().delete()

        for row in reader:
            print(row)

            user = User(id=row[0],
                        username=row[1],
                        email=row[2],
                        role=row[3],
                        bio=row[4],
                        first_name=row[5],
                        last_name=row[6])
            user.save()

    with open('api_yamdb/static/data/titles.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        Title.objects.all().delete()

        for row in reader:
            print(row)

            category, _ = Category.objects.get_or_create(id=row[3])
            title = Title(id=row[0],
                          name=row[1],
                          year=row[2],
                          category=category)
            title.save()

    with open('api_yamdb/static/data/review.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        Review.objects.all().delete()

        for row in reader:
            print(row)

            title_id, _ = Title.objects.get_or_create(id=row[1])
            author_id, _ = User.objects.get_or_create(id=row[3])
            review = Review(id=row[0],
                            title=title_id,
                            text=row[3],
                            author=author_id,
                            score=row[4],
                            pub_date=row[5])
            review.save()

    with open('api_yamdb/static/data/comments.csv', encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        Comment.objects.all().delete()

        for row in reader:
            print(row)

            review_id, _ = Review.objects.get_or_create(id=row[1])
            author_id, _ = User.objects.get_or_create(id=row[3])
            comment = Comment(id=row[0],
                              review=review_id,
                              text=row[3],
                              author=author_id,
                              pub_date=row[4])
            comment.save()

    with open('api_yamdb/static/data/genre_title.csv',
              encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        GenreTitle.objects.all().delete()

        for row in reader:
            print(row)

            genre_id, _ = Genre.objects.get_or_create(id=row[2])
            title_id, _ = Title.objects.get_or_create(id=row[1])
            genre_title = GenreTitle(id=row[0],
                                     genre=genre_id,
                                     title=title_id)
            genre_title.save()
