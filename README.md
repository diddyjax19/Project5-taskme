# The Task ME - API
The TaskME is a Task platform for the modern world. The project manager can create Projects on this platform and assign them to different user.You can view all the tasks and projects and see who dey are assigned to from the Project managers End. In this app you can also see deadlines of the Current Projects ,thier start date of the projects and it end date.Each User is restricted to see the Tasks assigned to them and get more details about each project.This section of the project is the backend API database built to support the ReactJS frontend, and it is powered by the Django Rest Framework.

#### DEPLOYED BACKEND API RENDER [LINK](https://taskit.herokuapp.com/)
#### DEPLOYED FRONTEND RENDER [LINK - LIVE SITE]()
#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/diddyjax19/Taskit-FrontEnd)

## Table of Contents
+ [User Stories](#user-stories "User Stories")
+ [Database](#database "Database")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## User Stories:
All User Stories have been documented in their own file, the link for which can be found [HERE](backend/static/userstories.md).

I have included links to the [GitHub Issues](https://github.com/CluelessBiker/project5-red-crayon/issues) for this project, as well as the [KANBAN board](https://github.com/users/CluelessBiker/projects/2).

## Database:
![SQL Database model](/static/images-readme/readme-models.png)

## Testing:
### Validator Testing: 
All files passed through [PEP8](http://pep8online.com/) without error.

![PEP8](/static/images-readme/readme-pep8.png)

### Manual Testing:
1. Manually verified each url path created works & opens without error.
2. Verified that the CRUD functionality is available in each app via the development version: Create Project, Create Task, Create USers, Assign Tasks, Assign Date and time.
 - Checked this by going to each link.
 - Creating a new user.
 - User Login
 - Creating Project with all details.
 - Creating Tasks with all details.
 - Assiging Tasks to the appropraite User.
 - Creating Project Date and time
 - Creating Project Status.
2. - Made sure that each user are not able to see the projects thhatthey are not assigned or are not working on .
```- Ran migrations file.
 - deleted `0001_initial.py` files & `__pycache__` from the migration folders in all apps.
 - Ran the migration commands again:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
 - created a new super user to test functionality
```
python3 manage.py createsuperuser
```
 - upon returning to the development version of the app, we were now unable to login or create a new user
 - clearing the browser cookies & cache, as well as relaunching the gitpod workspace resolved this.

### Unfixed Bugs
- None so far.

## Technologies Used:
### Main Languages Used:
- Python

### Frameworks, Libraries & Programs Used:
- Django
- Django RestFramework
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers
- DrawSQL: An interactive ERD platform that allows you to set up your database tables, & build the connections between them for a visual layout.

## Deployment:
### Project creation:
1. Create the GitHub repository.
2. Create the project app on [Heroku](heroku.com).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:
```
'django<4'
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```
5. Created the Django project with the following command:
```
django-admin startproject project_name .
```
6. Navigated back to [Heroku](heroku.com), and under the Settings tab, added the following configvars:
 - Key: SECRET_KEY | Value: hidden
 - Key: CLOUDINARY_URL | Value: cloudinary://hidden
 - Key: DISABLE_COLLECTSTATIC | Value: 1
 - Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com
7. Add two additional configvars once the ReactApp has been created:
 - Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
 - Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
  - Check that the trailing slash `\` at the end of both links has been removed.
  - Gitpod occasionally updates the browser preview link. Should this occur, the CLIENT_ORIGIN_DEV value shall need to be updated.

9. Add the following to INSTALLED_APPS to support the newly installed packages:
```
 'rest_framework',
  'rest_framework.authtoken'
  'home',
  'api',
  'api.users',
  'api.tasks',
  'api.projects'
'corsheaders',
```
10. Import the database, the regular expression module & the env.py
```
import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env
```



MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```
- Below INSTALLED_APPS, set site ID:
```
SITE_ID = 1
```
12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```
13. Set the default renderer to JSON:
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```
14. Beneath that, added the following:
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```
15. Then added:
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```
16. Updated DEBUG variable to:
```
DEBUG = 'False'
```
17. Updated the DATABASES variable to:
```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```
18. Added the Heroku app to the ALLOWED_HOSTS variable:
```
os.environ.get('ALLOWED_HOST'),
'localhost',
```
19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):
```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
20. Also added to the top of MIDDLEWARE:
```
'corsheaders.middleware.CorsMiddleware',
```
- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:
```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```
- In addition, Johan also suggested to add the following import statement at the top of the settings.py file:
```
from corsheaders.defaults import default_headers, default_methods
```

### Final requirements:
21. Created a Procfile, & added the following two lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```
22. Migrated the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
23. Froze requirements:
```
pip3 freeze --local > requirements.txt
```
24. Added, committed & pushed the changes to GitHub
25. Navigated back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
26. Deployed the branch.

### Deploy to Render & ElephantSQL:
* Due to Heroku revoking their frie tier access, the project has been redeployed using (Render)[https://render.com/] & (ElephantSQL)[https://www.elephantsql.com/] using the following [instructions](https://code-institute-students.github.io/deployment-docs/41-pp5-adv-fe/pp5-adv-fe-drf-01-create-a-database)

## CREDITS:

### Content:
- The creation of this API database was provided through the step by step guide of the C.I. DRF-API walkthrough project.
- All classes & functions have been credited.
- Modifications have been made to the 'Profiles' & 'Posts' app models, and an additional two apps along with models, serializers & views have been created by me.
- Oisin from Tutor support went above & beyond to assist me in resolving an issue with my database that prevented new posts from being created. The steps we took have been documented in point #5 of the Manual Testing section.

### Media:
- Default post image Photo by Artem Podrez from [Pexels](https://www.pexels.com/photo/image-of-a-whale-made-of-scrap-materials-7048043/)
- Default profile image from [Favicon](https://favicon.io/emoji-favicons/alien-monster)
