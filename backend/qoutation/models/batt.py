from typing import List
from  ....main import db
from datetime import datetime





class Batt(db.Model):

    __tablename__="batt"


    id           = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    batt_name= db.Column(db.String(50) ,unique=True)
    battv= db.Column(db.Integer,)
    dod = db.Column(db.Float)
    ah=db.Column(db.Integer,)
    losses = db.Column(db.Float)
    nreff = db.Column(db.Float)
    
    # voc= db.Column(db.Integer,)
    # isc= db.Column(db.Integer)
    # tcoeff= db.Column(db.Integer)
    # fman=db.Column(db.Integer)
    # vcoeff= db.Column(db.Integer)
    # date_added     = db.Column(db.DateTime(),default=datetime.utcnow )

    def __init__(self,batt_name, battv,ah,dod,nreff,losses):
        self.battv = battv
        self.batt_name=batt_name
        self.ah = ah
        self.dod= dod
        self.nreff = nreff
        self.losses =losses
        # self.vmp= vmp
        # self.date_added=date_added
        
        
    
    

    def __repr__(self):
        return 'Batt(name=%s)' % self.name

    def json(self):
        return {'name': self.name, }   

    @classmethod
    def find_by_name(cls, name) -> "Batt":
        return cls.query.filter_by(name = name).first() 

    @classmethod
    def find_by_id(cls, _id) -> "Batt":
        return cls.query.filter_by(id=_id).first() 
    
    @classmethod
    def find_all(cls) -> List["Batt"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()












