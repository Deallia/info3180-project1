from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = "Properties" 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    bedroomNo = db.Column(db.Integer)
    bathroomNo = db.Column(db.Numeric)
    location= db.Column(db.String(80))
    price = db.Column(db.String(128))
    type= db.Column(db.String(20))
    description = db.Column(db.String(500))
    photo=db.Column(db.String(80))

    def __init__(self,title,bedroomNo, bathroomNo, location, price, type, description, photo):
        self.title = title
        self.bedroomNo = bedroomNo
        self.bathroomNo = bathroomNo
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo
    
        

    # def is_authenticated(self):
    #     return True
    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)