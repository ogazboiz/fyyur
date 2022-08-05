#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
from email.headerregistry import Address
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from app import db
from flask_migrate import Migrate

class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    genres = db.Column(ARRAY(String)) # list = [clasical, Jazz]
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    # TODO: (completed) implement any missing fields, as a database migration using Flask-Migrate
    address = db.Column(db.String(400))
    seeking_description = db.Column(db.String(400))
    seeking_talent = db.Column(Boolean, default=False)
    showes = db.relationship('Show', backref='venue_list', lazy=True)

    def __repr__(self) -> str:
        return f"<Venue: id({self.id}, name({self.name}))>"

            
    def detail(self):
        return{
            'id' :self.id,
            'name' :self.name,
            'genres' : self.genres,
            'address' :self.address,
            'city': self.city,
            'state':self.state,
            'phone' :self.phone,
            'website_link' :self.website_link,
            'facebook_link':self.facebook_link,
            'seeking_talent' :self.seeking_talent,
            'description' :self.seeking_description,
            'image_link' :self.image_link
        }
        
    def short(self):
        return{
            'id':self.id,
            'name':self.name,
        }
    


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(ARRAY(String))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(300))
    seeking_description = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    showes = db.relationship('Show', backref='artist_list', lazy=True)

    def __repr__(self) -> str:
        return f"<Artist: id({self.id}, name({self.name})>"

    # def details(self):
    #     return{
    #         'id': self.id,
    #         'name': self.name,
    #         'genres': self.genres,
    #         'city': self.city,
    #         'state':self.state,
    #         'phone': self.phone,
    #         'website_link': self.website_link,
    #         'facebook_link': self.facebook_link,
    #         'seeking_venue': self.seeking_venue,
    #         'seeking_description': self.seeking_description,
    #         'image_link': self.image_link,

    #     }

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def short(self):
        return{
            'id':self.id,
            'name':self.name,
        }
    

# TODO (completed) Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)


    def detail(self):
        venue = Venue.query.get(self.venue_id)
        artist = Artist.query.get(self.artist_id)
        return{
            'venue_id' : venue.id,
            'venue_name' : venue.name,
            'artist_id' : artist.id,
            'artist_name' : artist.name,
            'artist_image_link' :artist.image_link,
            'start_time' :str(self.start_time)
        }

    # def venue_details(self):
    #     return{
    #         'venue_id' :self.venue_id,
    #         'venue_name' :self.venues.name,
    #         'venue_image_link' :self.venues.image_link,
    #         'start_time' :self.start_time
            
    #     }

    # def artist_details(self):
    #     return{
    #         'artist_id' :self.venue_id,
    #         'artist_name' :self.Artist.name,
    #         'artist_image_link' :self.Artist.image_link,
    #         'start_time' :self.start_time

    #     }
