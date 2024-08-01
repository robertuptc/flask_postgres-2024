from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Students(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def to_dictionary(self):
        return {
            "id":self.id,
            "first_name":self.first_name,
            "last_name":self.last_name,
            "age":self.age,
            "grade":self.grade,
        }