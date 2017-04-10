from businessObjects.libraries import Libraries

@auth.requires_login()
def index():
    filter = db.auth_user.company == auth.user.company
    libraries = Libraries().get_all_libraries_by_join_filter(db,filter)
    return  dict(libraries = libraries)