class Libraries(object):

    def create(self,db,library):
        id = db.library.insert(name=library.name,description=library.description,user_id=library.user_id)
        return id

    def delete(self,db,library):
        id = db(db.library.id==library.id).delete()
        return id

    def update(self,db,library):
        values = {}
        if library.name is not None:
            values.update({"name": library.name})
        if library.description is not None:
            values.update({"description": library.description})
        if library.user_id is not None:
            values.update({"user_id": library.user_id})
        library = db(db.library.id == library.id).update(**values)
        return library

    def get_library_by_filter(self,db,filter):
        library = db(filter).select().first()
        return  library

    def get_all_libraries_by_filter(self, db, filter):
        libraries = db(filter).select(db.library.ALL)
        return libraries

    def get_all_libraries(self, db):
        libraries = db().select(db.library.ALL)
        return libraries

    def get_all_libraries_by_join_filter(self,db,filter):
        libraries = db(filter).select(db.library.ALL,join=db.library.on(db.auth_user.id == db.library.user_id))
        return libraries