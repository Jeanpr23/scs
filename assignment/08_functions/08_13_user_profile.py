# 08_13_user_profile.py

def build_profile(first, last, **info):
    """Builds a dictionary with user information."""
    profile = {
        "first_name": first,
        "last_name": last
    }
    profile.update(info)
    return profile

user = build_profile("Jean", "Rivera", location="New Jersey", field="Anthropology")

print(user)