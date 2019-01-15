class User:
    def __init__(self,user_id,firstname,last_name,other_names,email,phone_number,username,registered,isAdmin):
        self.user_id = user_id
        self.firstname = firstname
        self.last_name = last_name
        self.other_names = other_names
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.isAdmin = isAdmin
   
        
class Incident:
    def __init__(self,incident_id,created_on,created_by,type,location,status,Images,Videos,comment):
        self.incident_id=incident_id
        self.created_on=created_on
        self.created_by=created_by
        self.type=type
        self.location=location
        self.status=status
        self.Images=Images
        self.Videos=Videos
        self.comment=comment
        
    def get_incident(self):
        return{"incident_id":self.incident_id,
        "created_on":self.created_on,
        "created_by":self.created_by,
        "type": self.type,
        "status":self.status,
        "location": self.location,
        "Images":self.Images,
        "videos":self.Videos,
        "comment":self.comment}
        
