from flask import Flask,request,jsonify,abort

from datetime import datetime
from api.models import User, Incident

app=Flask(__name__)
users=[]
Incidents=[]

@app.route('/api/v1/users', methods=['POST'])
def  register_incident(incident_id):
      #fetches all
      info=request.get_json()
      user_id=len(users)+1
      registered =datetime.now()
      user = User(user_id, info[firstname], info[last_name], info[other_names], info[email], info[phone_number], info[username], info[registered], info[isAdmin])
      users.append(user)
      return jsonify({"message":"the account is successfully created"}),201

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def fetch_user_details(user_id):
    fetched_user=[]
    user=users[user_id -1]
    fetched_user.append(user.get_user_details())
    return jsonify({"user":fetched_user}),200

@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def fetch_user(user_id):
    #this function enables user to delete his/her account
    if user_id==0 or user_id > len(users):
        return jsonify({"message":"Index out of range"}),400
    for user in users:
        if user in users:
            if user.user_id==user_id:
                users.remove(user)
    return jsonify({"message":"account successfully deleted"}),200

@app.route('/api/v1/incidents',methods=['POST'])
def  create_incident():
    #this function creates a new incident
    info=request.get_json()
    incident_id=len(Incidents)+1
    created_on = datetime.now
    incident=Incident(incident_id,created_on,info['created_by'],info['type'],info['location'],
                      info['status'],info['Images'],info['comment'])
    Incidents.append(incident)
    return jsonify({"message":"incident successfully created"}),201

@app.route('/api/v1/incidents',methods=['GET'])
def  fetch_incidents():
    #this function enables user to fetch all incidents
    incident = [incident.get_incident() for incident in Incidents]
    if incident:
        return jsonify({"message": Incidents}),200

@app.route('/api/v1/incidents/<incident_id>', methods=['GET'])
def  fetch_single_incident(incident_id):
    fetch_incident=[]
    incident= Incidents [incident_id -1]
    fetch_incident.append(incident.get_incident())
    return jsonify({"incident":fetch_incident}),200


@app.route('/api/v1/incidents/<incidents_id>', methods=['PUT'])
def  edit_incident(incident_id):
    #function for editing a single incident
    info =request.get_json()
    for incident in Incidents:
        if int(incident.incident_id) == int(incident_id):
            incident.type = info['type']
            incident.location=info['location']
            incident.status=info['status']
            incident.Images=info['images']
            incident.Videos=info['videos']
            incident.comment=info['comment']
            return jsonify({'message':"Successfully written"}), 200


    






