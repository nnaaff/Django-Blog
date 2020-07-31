# Django-Blog
A simple blog illustrating the basic concepts of Django using SQLite.

Users can **"Sign Up"**, **"Login"**, **"View"** existing articles, **"Create"** a new article, and **"Logout"** of the blog.

## Logged Out:
- Users can only view any existing articles when not logged in.
- Users have an option to *Login* and *Sign Up*. 
- In order to create and add a new article, new users must sign up and existing users must log in.

## Logged In:
- Users can now create and add a new article.
- Users can choose to upload an image as the thumbnail of their article, or leave it which results in the use of a default thumbnail image.
- The *Title* of the article is automatically converted into a slug.
- Users can *Logout*.

Only the **Admin**(superuser) profile has article modification and deletion rights.
