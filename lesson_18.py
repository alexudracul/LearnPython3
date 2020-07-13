# Создайте класс BlogPost с атрибутами user_name, text, number_of_likes.
# Создайте два объекта этого класса. После создания измените атрибут number_of_likes одного из объектов.
# Распечатайте атрибут number_of_likes каждого из объектов


class BlogPost:
    number_of_likes = 0

    def __init__(self, user_name, text):
        self.user_name = user_name
        self.text = text


first_post = BlogPost('John', 'Lorem ipsum')
second_post = BlogPost('Jane', 'Some text for some blog')
second_post.number_of_likes = 5

print(first_post.number_of_likes)
print(second_post.number_of_likes)
