from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from webpage.models import Book, Author, Publisher, CATEGORY, GENRES

def add_book(request):
    #verify admin
    if not request.user.is_superuser:
        messages.error(request, "You are not admin!")
        redirect("_something_") # TODO: redirect to homepage (ยังไม่รู้ชื่อ)
    if request.method == "POST":
        category_ = request.POST["category"]
        same_category_books_id = [int(obj.id[2:]) for obj in Book.objects.filter(category=category_)] # cut out leading category number
        lastest_id = max(same_category_books_id) if len(same_category_books_id) else 0
        book_id = category_ + str(lastest_id + 1).zfill(4)
        # check author and publisher
        author = Author.objects.get_or_create(name=request.POST["author"])[0]
        author.book_count += 1
        author.save()
        publisher = Publisher.objects.get_or_create(name=request.POST["publisher"])[0]
        # add book to db
        Book.objects.create(
            id=book_id, name=request.POST["name"], author=author, publisher=publisher, category=category_, 
            genre=request.POST["genre"], quantity=request.POST["quantity"], description=request.POST["description"], image=request.FILES["image"])
        return redirect("add_book")

    # option for category, genre, author and publisher field
    category_list = ''
    for name in CATEGORY:
        category_list += (f'<option value="{name[0]}">' + name[1] + '</option>')
    genre_list = ''
    for name in GENRES:
        genre_list += (f'<option value="{name[0]}">' + name[1] + '</option>')   
    author_list = '<datalist id="author-list">'
    for name in [obj.name for obj in Author.objects.all()]:
        author_list += (f'<option value="{name}">' + name + '</option>')
    author_list += '</datalist>'
    publisher_list = '<datalist id="publisher-list">'
    for name in [obj.name for obj in Publisher.objects.all()]:
        publisher_list += (f'<option value="{name}">' + name + '</option>')
    publisher_list += '</datalist>'

    data = {"category_list":category_list, "genre_list":genre_list ,"author_list":author_list, "publisher_list":publisher_list}
    return render(request, "webpage/add_book.html", {"data":data})