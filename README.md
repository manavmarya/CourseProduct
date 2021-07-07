# CourseProduct

CourseProduct is an DjangoRestFramework based CRUD platform with user authentication integrated.
https://floating-basin-54604.herokuapp.com/login/

## Features

### Creates two profiles - Staff & Non-staff

<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/register.png" width="500" style="margin:auto">

### CRUD operations 

#### Course Model has name, price, users_enrolled, creator, date_added as attributes
1. Users_enrolled : non-staff users can be added - ManyToMany relation
2. Creator would be automatically added -> Current User
3. Date stamp is also made

Operations    | URL
------------- | -------------
GET           | api/course/
POST          | api/course/
PUT/PATCH     | api/course/<id>
DELETE        | api/course/<id>

<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/course-post.png" width="500" style="margin:auto">
<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/course-result.png" width="500" style="margin:auto">
<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/course-delete.png" width="500" style="margin:auto">

#### WishList Model has course & creator as attributes
1. Course : selected from list of already posted courses [Displayed as Course_name--Creator_name]
2. Only one course can be added

Operations    | URL
------------- | -------------
GET           | api/wishlist/
POST          | api/wishlist/
PUT/PATCH     | api/wishlist/<id>
DELETE        | api/wishlist/<id>

<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/wishlist-result.png" width="500" style="margin:auto">
                                                                                                                    
#### User model also supports CRUD Api

1. at api/user

<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/wishlist-result.png" width="500" style="margin:auto">

2. login/ & register/ -> if user would be loggen in, it would be automatically redirected to api/

<img src="https://github.com/manavmarya/QuizApp/raw/master/static/images/add-user-edit.png" width="500" style="margin:auto">
<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/adduser-post.png" width="500" style="margin:auto">
<img src="https://github.com/manavmarya/CourseProduct/raw/master/static/images/add-user-result.png" width="500" style="margin:auto">

## Installation

#### Install all dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/)
```bash
pip install -r requirements.txt
```

