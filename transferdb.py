from google.appengine.ext import ndb

class Name(ndb.Model):
	first_name     = ndb.StringProperty(required = True)
	middle_name    = ndb.StringProperty(default = "")
	last_name      = ndb.StringProperty(required = True)
	lower_first    = ndb.ComputedProperty(lambda self: self.first_name.lower())
	lower_last     = ndb.ComputedProperty(lambda self: self.last_name.lower())

STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class Address(ndb.Model):
	address_line_1 = ndb.StringProperty(required = True)
	address_line_2 = ndb.StringProperty(default = "")
	city           = ndb.StringProperty(required = True)
	zipcode        = ndb.StringProperty(required = True)
	state          = ndb.StringProperty(required = True, choices = STATES)

def arrayToString( a ):
	s = ''
	for i in range(len(a)-1):
		s += str(a[i]) + ", "
	s += "and " + str(a[-1])

class Tutor(ndb.Model):
	name         = ndb.StructuredProperty(Name, required = True)
	age          = ndb.IntegerProperty(required = True)
	email        = ndb.StringProperty(required = True)
	phone        = ndb.StringProperty(required = False)
	address      = ndb.StructuredProperty(Address, required = True)
	school       = ndb.StringProperty(required = False)
	offerings    = ndb.StringProperty(repeated = False)
	will_travel  = ndb.BooleanProperty(default = False)
	hourly_rates = ndb.IntegerProperty(required = False)
	bio       = ndb.TextProperty(default = 
		self.name.first_name + " " + self.name.last_name + " is a tutor from " + 
		self.address.city + ", " + self.address.state + " who teaches " + 
		arrayToString( offerings ) + ".")

class Student(ndb.Model):
	name         = ndb.StructuredProperty(Name, required = True)
	age          = ndb.IntegerProperty(required = True)
	email        = ndb.StringProperty(required = True)
	phone        = ndb.StringProperty(required = False)
	address      = ndb.StructuredProperty(Address, required = False)
	school       = ndb.StringProperty(required = False)