class myappRouter(object):
    """
    A router to control all database operations on models in
    the myapp application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on myapp models to 'my_db_2'
        """
        if model._meta.app_label == 'myapp':
            return 'yelp'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'myapp':
            return 'yelp'
        return None

    def allow_migrate(self, db, app_label, model_name=None,**hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label == 'yelp':
            return db == 'myapp_db'

        return None


