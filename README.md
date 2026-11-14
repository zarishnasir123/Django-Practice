# Django Practice

Hi, I'm Zarish. This repo is where I learned Django, one chapter at a time, from October to November 2026.

Every `ChNN` folder is a small separate project for one topic. I wrote the code, ran it, got errors, fixed them, and committed. So the code here is learner code: you'll find commented-out lines where I tried something one way and then another. I left them in on purpose, because that's how I understood things.

If you're learning Django too, feel free to go through it in the same order. I've written some notes at the end that I wish someone had told me earlier.

## How the folders work

- Each chapter has its own project and its own virtual environment, so breaking one chapter never broke the others.
- Chapters build on each other, so the order below is the order I'd recommend.
- From Ch56 onwards I used the same 10 students (same names, cities and marks) in every database chapter, so it's easy to compare what each query returns.
- `Bistro`, `BookReview` and `underconst` are small projects where I put things together.

## Chapter list

### Basics (Ch1–Ch10)

- **Ch1:** Made a virtual environment and installed Django. That's all, and it's the first step every chapter after this repeats.
- **Ch2–Ch4:** Created my first projects with `django-admin startproject` and looked at what each generated file is for (`settings.py`, `urls.py`, `manage.py`). Ch3 is where I ran `migrate` for the first time.
- **Ch5:** Created two apps (`app1`, `app2`) inside one project and added them to `INSTALLED_APPS`.
- **Ch6:** First views (`learn_python`, `math`) returning simple responses, and connecting them in `urls.py`.
- **Ch7–Ch8:** Views in two different apps (home, about pages) and giving each app its own `urls.py`, joined in the project with `include()`.
- **Ch9:** Added a third app (`course`) to see how a project grows.
- **Ch10:** Two apps that make sense together: `course` and `fees`.

### Templates and styling (Ch11–Ch21)

- **Ch11:** Moved from returning text to rendering HTML templates.
- **Ch12:** Sent data from a view to a template with a context dictionary, and showed student details with variables, `{% for %}` and `{% if %}`.
- **Ch13:** Static files: a `static` folder, `{% load static %}` and linking CSS and images.
- **Ch14:** Template inheritance: one `base.html` with `{% block %}`, and other pages that `{% extends %}` it, so the navbar is written once.
- **Ch15:** Inheritance again, this time with static files in the base template.
- **Ch16–Ch17:** Added Bootstrap to the base template and styled pages with its classes.
- **Ch18:** Tailwind CSS through a `theme` app.
- **Ch19:** Tailwind with the Tailwind CLI, which builds a CSS file from only the classes I used.
- **Ch20:** Links with `{% url 'name' %}` instead of typing paths, so changing a URL doesn't break links.
- **Ch21:** Splitting pages into small parts (like a navbar) and adding them with `{% include %}`.

### Models and admin (Ch22–Ch26)

- **Ch22:** My first model (`Profile`) and turning it into a table with `makemigrations` and `migrate`.
- **Ch23:** Reading data in views: `all_data` shows every row, `single_data` gets one row.
- **Ch24:** The built-in admin panel and `createsuperuser`.
- **Ch25:** Registering models (`Profile`, `Result`) in `admin.py` so they show in admin.
- **Ch26:** Making the admin list readable with `list_display`.

### Forms (Ch27–Ch40)

- **Ch27:** Form API basics: `Registration` and `Login` forms made with `forms.Form` and shown with `{{ form }}`.
- **Ch28:** Rendering each field by hand (labels, inputs and errors) instead of the whole form at once.
- **Ch29:** A `DemoForm` with lots of field types, field arguments (`required`, `initial`, `help_text`…) and widgets.
- **Ch30:** A form that actually submits: `request.method == 'POST'`, `is_valid()`, `cleaned_data`, then a success page.
- **Ch31:** Validation two ways: `clean_<field>()` for one field and `clean()` for checking fields together.
- **Ch32:** Built-in validators and writing my own validator functions.
- **Ch33:** Custom error messages and how errors are displayed.
- **Ch34:** Saving form data to a `Student` model, then updating and deleting rows.
- **Ch35:** `ModelForm`, which builds the form from the model so I don't repeat the fields.
- **Ch36:** ModelForm inheritance: one `Person` model, and `StudentRegistration` / `TeacherRegistration` forms that share fields.
- **Ch37:** My own template filter (`iamToweare`) in `templatetags`, plus Django's built-in filters.
- **Ch38:** A bigger form practice: a candidate profile with an image upload (`ImageField`, `MEDIA_URL`, `MEDIA_ROOT`) and a details page.
- **Ch38(b):** CKEditor, a rich-text editor for a blog `Post` (bold, lists, images inside the text).
- **Ch39:** Dynamic URLs: `<int:id>`, `<slug:subject>`, `<str:name>`, more than one value in one URL, and my own path converter for roll numbers like `2024-CS-001`.
- **Ch40:** Messages framework: `messages.success` and `messages.error` after saving or deleting a student, every message level, and custom `MESSAGE_TAGS`.

### Authentication (Ch41–Ch45)

- **Ch41:** Built-in users, groups and permissions, all managed from admin.
- **Ch42:** My own authentication system with function-based views, in three apps (`accounts`, `customer`, `seller`):
  - a custom `User` model that logs in with email instead of username
  - after registering, an activation link is emailed, and it stops working after 15 minutes
  - login (with a safe `next` redirect), logout, change password
  - forgot password and reset password, with a styled HTML email
  - Gmail SMTP settings kept in a `.env` file, and emails sent in a background thread so the page doesn't wait
- **Ch43:** Limiting pages by role. I wrote decorators like `customer_required` and `seller_required` in a `core` app and used them on views.
- **Ch44:** Role-based registration (sign up as a customer or a seller) with a few extra security checks.
- **Ch45:** Giving permissions in code. A config file says which role gets which permissions, and they're added when a user registers. Customers can only view products; sellers can add, edit and delete them. Buttons in the templates are hidden with `perms` too.

### Cookies, sessions, caching (Ch46–Ch52)

- **Ch46:** Cookies: `set_cookie`, reading them from `request.COOKIES`, expiry with `max_age` and `expires`, signed cookies, and deleting. There's a `readme.txt` in this folder about `set_cookie`.
- **Ch47:** Database sessions: set, get, delete one key, `flush()`, `clear_expired()`, test cookies, and session methods used in both views and templates.
- **Ch48:** The same with file-based sessions.
- **Ch49:** Per-site caching with the cache middleware.
- **Ch50:** Per-view caching with `@cache_page`.
- **Ch51:** Caching only part of a template with `{% cache %}` (good for seeing how long a cached block stays).
- **Ch52:** The low-level cache API: `cache.get`, `cache.set`, `get_or_set`, and versions.

### Signals and middleware (Ch53–Ch55)

- **Ch53:** Built-in signals with `@receiver`: login, logout, login failed, `pre_save`/`post_save`, `pre_delete`/`post_delete`, `pre_init`/`post_init`, `pre_migrate`/`post_migrate`, and request started, finished and exception.
- **Ch54:** Making and sending my own signals.
- **Ch55:** Middleware: a function middleware, class middlewares, several of them at once to see the order (in top to bottom, out bottom to top), and the hooks `process_view`, `process_exception` and `process_template_response`.

### Database queries (Ch56–Ch63)

All of these use the same 10 students, so you can compare results.

- **Ch56:** Methods that return a QuerySet: `all`, `filter`, `exclude`, `order_by`, `reverse`, `values`, `values_list`, `distinct`, `dates`, `only`, `defer`, and `union`, `intersection` and `difference` with a `Teacher` table. Each one also prints its SQL.
- **Ch57:** Methods that return something else: `get`, `first`, `last`, `latest`, `exists`, `count`, `in_bulk`, `aggregate`, `create`, `get_or_create`, `update_or_create`, `bulk_create`, `update`, `delete`.
- **Ch58:** Field lookups: `exact`, `iexact`, `contains`, `icontains`, `startswith`, `endswith`, `in`, `range`, `gt`/`gte`/`lt`/`lte`, date parts (`year`, `month`, `week_day`, `quarter`…), `isnull`, `regex`.
- **Ch59:** `aggregate()` with `Avg`, `Sum`, `Min`, `Max`, `Count`, and `annotate()` to make a report per city.
- **Ch60:** `Q` objects for OR (`|`), AND (`&`) and NOT (`~`), and building a search filter in a loop.
- **Ch61:** Limiting results with slicing (`[:5]`, `[5:10]`) and why negative slicing isn't allowed.
- **Ch62:** Model inheritance: an abstract `BaseModel` shared by `Student`, `Teacher` and `Contractor`, and multi-table inheritance.
- **Ch63:** Model managers: renaming `objects` and writing a custom manager.

### Relationships (Ch64–Ch67)

- **Ch64:** One to one: a `Profile` for each `User`, trying different `on_delete` options and `limit_choices_to`, and a `Like` model that inherits from `Page` with `parent_link`.
- **Ch65:** Many to one with `ForeignKey`: one user, many posts.
- **Ch66:** Many to many: many users linked to many songs, and showing the users in admin.
- **Ch67:** All three in one app (users, pages, posts, songs) with a page for each, and filters that go across models like `user__page__pcat` or `post__isnull`.

### Other (Ch68)

- **Ch68:** Context processors: the site name, a cart count read from the session, and a "Hello, user" greeting available in every template without sending them from any view.

### Async Django (Ch69–Ch76)

- **Ch69:** Running Django on ASGI with Daphne (added to `INSTALLED_APPS`, then `runserver` uses it).
- **Ch70:** Running Django with Uvicorn: `uvicorn Ch70.asgi:application --reload`.
- **Ch71:** A sync view and an async view that both call an API 5 times. The sync one calls one by one; the async one calls all 5 together with `httpx` and `asyncio.gather`, and returns the time each took.
- **Ch72:** `sync_to_async` (using the normal ORM from an async view) and `async_to_sync`, plus serving static files from `urls.py`.
- **Ch73:** Fixing missing CSS on Uvicorn with `ASGIStaticFilesHandler` in `asgi.py`.
- **Ch74:** The same fix with WhiteNoise in `settings.py`.
- **Ch75:** The async ORM: `async for`, `acount()`, `afirst()` and others. `note.txt` lists which ORM calls work in async views and which don't.
- **Ch76:** Async middleware: a function middleware and a class middleware that are async only (`sync_capable` / `async_capable`, `markcoroutinefunction`), and a hybrid one that works under both `runserver` and Uvicorn. Tested with an async view that waits one second.

### Class-based views (Ch77–Ch79)

- **Ch77:** My first class-based views with the base `View` class. I wrote the same pages (home, about, contact with a form, news) first as function views, then as classes with `get()` and `post()`, and connected them with `.as_view()`. The contact form shows a thank-you page after a valid submit. One `NewsView` class serves two templates by changing `template_name` in `as_view()`.
- **Ch78:** `TemplateView`: `template_name`, sending data with `get_context_data()` (and why `super()` comes first), `extra_context`, and URL values arriving in `kwargs`. Pages like home, about, contact and profile, some with their own class and some with `TemplateView` straight in `urls.py`.
- **Ch79:** `RedirectView`: redirecting to a fixed `url`, to a URL name with `pattern_name`, temporary (302) vs `permanent=True` (301), carrying URL values over, keeping `?q=` with `query_string=True`, and working out the address in `get_redirect_url()`.

## Small projects

- **Bistro:** a restaurant website with Tailwind CSS.
- **BookReview:** books and reviews. You have to log in to write a review, and you can filter books by genre. I made it to practise everything up to the forms chapters.
- **underconst:** a "site under construction" switch. Tick a box in admin and every visitor sees the maintenance page (done with middleware), while staff can still use the site. It can turn itself off at a set time.

I also made a separate project with what I learned here: **[Django QR Code Generator](https://github.com/zarishnasir123/Django-QR-Code-Generator)**.

## How to run a chapter

```bash
cd Ch42
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

On macOS/Linux, activate with `source venv/bin/activate` instead.

A few chapters have a `requirements.txt`. Later chapters need an extra package; if you get `ModuleNotFoundError`, install the missing one (for example `python-decouple`, `uvicorn`, `daphne`, `httpx` or `whitenoise`).

For the async chapters, run the server with Uvicorn instead, for example `uvicorn Ch75.asgi:application --reload`.

The databases aren't in the repo anymore (older commits still have them, but those were only practice data), so every chapter starts empty. Add your own data through admin. The email chapters (Ch42–Ch45) need your own Gmail settings in a `.env` file.

## Mistakes I made (so you don't have to)

- I deleted migration files after migrating, twice. Then Django said "no such column" because the database and the files didn't match anymore. If you change a model, just run `makemigrations` again.
- Many of my errors were indentation. If a method or a `return` is one level out, it isn't inside the class or function anymore.
- With many projects open in VS Code, auto-import sometimes picked a file from another chapter (`from Ch22 import student`). Check where the import comes from before pressing Enter.
- In `urls.py`, `name='home'` needs quotes. Without quotes it's the view function, not a name.
- Middleware runs top to bottom on the way in and bottom to top on the way out. If your middleware blocks pages, let `/admin/` through or you can't get back in to turn it off.
- `runserver` serves CSS for you. Uvicorn and Daphne don't, so the admin looks broken until you fix static files (Ch73–Ch74).
- With class-based views, check which class `urls.py` calls. I wrote `get_context_data()` in my own class, but the URL used the generic `TemplateView`, so my values never showed up. The URL has to point to `views.MyClass.as_view()`.
- A comma is easy to forget in `urls.py`: a missing one made Pylance say `"[" was not closed`. Also, options like `extra_context` go inside `as_view(...)`, not inside `path(...)`.
- In async views, normal ORM calls like `Student.objects.get()` fail. Use `aget()`, `acount()`, `async for`, or `sync_to_async`.
- In the earlier chapters I pushed `db.sqlite3` too. That was fine here because it only had practice data (dummy students and test users), but in a real project the database holds real users, so I stopped and added it to `.gitignore`. Do the same with `.env` files from day one.

## What I'm learning next

More class-based views (`ListView`, `DetailView` and the form and edit views), Django REST Framework, testing, and deploying a project.
