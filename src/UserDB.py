# Define the user model
class User(models.BaseUser):
    username: str
    email: str
    password: str
    date_of_birth: date
    first_name: str
    last_name: str
    gender: str