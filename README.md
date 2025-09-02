# Django Notes Aplcation 

To run the applcation create and shell into a virtual enviorment
Run the application using python manage.py run server

# Landing Page
See Notes button, takes you to all currently saved notes
Add a Note botton, takes you to gui to write and save note
Notes link on top left of  Navigation bar takes you to home page

# Notes Admin Area 
Admin gui for running CRUD operations accessed through localhost/admin

# APi
log/ returns a list of all notes by their titles.
makenote/ creates a note.
updatenote/<int:pk>/' updates a note. 
noteDelete/<int:id> deletes a note. 