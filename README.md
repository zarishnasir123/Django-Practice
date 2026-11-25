# Django Practice

Hi, I'm Zarish. This repo is where I learned Django, one chapter at a time, from October to November 2026.

Every `ChNN` folder is a small separate project for one topic. I wrote the code, ran it, got errors, fixed them, and committed. So the code here is learner code: you'll find commented-out lines where I tried something one way and then another. I left them in on purpose, because that's how I understood things.

If you're learning Django too, feel free to go through it in the same order. I've written some notes at the end that I wish someone had told me earlier.

## How the folders work

- Each chapter has its own project and its own virtual environment, so breaking one chapter never broke the others.
- Chapters build on each other, so the order below is the order I'd recommend.
- From Ch56 onwards I used the same 10 students (same names, cities and marks) in every database chapter, so it's easy to compare what each query returns.
- The generic class-based view chapters (Ch80–Ch86) use a small `Student` model again (name plus roll, course, email or password), so the views are easy to compare.
- `Bistro`, `BookReview`, `BookReviewCBV` and `underconst` are small projects where I put things together.

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

Ch42–Ch45 are all function-based views. I did the same idea again with class-based views in Ch87–Ch90 (see below).

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

### Class-based views (Ch77–Ch86)

- **Ch77:** My first class-based views with the base `View` class. I wrote the same pages (home, about, contact with a form, news) first as function views, then as classes with `get()` and `post()`, and connected them with `.as_view()`. The contact form shows a thank-you page after a valid submit. One `NewsView` class serves two templates by changing `template_name` in `as_view()`.
- **Ch78:** `TemplateView`: `template_name`, sending data with `get_context_data()` (and why `super()` comes first), `extra_context`, and URL values arriving in `kwargs`. Pages like home, about, contact and profile, some with their own class and some with `TemplateView` straight in `urls.py`.
- **Ch79:** `RedirectView`: redirecting to a fixed `url`, to a URL name with `pattern_name`, temporary (302) vs `permanent=True` (301), carrying URL values over, keeping `?q=` with `query_string=True`, and working out the address in `get_redirect_url()`.
- **Ch80:** The first generic view, `ListView`. With only `model = Student` it already finds the rows and the template (`myapp/student_list.html`). Then I changed it step by step: `template_name`, `template_name_suffix`, `ordering`, `context_object_name`, `get_queryset()` to keep only some rows, `get_context_data()` to send a second list, and `get_template_names()` to pick the template from a cookie (I set it from the browser console with `document.cookie = "user=Umar"`).
- **Ch81:** `DetailView`: shows one row, and the `pk` comes from the URL (`<int:pk>`). Also `pk_url_kwarg` (when the URL calls it `id`) and `template_name_suffix` (`_info` instead of `_detail`).
- **Ch82:** `FormView` with a contact form: `form_class`, `template_name`, `success_url`, `initial`, `form_valid()` (where I save the data into a `Contact` model), `form_invalid()` and `get_context_data()`.
- **Ch83:** `CreateView`: `model` and `fields`, or a `ModelForm` as `form_class` with Bootstrap classes in `widgets`. After saving it goes to `success_url` or to the model's `get_absolute_url()`.
- **Ch84:** `UpdateView`: the same form template as create, filled with the row found by `pk`. A password box is empty by default, so I used `render_value=True` for it.
- **Ch85:** `DeleteView`: a GET shows the "are you sure?" page (`student_confirm_delete.html`) and a POST deletes the row. It needs a `success_url`, written with `reverse_lazy`, because the row is gone and there is nothing to go back to.
- **Ch86:** A CRUD project with all five generic views on one `Student` model (name, email, roll): list, detail, add, edit and delete, with one `student_form.html` shared by add and edit, and a `base.html` with Bootstrap.

### Authentication with class-based views (Ch87–Ch90)

- **Ch87:** The Ch42 idea again, but with class-based views and less code, in three apps (`accounts`, `customer`, `seller`):
  - a custom user model built from `AbstractBaseUser`, with my own `BaseUserManager` (`create_user` and `create_superuser`), the `has_perm` and `has_module_perms` methods the admin asks for, and two extra fields, `is_customer` and `is_seller`, set with `AUTH_USER_MODEL`
  - customer and seller sign up with `CreateView` and a `UserCreationForm`, and each kind of user goes to their own dashboard after login
  - login with the **email** (`USERNAME_FIELD = 'email'`), and `LogoutView` (logout has to be a POST)
  - change password with the old password (`PasswordChangeView`) and forgot password by email (`PasswordResetView` and the three pages after it), with an HTML email card
  - Gmail settings read from a `.env` file with `python-dotenv`; without the file the emails are printed in the terminal instead
  - I left the login rules (mixins) out in this chapter, so the dashboards are open to anyone who knows the address. Ch88 fixes that.
- **Ch88:** Ch87 again (same three apps, with a fresh database) with mixins that restrict each dashboard to one role:
  - `CustomerRequiredMixin` and `SellerRequiredMixin` in `accounts/mixins.py`. Each one combines `LoginRequiredMixin` with `UserPassesTestMixin`, whose `test_func()` checks `is_customer` or `is_seller`
  - the mixin is written before the view (`class CustomerDashboardView(CustomerRequiredMixin, TemplateView)`), so the login is checked first and the role second
  - a visitor who isn't logged in is sent to the login page; a logged in user with the wrong role gets a 403 page (my own `403.html`) with a button back to their own dashboard
- **Ch89:** Ch88 again, but now the two roles have something to do: products. Sellers get their own pages to add, edit and delete products, and they only ever see their own. If a seller types the address of somebody else's product, they get a 404. Customers get a small shop window where they can browse all the products and open one.
  - the rules come from permissions I give in code: customers can only view products, sellers can view, add, change and delete. The views check them with `PermissionRequiredMixin` and `permission_required`
  - my user model doesn't use `PermissionsMixin`, so I wrote `has_perm()` and `has_perms()` myself
  - the navbar uses `perms` in the template to hide links that a person isn't allowed to use
- **Ch90:** The same role rules as Ch88 (no products this time), but written as decorators instead of mixins. I wrote `customer_required`, `seller_required` and `anonymous_required` in `accounts/decorators.py`.
  - a decorator made for a function can't go straight on a method of a class, so I used `method_decorator`. On the class I put it on `dispatch`, because every request goes through `dispatch()` first, so one line covers `get()` and `post()` together
  - I tried stacking two decorators, giving them as a list, and putting `never_cache` on just one method (the home page `get()`), so the back button doesn't show a logged in page after logout
  - the sign up pages use `anonymous_required`: if you're already logged in, you're sent home instead of seeing the form

### Built-in authentication (Ch91–Ch92)

Django already comes with the views for login, logout and passwords, so in these two chapters I just used them. There's no custom user model, only the normal `User`.

- **Ch91:** I added `django.contrib.auth.urls` to the project's `urls.py`, and that gave me login, logout and the password pages. I made an app called `registration` for my own templates, because the built-in views look for them in a folder called `registration/`. I wrote the login, profile and change password templates. The profile page is where Django sends you after login by default (`/accounts/profile/`). It has a logout button, and that has to be a small POST form, because logout doesn't work with a normal link.
- **Ch92:** The same idea, but this time I wrote the views in my own `urls.py` and gave each one a `template_name`, so my templates can have any name I like (`myapp/login.html`, `password_change.html` and so on).
  - `LoginView`, `LogoutView`, `PasswordChangeView` and `PasswordChangeDoneView` with `.as_view(template_name=...)`
  - a dashboard that needs a login (a `TemplateView` wrapped in `login_required`) with the user's details, a "Change password" button and a logout button
  - `LOGIN_URL`, `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` in `settings.py`: where a visitor is sent to log in, where you land after logging in, and where you land after logging out
  - I also made a `logout.html` page, but it only shows when `LOGOUT_REDIRECT_URL` isn't set. While it is set, logout goes straight to the login page.

### Async class-based views (Ch93)

- **Ch93:** The Ch71 idea again, but with class-based views and run with Uvicorn (`uvicorn Ch93.asgi:application --reload`). Both views call a free API 5 times. `SyncView` uses `requests` and asks one call after another, so it took about 5.4 seconds. `AsyncView` uses `httpx` and `asyncio.gather` to ask all 5 together, so it took about 1.2 seconds. One rule to remember: all the methods in one view class must be the same kind, either all `def` or all `async def`.

### Login required middleware (Ch94)

- **Ch94:** A middleware that makes every page need a login, so none of the views needs `@login_required` or `LoginRequiredMixin`. I wrote it as a class in `myapp/middleware.py`.
  - the important part is the `process_view()` method. Django calls it after it has found which view will answer, so the middleware can look at that view before it runs
  - it asks two questions: is this view marked as open, and is the user logged in? If the answer to both is no, the visitor is sent to the login page with `?next=`, so they come back to the page they wanted after logging in
  - I mark the open pages with `@login_not_required` (on a class it goes on `dispatch` with `method_decorator`, like in Ch90). Django's own login view already has it, so the login page doesn't lock itself out
  - the middleware has to be listed below `AuthenticationMiddleware` in `MIDDLEWARE`, because it needs `request.user`
  - Django also has a ready-made `LoginRequiredMiddleware` that works the same way, with the same decorator

### URL namespaces (Ch95)

- **Ch95:** Three apps in one project (`core`, `customer`, `seller`) to see why URL namespaces exist. `customer` and `seller` both have a page called `dashboard`, and if the names were plain, `{% url 'dashboard' %}` couldn't tell which one I mean (it quietly picks the last one in the list).
  - the fix is one line in each app's `urls.py`: `app_name = 'customer'` and `app_name = 'seller'`. That is the namespace of the app
  - after that I write `{% url 'customer:dashboard' %}` and `{% url 'seller:dashboard' %}`: the namespace, a colon, then the name. A plain `reverse('dashboard')` now fails with `NoReverseMatch`
  - `core` has no `app_name`, so its home page is still just `{% url 'home' %}`
  - the home page links to both dashboards and to the customer profile, and each page prints `request.resolver_match.namespace` and `.view_name`, so it shows which namespace answered

### reverse and reverse_lazy (Ch96)

- **Ch96:** In templates I already use `{% url 'name' %}` to get an address from its name. `reverse()` does the same thing inside Python code, so a view doesn't need the address typed in.
  - in the function views, `reverse('home')` gives `/home/`, and `reverse('product', kwargs={'pk': pk})` gives `/product/5/` (the values for the address go in `kwargs`)
  - the class-based views use `reverse_lazy()`. It gives the same result, but it waits until the address is really needed. That matters when it is written at the top of a class (like `success_url = reverse_lazy('home')`), because the URLs are not loaded yet when Python reads the class
  - the names used are the `name=` values in `urls.py`, so if I change an address there, nothing else breaks

### JSON responses (Ch97)

- **Ch97:** Sending JSON instead of HTML with `JsonResponse`, with a `Product` model (name and price) and 8 dummy products.
  - a dictionary becomes JSON by itself, and `Content-Type: application/json` is set for me
  - a QuerySet can't be sent, so I use `list(Product.objects.values(...))`. A list (not a dictionary) needs `safe=False`, or Django raises `TypeError`
  - a missing product gives `{"error": "Product not found"}` with `status=404`. I used `filter(pk=pk).first()` and an `if`, so there is no `try`/`except`
  - `status=201`, my own header (`response['X-Student-Note'] = ...`) and `json_dumps_params={'indent': 4}` for readable output
  - a `Decimal` price is sent as text (`"899.99"`, with quotes)
  - the same list and detail pages as function views and as class-based views

### CRUD API with AJAX (Ch98)

- **Ch98:** A product page that creates, reads, updates and deletes products without reloading, by talking to a JSON API with `fetch`. I used the `Product` model again, and the page is one `home` view with `base.html` (Bootstrap), `home.html` and `static/myapp/js/script.js`.
  - the API has two views: `ProductAPI` (`get` for the list, `post` to create) and `ProductDetailAPI` (`get`, `put` and `delete` for one product, with the `pk` in the address)
  - the data arrives as JSON text in `request.body`, so I use `json.loads()` and give it to a `ModelForm`. That is the same validation as a normal form: name at least 3 characters and not used by another product, price above 0. A wrong form answers with the errors and `status=400`, and the page writes them under the inputs
  - for an update the form gets `instance=product`, so it changes the row instead of making a new one (and the product's own name doesn't count as a duplicate)
  - in JavaScript: `fetch` with `async` / `await`, `response.ok`, `response.json()`, `JSON.stringify()` and `method: 'POST'`, `'PUT'` or `'DELETE'`
  - the csrf token is read from the hidden input and sent in the `X-CSRFToken` header. Without it Django answers 403
  - the table is filled by JavaScript, with buttons for View (a Bootstrap popup), Edit (fills the form, and the button says "Update") and Delete (asks first). One click listener on the table body handles all of them, because the buttons are made again each time
  - names are written with `escapeHtml()`, so a name like `<b>hi</b>` shows as text

### annotate with related_name (Ch99)

- **Ch99:** `annotate()` across a ForeignKey, with an `Author` and a `Book` (title, author, price, discount) and dummy data: 5 authors and 10 books, one author with no books on purpose. In `Book` the key has `related_name='books'`, and that name is how an `Author` query reaches the books.
  - `Author.objects.annotate(book_count=Count('books'))`, ordered with `order_by('-book_count')`, and filtered on the new name (`filter(book_count__gt=1)`, `filter(book_count=0)`)
  - several at once: `Sum`, `Avg`, `Min` and `Max` of `'books__price'` (two underscores to reach a field of the books)
  - `Count('books', filter=Q(books__discount__gt=0))` counts only the books that match
  - `filter(books__price__gt=12).distinct()` finds authors by their books, and `distinct()` stops an author from showing up once for every matching book
  - the other direction, `author.books.all()`, with `prefetch_related('books')` so the loop doesn't ask the database again for every author
  - an author without books gets `0` from `Count` but `None` from `Sum` and `Avg`

## Small projects

- **Bistro:** a restaurant website with Tailwind CSS.
- **BookReview:** books and reviews. You have to log in to write a review, and you can filter books by genre. I made it to practise everything up to the forms chapters.
- **BookReviewCBV:** the same book idea again, rebuilt with class-based views after Ch77–Ch79. It has a book library with:
  - list, detail, add, edit and delete pages, all class-based views built on `TemplateView` with `get_context_data()` (the delete page asks first, and only a POST really deletes)
  - **filters** on the list: search in the title or author (a `Q` object), genre, minimum rating and sorting. The choices are in the address (`/?genre=technology&min_rating=4`), and unknown values are ignored
  - **cover images**: an `ImageField` with uploads (`MEDIA_ROOT`, `request.FILES`, `enctype="multipart/form-data"`, needs Pillow). Books without a cover show a coloured block with their first letter
  - **messages** ("Book added", "Book deleted") stored in the session and shown as Bootstrap alerts, plus a "Recently viewed" list kept in the session
  - **RedirectView**: `/latest/` and `/random/` send you to a book, and the old `/books/` address redirects (301) to the list
  - a Bootstrap 5 design with star ratings, cards and icons, and Bootstrap classes added to the form fields from `forms.py`
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

A few chapters have a `requirements.txt`. Later chapters need an extra package; if you get `ModuleNotFoundError`, install the missing one (for example `python-decouple`, `python-dotenv`, `uvicorn`, `daphne`, `httpx`, `requests`, `whitenoise` or `pillow`).

For the async chapters, run the server with Uvicorn instead, for example `uvicorn Ch75.asgi:application --reload`.

The databases aren't in the repo anymore (older commits still have them, but those were only practice data), so every chapter starts empty. Add your own data through admin. The email chapters (Ch42–Ch45 and Ch87–Ch90) need your own Gmail address and App Password in a `.env` file (`GMAIL_ADDRESS` and `GMAIL_APP_PASSWORD`). Without it, Ch87–Ch90 print the emails in the terminal.

## Mistakes I made (so you don't have to)

- I deleted migration files after migrating, twice. Then Django said "no such column" because the database and the files didn't match anymore. If you change a model, just run `makemigrations` again.
- Many of my errors were indentation. If a method or a `return` is one level out, it isn't inside the class or function anymore.
- With many projects open in VS Code, auto-import sometimes picked a file from another chapter (`from Ch22 import student`). Check where the import comes from before pressing Enter.
- In `urls.py`, `name='home'` needs quotes. Without quotes it's the view function, not a name.
- Middleware runs top to bottom on the way in and bottom to top on the way out. If your middleware blocks pages, let `/admin/` through or you can't get back in to turn it off.
- `runserver` serves CSS for you. Uvicorn and Daphne don't, so the admin looks broken until you fix static files (Ch73–Ch74).
- With class-based views, check which class `urls.py` calls. I wrote `get_context_data()` in my own class, but the URL used the generic `TemplateView`, so my values never showed up. The URL has to point to `views.MyClass.as_view()`.
- A comma is easy to forget in `urls.py`: a missing one made Pylance say `"[" was not closed`. Also, options like `extra_context` go inside `as_view(...)`, not inside `path(...)`.
- The plain `View` class has no `get_context_data()`. That method comes with `TemplateView` (or `ContextMixin`), so use one of those when you want it.
- An `ImageField` needs Pillow installed, and deleting a book row doesn't delete its image file. Remove the file yourself in the delete view, and keep the `media` folder out of Git.
- Tailwind IntelliSense told me to change `flex-grow-1` to `grow` in a Bootstrap page. Bootstrap doesn't have `grow`, so I left it. Editor hints are for one framework only.
- In async views, normal ORM calls like `Student.objects.get()` fail. Use `aget()`, `acount()`, `async for`, or `sync_to_async`.
- `form_class` needs the class, not an object: `form_class = ContactForm`. With brackets I got `'ContactForm' object is not callable`, because Django makes the form itself.
- A `TemplateView` used straight in `urls.py` still needs `template_name`. I forgot it on my thank-you page and got "TemplateResponseMixin requires either a definition of 'template_name'".
- When I overrode `get_form()` I forgot `return form` at the end, so the page showed no fields.
- In Ch87 I typed my email into the login box, but Django's login form asks for the username. To log in with the email, the user model has to use it as its `USERNAME_FIELD` (a small authentication backend also works, but I ended up building the user from `AbstractBaseUser`).
- Decide the custom user model before the first `migrate`. In Ch87 I changed it twice. The first time the database had no users, so I just started again. The second time it had users, so I tested the migration on a copy of the database first.
- A decorator I wrote for a function view can't go straight on a method of a class, because the method receives `self` first. Use `@method_decorator(my_decorator, name='dispatch')` on the class (Ch90). Putting it on `dispatch` covers `get()` and `post()` together.
- Django's admin has its own templates in a `registration/` folder too, for example `password_change_form.html`. If my app has a file with the same name, whichever app is listed first in `INSTALLED_APPS` wins, so my `registration` app had to go above `django.contrib.admin` (Ch91). Giving my templates their own folder name, like `myapp/`, avoids the problem (Ch92).
- Async doesn't speed up separate requests. Under Uvicorn, Django already gives every sync request its own thread, so three sync requests at once took the same time as three async ones. Async helps inside one view that has to wait for many things, like the 5 API calls in Ch93.
- If a middleware uses `request.user`, it has to be listed below `AuthenticationMiddleware`. Above it, `request.user` doesn't exist yet and the pages crash (Ch94).
- Two apps with the same url name (like `dashboard`) is not an error, and that's the problem: `{% url 'dashboard' %}` quietly gives you the last one in `urlpatterns` (the seller page), so a customer link would open the seller's page. Add `app_name` to each app's `urls.py` and use `{% url 'customer:dashboard' %}` (Ch95).
- In a view I wrote `def get(self, request, **args, **kwargs)` and Pylance said "Only one `**` parameter allowed". It's `*args, **kwargs`: one star collects the extra values in a tuple, two stars collect the named ones in a dictionary (Ch96).
- `JsonResponse([...])` with a list raises `TypeError` unless you add `safe=False`. Wrapping the list in a dictionary (`{'products': [...]}`) also works (Ch97).
- Keep the trailing slash the same in `urls.py` and in JavaScript. My path was `api/products/` but the script used `/api/products`, so Django had to redirect every request, and a POST can't be redirected. Also, `fetch` with POST, PUT or DELETE needs the csrf token in the `X-CSRFToken` header (Ch98).
- A sum of decimals in SQLite can show extra digits (`43.9900000000000`). Format money with `:.2f` when showing it (Ch99).
- In the earlier chapters I pushed `db.sqlite3` too. That was fine here because it only had practice data (dummy students and test users), but in a real project the database holds real users, so I stopped and added it to `.gitignore`. Do the same with `.env` files from day one.

## What I'm learning next

Redoing BookReviewCBV with the generic class-based views (`ListView`, `DetailView`, `CreateView`, `UpdateView` and `DeleteView`) to use even less code, Django REST Framework, testing, and deploying a project.
