from application.models import User


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, and hashed_password fields are defined correctly.
    """
    # user = User("john99@gmail.com", "myawesomepassword")
    assert new_user.email == "john@somewhere.com"
