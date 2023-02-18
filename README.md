# Registrar Project
This is the web framework for our registrar project. This is the main part of our project and most work will be submitted to this repo.

To start the server run

    $ python3 manage.py runserver

and navigate to http://127.0.0.1:8000.

Likewise to reach the form index page, go to http://127.0.0.1:8000/forms.

To go to a template of the Drop/Add Class Page, go to http://127.0.0.1:8000/forms/addDropClass

Right now, information is sent in through the context object in forms/view.py.
Eventually this will be updated to receive information through the database.

Joe is currently working on a form builder which will speed up the process of the form development. To see the progress on this form builder, visit https://joebieker.com/formBuilder

# Progress
Progress Made:
- emails outlined
- home page created

# Views and URLs

### Views

To add a new web page, you first must build out the html template and put it in the forms/templates
Next you'll need to add the view to forms/views.py. For example, for a page named dropClass.html, you would have the following code

    $ def dropClass(request):
    $ context = {
    $     fname = 'first_name'
    $ }
    $ return render(request, 'dropClass.html',context)

The context parameter specifies any information that needs to be sent to the page. In the html this would be inputed as

    $ <p>{{ fname }}</p>

This would then show the fname property of the context object. 

### URLs

To add the url of the dropClass.html page, navigate to forms/urls.py. Within the urlpatterns list, you would need to add the path.

For the dropClass.html file we created, that would look like this.

    $ path('dropClass', views.dropClass, name='dropClass')

The first parameter tells us the extension of the page. So we can find this page at http://...forms/dropClass

The second parameter tells the script which view to load. This is what we did earlier in the views.py section.

The last parameter is just the name of the path.