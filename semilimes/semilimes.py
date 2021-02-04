def SendTxtMsg(AuthToken, ReceiverID, dest_type, Body):
  TypeID = "590E4E6C-2C5D-47E8-8F38-311D5A299EE7"
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", "
  wsmsg += "\"Type\": \"chat\", "
  wsmsg += "\"TypeID\": \"" + TypeID + "\", "
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", " #send msg to a User ID
  else: 
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", " #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\"}"

  return wsmsg

def SendSelectOpt(AuthToken, ReceiverID, dest_type, Body, Options_list): # [["Option1",val1],["Option2",...]
  TypeID = "4DB40F80-4C25-454B-BDB4-330A05285D71"
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", "
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", "
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", " #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", " #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\", "
  wsmsg += "\"Layout\": \"flexible\", "
  wsmsg += "\"Options\": [ ";
  for i in range(len(Options_list)-1):
    wsmsg += "{\"Text\": \"" + str(Options_list[i][0]) + "\", \"Value\": \"" + str(Options_list[i][1]) + "\"},"
  wsmsg += "{\"Text\": \"" + str(Options_list[i+1][0]) + "\", \"Value\": \"" + str(Options_list[i+1][1]) + "\"}],"
  wsmsg += "\"Data\": {}}"

  return wsmsg

def SendLocation(AuthToken, ReceiverID, dest_type, Body, latitude, longitude):
  TypeID = "4BDD5F50-DC68-11EA-9FCE-5302A705E738";
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", ";
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", ";
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", "; #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", "; #send msg to a Channel
  wsmsg += "\"Location\": {\"latitude\":" + latitude + ",\"longitude\":" + longitude + "},";
  wsmsg += "\"Body\": \"" + Body + "\"} ";

  return wsmsg;

def SendHTML(AuthToken, ReceiverID, dest_type, Body):
  TypeID = "38199F47-504C-4C73-97E5-8076C8CFAA21";
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", ";
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", ";
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", "; #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", "; #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\"} ";

  return wsmsg;

def ReceiveDate(AuthToken, ReceiverID, dest_type, Body):
  TypeID = "242B5A3B-C1AF-4663-BD97-E296E3DB4D2F";
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", ";
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", ";
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", "; #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", "; #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\", ";
  wsmsg += "\"Data\": {}}";

  return wsmsg;

def ReceiveTime(AuthToken, ReceiverID, dest_type, Body):
  TypeID = "F489C072-2C8B-4BC6-AD75-946D3CA721B7";
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", ";
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", ";
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", "; #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", "; #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\", ";
  wsmsg += "\"Data\": {}}";

  return wsmsg;

def ReceiveLocation(AuthToken, ReceiverID, dest_type, Body):
  TypeID = "20A0CE4B-A236-4E96-9629-45A3AF5F62EA";
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", ";
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", ";
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", "; #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", "; #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\", ";
  wsmsg += "\"Data\": {}}";

  return wsmsg;

def SendJSON(AuthToken, ReceiverID, dest_type, TypeID, Body):
  wsmsg = "{\"AuthToken\": \"" + AuthToken + "\", ";
  wsmsg += "\"Type\": \"chat\", ";
  wsmsg += "\"TypeID\": \"" + TypeID + "\", ";
  if(dest_type==0):
    wsmsg += "\"ReceiverID\": \"" + ReceiverID + "\", "; #send msg to a User ID
  else:
    wsmsg += "\"ConversationID\": \"" + ReceiverID + "\", "; #send msg to a Channel
  wsmsg += "\"Body\": \"" + Body + "\", ";
  wsmsg += "\"Data\": {}}";

  return wsmsg;
