# -*- coding: utf-8 -*-
# CNN
# LINE Library by LineAlpha
# Thank's to all my friend's in CNN 
import CNNBOT
from CNNBOT.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob

#cl = CNNBOT.LINE()
#cl.login(qr=True)
#cl.loginResult()

#ki = CNNBOT.LINE()
#ki.login(qr=True)
#ki.loginResult()

#ki2 = CNNBOT.LINE()
#ki2.login(qr=True)
#ki2.loginResult()

cl = CNNBOT.LINE()
cl.login(qr=True)
cl.loginResult()
#MYID#
ki = CNNBOT.LINE()
ki.login(qr=True)
ki.loginResult()
#QUEEN#
ki2 = CNNBOT.LINE()
ki2.login(qr=True)
ki2.loginResult()
#SUN#
ki3 = CNNBOT.LINE()
ki3.login(qr=True)
ki3.loginResult()
#CLOUD#
#===LOGIN OPERATION===#
print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
#helpMessage ="""666"""
KAC=[cl,ki,ki2,ki3]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
k2mid = ki2.getProfile().mid
k3mid = ki3.getProfile().mid
Bots=[mid,kimid,k2mid,k3mid]
#YANG STANDBY DI GROUP KI,KI2,KI3#
wait = {
    'contact':True,
    'autoJoin':False,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"",
    "lang":"JP",
    "comment":"BLVCK HITTER 花音",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"BLVCK HITTER",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":True,
    "atjointicket":True,
    "winvite":True
}
#WAITING TIME MODE#
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
#WAITING TIME MODE 02#
setTime = {}
setTime = wait2['setTime']
#SET TIME WAIT#
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\nãƒ»" + Name
                wait2['ROM'][op.param1][op.param2] = "ãƒ»" + Name
        else:
            pass
    except:
        pass
#=========================OPERATION START==#
def cloneContactProfile(cl, mid):
    try:
        contact = cl.getContact(mid)
        profile = cl.profile
        profile.displayName = contact.displayName
        profile.statusMessage = contact.statusMessage
        profile.pictureStatus = contact.pictureStatus
        cl.updateProfilePicture(profile.pictureStatus)
        return cl.updateProfile(profile)
    except:   
        pass
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
#==========================OPERATION ADD===#
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#THE PROGRAM BEGINS HERE#
#===OPEN QR KICK START===#
#BOT PROTECT QR CODE#
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).updateGroup(G)
#===RANDOM KICK CHOICE MODE===#
#===OPEN QR KICK AND FINISH===#
#=====TYPE OF 3 KICKER========#
#======📍CL (CLIENT)IN MID
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in kimid:
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)

            if op.param3 in mid:
                if op.param2 in k2mid:
                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki2.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    ki2.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)

            if op.param3 in mid:
                if op.param2 in k3mid:
                    G = ki3.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)

#======📍KI (KICKER 01) IN MID
            if op.param3 in kimid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)

            if op.param3 in kimid:
                if op.param2 in k2mid:
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)

            if op.param3 in kimid:
                if op.param2 in k3mid:
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
#======📍KI2 (KICKER 02) IN MID
            if op.param3 in k2mid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in k2mid:
                if op.param2 in kimid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in k2mid:
                if op.param2 in k3mid:
                    X = ki3.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki3.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)
#======📍KI3 (KICKER 03) IN MID
            if op.param3 in k3mid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = ki3.reissueGroupTicket(op.param1)

            if op.param3 in k3mid:
                if op.param2 in kimid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in k3mid:
                if op.param2 in k2mid:
                    X = ki2.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(op.param1)

#-----DONT NOT CHANGE THIS
#===END OF OPERATION
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

#===ROTATION BOT===#

	if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
#=====#
                       
                elif op.param3 in kimid:
                    if op.param2 in mid:
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)

                        wait["blacklist"][op.param2] = True
#=====#

                elif op.param3 in k2mid:
                    if op.param2 in mid:
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
#======#
                elif op.param3 in k3mid:
                    if op.param2 in mid:
                        ki3.kickoutFromGroup(op.param1,[op.param2])

                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                
            except:
                pass
        
#=============END OF PHARSE PART 04=====#
#DONE OPERATION#
#KI6 COVER BY KI13 & KI14#
#===END OF PHARSE AMOEBA PROJECT MODE===#
#===MOD 1 INVIT 2===#
#==========================NEXT OPERATION=#
#===AUTO JOIN OPERATION====#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "ua717cfcb0ff03ddfc3340974557c20da":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"accept")
#===OPERATION TYPE===#
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already On Blacklist From The komite at ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"I choose to have no idea About this Apologize ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        f=codecs.open('st2.json','w','utf-8')
                        json.dump(wait["commentBlack"], f, sort_keys=True, indent=4,ensure_ascii=False)
                        
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"This contact erase from the blacklist at the komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        wait["dblack"] = False
                        f=codecs.open('st2.json','w','utf-8')
                        json.dump(wait["commentBlack"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"This contac not reading at the Blackist From we are komite at ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already On blacklist of the Komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Already on black list on the komite at ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"We already deleted sir. from the blacklist at the komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─")
                        wait["dblacklist"] = False
                        f=codecs.open('st2__b.json','w','utf-8')
                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Sory sir this contact not already on the blacklist from ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─")
#=====================CONTACT====#
#===WAITING COMMAND===#
#===CONTACT HITTER====#
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
#===TIMELINE POST===#
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#====HELP 01 HITTER HELP�====#
#            elif msg.text is None:
#                return
#            elif msg.text in ["Hitter help"]:
#                if wait["lang"] == "JP":
#                    cl.sendText(msg.to,helpMessage)
#                else:
#                    cl.sendText(msg.to,helpt)
#===GROUP NAME CHANGE✔===#
            elif ("Gnc" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn","")
                    ki.updateGroup(group)
                else:
                    ki3.sendText(msg.to,"Success for change name group sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
#===MKICK✔===#
            elif "Mkick" in msg.text:
                midd = msg.text.replace("Mkick","")
                ki.kickoutFromGroup(msg.to,[midd])
#===INVITW USER BY MID ✔===#
            elif "Invite " in msg.text:
                midd = msg.text.replace("Invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
#===PROTOCOLB===#
            elif "Bourbon" in msg.text:
                midd = msg.text.replace("Bourbon","uaa40df2f8bd9900906cffc086138adb6")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
#===CALL ADMIN===#
            elif "The swan" in msg.text:
                midd = msg.text.replace("The swan","ua717cfcb0ff03ddfc3340974557c20da")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
#===HITTERMID✔===#
            elif "Hitter mid" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
#===GIFT✔===#
            elif msg.text in ["Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
#===CANCEL ALL✔===#
            elif msg.text in ["Sayonara"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"success cancel by komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                            ki2.sendText(msg.to,"Writing to next Protocol sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                            ki3.sendText(msg.to,"success canceling sir. by the komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        else:
                            cl.sendText(msg.to,"done ─অই͜⟦㉿ Континентальный ™ ⟧ ೋa")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Cancelling successfully sir。by komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"All invitation has been canceled sir. by the komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"success canceling sir, By komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Thanks sir")
#===QR ON KICK START✔===#
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Qr:on"]:
                if msg.toType == 2:
                    group = ki3.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    ki3.updateGroup(group)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"url opened By komite Sir\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"What can i do next sir, perhaps?\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki3.sendText(msg.to,"its already opened for you sir, by\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                    else:
                        cl.sendText(msg.to,"Thanks")
                        ki2.sendText(msg.to,"What can i do next, sir?\n  ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki3.sendText(msg.to,"its already opened for you, By the komite of\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"url opened")
                        ki3.sendText(msg.to,"What can i do next,can we have a time together?, With bourbon sir, at the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki.sendText(msg.to,"its already for you, By the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                    else:
                        cl.sendText(msg.to,"Perfect time")
#===QR OFF✔===#
            elif msg.text in ["Qr:off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"url closed")
                        ki2.sendText(msg.to,"What can i do next,Sir? ")
                        ki3.sendText(msg.to,"its already for you, From the Komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                    else:
                        cl.sendText(msg.to,"Lets Dance")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"url closed by\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"We have more time to doing bussines sir. Are you working again?\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki2.sendText(msg.to,"uh im so Ready for the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                    else:
                        cl.sendText(msg.to,"Perfect time")
                        ki2.sendText(msg.to,"What can i do next, Sir? Protocol Please\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki3.sendText(msg.to,"its already opened sir. by komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
#===DEFEND GROUP✔===#
            elif msg.text in ["Protected:on"]:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect url by the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Already success sir. by komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"protect by url successfully sir\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protected sucessfully by komite sir.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"protect by url success From the komite\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"protecteb by\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Thanks")
            elif msg.text in ["Protected:off"]:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect by url has been disable\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Protect disabling\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Protect disable sir by komite of\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Good job sir !")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect by url Already disable sir\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Thank you sir ! ")
#===Group Information===#
#===TRACKING DATA GROUP✔===#
            elif msg.text == "Gdata":
                if msg.toType == 2:
                    ginfo = ki.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "Refusal"
                        else:
                            u = "許可"
                        ki.sendText(msg.to,"[Group]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[Group Creator]\n" + gCreator + "\n[Profile Group]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmember:" + str(len(ginfo.members)) + "People\ninvite:" + sinvitee + "People\nRejectURL:" + u + " By Swan。")
                    else:
                        ki.sendText(msg.to,"[名字]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[小组的作成者]\n" + gCreator + "\n[小组图标]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Next order sir。")
                        ki.sendText(msg.to,"Mybe after this we need to dinner together。")
                        ki2.sendText(msg.to,"What you wanna i to do something affter this sir? Next protocol. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        ki3.sendText(msg.to,"Tracking Progres already Complette Are you wotking again ? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        ki2.sendText(msg.to,"This system cannot use if we not stay on the group sir. this by komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"Tracking group Complete sir, by the komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#====MY ID✔====#
            elif "Hitter id" == msg.text:
                cl.sendText(msg.to,msg.to)
#====MID ID✔====#
            elif "Hitter Mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,k5mid)
                ki3.sendText(msg.to,k3mid)
#====IMPORTANT FITURE====#
#====OPTIONAL SET CHECK====#
#====WILL CHECKING STATS====#
#==========================BLOCK INVITE✔===#
            elif msg.text in ["Protectall:on"]:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set Block invite already turn On sir ! By the komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki.sendText(msg.to,"All hitter already prepare to def sir. by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Already send the message to all hitter if have a trouble here Sir by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"All of you sir. by the komite, Prepare To defend Here ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block invite already Turn on sir, Mybe it will spend a few time, till negotiate end with the komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"No Bussines on Continental Ground Sir, DOG BOARDNING AVAILABLE ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
                        ki2.sendText(msg.to,"So please Respect with our people, Then They will respect to you too. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"Ashes to ashes, This just like the circle of the life and death Continues ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Lets Doing bussines ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#==========================BLOCK INVITE✔===#
            elif msg.text in ["Protectall:off"]:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already turn off by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"No Bussines on Continental Ground Sir, DOG BOARDNING AVAILABLE. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Evrything have a pride, and everything have a price, Lets agree to disagree.Lets doing bussines here sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"You will be Revoke by your attitude from the komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Hitter Standby sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Has been turn Off sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Dont Missing it Kid.─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Evrything have a pride, and everything have a price. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"Keep your attitude sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"And Relax, For now ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#==========================END PHARSE===#
#===BROADCAST✔===#
#            elif "Broadcast " in msg.text:
#                                bctxt = msg.text.replace("Said ","")
#                                cl.sendText(msg.to,(bctxt))
#                                ki.sendText(msg.to,(bctxt))
#                                ki2.sendText(msg.to,(bctxt))
#===TIME LINE UPDATE STATUS✔===#
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#===CHANGE NAME (ME)✔===#
            elif "Changename " in msg.text:
                string = msg.text.replace("Changename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"changed name to " + string + " success Sir !")
#===BOT CHANGE NAME KI✔===#
            elif "Kicn:" in msg.text:
                string = msg.text.replace("Kicn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"change name to" + string + "success Ser, Anything Else sir? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===BOT CHANGE NAME KI2✔===#
            elif "Ki2cn:" in msg.text:
                string = msg.text.replace("Ki2cn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to,"change name to" + string + "─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===BOT CHANGE NAME KI3✔===#
            elif "Ki3cn:" in msg.text:
                string = msg.text.replace("Ki3cn:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to,"change name to" + string + "Thanks Sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#======================END PHARSE BOT CN==#
#===CONTACT OFF✔===#
            elif msg.text in ["Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Already Change On Sir ! by komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki3.sendText(msg.to,"Turning on Sir by komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki7.sendText(msg.to,"Turning On Complete Sir by komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ki5.sendText(msg.to,"Succes tun on Sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki.sendText(msg.to,"This already on Sir, Procesed complete..By the komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===CONTACT OFF✔===#
            elif msg.text in ["Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Already turning Off sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki2.sendText(msg.to,"successful.. Turning Off Sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Now What Sir ? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        cl.sendText(msg.to,"Turning off Complete sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#======================END SHARE CONTACT==#
#====JOIN ON✔====#
            elif msg.text in ["Join:on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"auto join ready activated sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"I already activated, The join on sir ! will you want to cal all hitter to sir ? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki.sendText(msg.to,"Progress Complette sir by komite of ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Writing to next order sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"auto join ready by the komite sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki.sendText(msg.to,"success turn on sir by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#======JOIN OFF✔======#
            elif msg.text in ["Join:off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"auto join not set by komite sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Set off sir by komite ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki2.sendText(msg.to,"We already turn it off for you sir, by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Writing to next protocol sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki2.sendText(msg.to,"Can you give me next protocol sir, Im stay in a good position. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#====REJECT GROUP INVITATION✔====#
            elif msg.text in ["Group:lock"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been refused sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"Now We can doing bussines here sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    ki.sendText(msg.to,"Can you give me next protocol sir? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"Enjoy and Relax sir, For now ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#====ACCEPT GROUP INVITATION✔====#
            elif msg.text in ["Group:unlock"]:
                gid = ki.getGroupIdsInvited()
                for i in gid:
                    ki.acceptGroupInvitation(i)
                if wait["lang"] == "JP":
                    ki.sendText(msg.to,"All invitations have been Allowed sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"Mybe we can show ,how to hold the spoon sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    ki.sendText(msg.to,"Can you give me next protocol sir? ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"Perhaps Bourbon will make your good, Enjoy and Relax sir, For now ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#====HITTER STATTS====#
#====LEAVE ON✔====#
            elif msg.text in ["Leave:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ─。")
                    else:
                        cl.sendText(msg.to,"its already opened sir by ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"i already turn it on sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"its opened sir ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#====LEAVE OFF✔====#
            elif msg.text in ["Leave:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turn it off ser ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Turn Off by the komite sir. ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"I turn it of by the komite Ser ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"This just for said see you again soon. buddy ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#====AUTOSHAREON✔====#
            elif msg.text in ["Auto share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Turn on Sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Already opened by the komite sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"I turn it on Sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Opened Ser ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#====AUTOSHARE✔====#
            elif msg.text in ["Auto share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Its Already turn off sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Turn Off sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"I Turn it of Sir ! ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"For going, ashes to ashes . ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#====Hitter stats====#
            elif msg.text in ["Set check"]:
                md = ""
                if wait["Protectcancel"] == True: md+="─অই͜⟦㉿ Континентальный ™ ⟧ ೋ\n\nঅই ͜⁅▣ Protect Cancel : on\n"
                else: md+="─অই͜⟦㉿ Континентальный ™ ⟧ ೋ\n\nঅই ͜⁅▣ Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+="অই ͜⁅▣ Protect Qr      : on\n"
                else: md+="অই ͜⁅▣ Protect Qr   : off\n"
                if wait["Protectguest"] == True: md+="অই ͜⁅▣ Block Invite : on\n"
                if wait["contact"] == True: md+="অই ͜⁅▣ Contact : on\n"
                else: md+="অই ͜⁅▣ Contact : off\n"
                if wait["autoJoin"] == True: md+="অই ͜⁅▣ Auto join : on\n"
                else: md +="অই ͜⁅▣ Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="অই ͜⁅▣ Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "অই ͜⁅▣ Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="অই ͜⁅▣ Auto leave : on\n"
                else: md+="অই ͜⁅▣ Auto leave : off\n"
                if wait["timeline"] == True: md+="অই ͜⁅▣ Share : on\n"
                else:md+="অই ͜⁅▣ Share : off\n"
                if wait["autoAdd"] == True: md+="অই ͜⁅▣ Auto add : on\n"
                else:md+="অই ͜⁅▣ Auto add : off\n"
                if wait["commentOn"] == True: md+="অই ͜⁅▣ Comment : on\n"
                else:md+="অই ͜⁅▣ Comment : off\n"
                cl.sendText(msg.to,md)
#===AUTO ADD ON✔===#
            elif msg.text in ["Auto add:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add has been set on ser ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Auto add on sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already set on sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Set on done \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#===AUTO ADD OFF✔===#
            elif msg.text in ["Auto add:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hasbeen Turn of sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Set it off ser ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add has turn off sir \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Seting off done. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#===MESAAGE ADD✔===#
            elif "Message add:" in msg.text:
                wait["message"] = msg.text.replace("Message add:","")
                cl.sendText(msg.to,"Mesaage Add has been Created。\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
#===GREETING COMMAND✔===#
            elif "Greeting:" in msg.text:
                wait["message"] = msg.text.replace("Greeting:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Greeting successfully set sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    cl.sendText(msg.to,"Changed the information ser ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#===CONFIRMATION ADD✔===#
            elif msg.text in ["Add message"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Mesaage add automatical confirmed like this sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Add confirmation message has been change like this sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。\n\n" + wait["message"])
#===CHANGE LANGUAGE COMMAND❌===#
            elif msg.text in ["言語変更"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"切換中國語。")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"言語を日本語にしました。")
#===CHANGE COMMENT✔===#
            elif "Change comment:" in msg.text:
                c = msg.text.replace("Change comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"The string cannot be change by the komite ser. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"The comment already changed \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。\n\n" + c)
#===COMMENT SET✔===#
            elif "Comment set:" in msg.text:
                c = msg.text.replace("Comment set:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Set Comment already Checkpointed sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Comment has been Set sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。\n\n" + c)
#===COMMENT ON✔===#
            elif msg.text in ["Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set on sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Already seting on sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Set On complette sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Already turn on \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#===COMMEND OFF✔===#
            elif msg.text in ["Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turning off sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Already Off \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Has been off sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    else:
                        cl.sendText(msg.to,"Set it off sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#===COMMEND CHECK✔===#
            elif msg.text in ["Comment check"]:
                cl.sendText(
msg.to,"Automatical Commend Has been set Like this sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。\n\n" + str(wait["comment"]))

#===JOINTICKET✔===#
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ","")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
#===URL✔===#
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"....")
                    else:
                        cl.sendText(msg.to,"..")
#===UPDATING TIME✔===#
            elif msg.text in ["Update Time"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"clock success update. and syncronization with Continental server. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki.sendText(msg.to,"success sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to," Already update. success sir \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki3.sendText(msg.to,"Next Protocol Sir \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    ki.sendText(msg.to,"success update with the server Continental Sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"The system already Sync Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki3.sendText(msg.to,"Connecting Success \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===REVOKE1 PEOPLE✔===#
	    elif "Denied " in msg.text:
                       nk0 = msg.text.replace("Kick","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,ki2,ki3]
                                    kicker=random.choice(klist)
				    kicker.kickoutFromGroup(msg.to,[target])
                                    
                                    romGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"success revoke sir \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                                    ki2.sendText(msg.to,"I am sorry sir. Evrything its just for a good bussines. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===RELAX SIR✔===#
            elif "Relax sir" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Relax sir","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    ki.sendText(msg.to,"excuise me sir, But you have been Revoke By the komite of Continental, As By your attitude. Enjoy and Relax sir. For now !\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"Now you know How we doing bussines. Or wash your foot and going sleep kid. dont going to far away from your home kid. Or we will teach you how to hold the spoon. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki3.sendText(msg.to,"Evrything have a pride and evrything have a CODE, Without Eticade code we just spend a life like animal sir! so please RESPECT for The Kommite at the ㉿Continental™NO BUSSINES ON CONTINENTAL GROUND. DOG BOARDNING AVAILABLE Sir.\n\n●Regards - Continental")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not yet Sir. We still Doing bussines here. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Perhaps Next time Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Not Ready yet sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        for target in targets:
                            try:
                                klist=[cl,ki,ki2,ki3]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                pass
#====FUNGTION BAN✔====#

            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Banned Protocol activited. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki.sendText(msg.to,"Sir Can You Send The contact sir ? \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki2.sendText(msg.to,"We will send The information To the Continental sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
                ki3.sendText(msg.to,"send contact Sir i already Connect with Continental Server. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#====FUNGTION UNBAN✔====#
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Unbanned Protocol has been activited.")
                ki.sendText(msg.to,"send contact sir i already connect, with Continental Server. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki2.sendText(msg.to,"send contact And progressing Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki3.sendText(msg.to,"send contact sir.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")


#===UNBAN BY TAGGING✔===#
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        ki2.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Done Doing Bussines..")
                                ki.sendText(msg.to,"Succes unbanned ser ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
                                ki2.sendText(msg.to,"Anything else sir ?. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                                ki3.sendText(msg.to,"Succes Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                            except:
                                ki.sendText(msg.to,"Success unban by komite Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                                ki2.sendText(msg.to,"Successfully sir unbanned by komite. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                                ki3.sendText(msg.to,"Succes unbaned the Contact Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===BANNED USE TAG✔===#
            elif "Ban @" in msg.text:

                _name = msg.text.replace("Ban @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki2.sendText(msg.to,"I already Successfully banned the Contact sir, Hes will be the Continental Targets, And Without Eticade Code We just Same like animal Sir！")
                                    ki3.sendText(msg.to,"Sucessfully banned sir. Now The Contact Already On Continental Server Targeting List, And they soul will be priceless！")
                                    ki.sendText(msg.to,"And They Will be Revoke From the Komite By they own Atitude！")
                                except:
                                    ki.sendText(msg.to,"error")
#===MENTIONESS✔===#
            elif msg.text in ["Mentiones"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#===RESPONSENAME✔===#
            elif "Response name" in msg.text:
                profile = ki.getProfile()
                text = profile.displayName + "\n[ BLVCK HITTER - ORGANIZATION ]\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ"
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + "\n[ BLVCK HITTER - ORGANIZATION ]\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + "\n[ BLVCK HITTER - ORGANIZATION ]\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ"
                ki3.sendText(msg.to, text)
#===UTILITY BOT===#
#==BANNED✔==#
            elif msg.text in ["Banned"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Banned contact successfully sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                ki.sendText(msg.to,"Banned Contact Success Sir, The data will be send to the Continental Server. Uploading sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                ki2.sendText(msg.to,"Banned Success sir, Now the Contact is priceless By the Komite \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                ki3.sendText(msg.to,"Banned Done. Next Protocol sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#==UNBAN✔==#
            elif msg.text in ["Unbanned"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Unbanned success Sir ! 。\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki.sendText(msg.to,"Un Banned The contact Already success by the komite of Continental Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ 。")
                ki2.sendText(msg.to,"Un banned Has bees Successfully by The komite sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                ki3.sendText(msg.to,"Un Banned Progress Clear. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
#==BANLIST✔==#
            elif msg.text in ["Banned list"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"no user in banlist..")
                else:
                    cl.sendText(msg.to,"checking banlist user in Continental Server Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki.sendText(msg.to,"This we show the Banlist user From Continental sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    ki2.sendText(msg.to,"List Banned in Progress, Updating sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    ki3.sendText(msg.to,"This The list Target From the Continental Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "List user\n\n✩ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
             
#==LIST BANNED✔==#
            elif msg.text in ["List banned"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"no user in banlist Sir. What you want to banned the contact write「Banned」Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                    ki.sendText(msg.to,"no user in banlist.. ser. ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"no user in banlist from the Comite on continental Sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                else:
                    cl.sendText(msg.to," Still checking bandlist user, From the Commite of continental Server. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki.sendText(msg.to,"checking at Komite server Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to,"Check banlist. Waiting the Follow up from the Continental Server sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "List user\n\n\✩ " +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    ki.sendText(msg.to,mc)
                    ki2.sendText(msg.to,mc)
                    ki3.sendText(msg.to,mc)
#===KICK BANNED LIST✔===#
            elif msg.text in ["Enjoy sir"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"No user on Continental Blacklist To Revoke The Contact From this group sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        ki2.sendText(msg.to,"No Targets here Sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        ki3.sendText(msg.to,"No user on The Contact From this group sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ。")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,ki2,ki3]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
#===ALL INVIT AND LOCK✔===#
            elif "Continental lock" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "Ready For Protocol Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "Ready For Doing bussines here sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ ")
                        ki.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "Perhaps Bourbon Will make your good and Relax Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        print "Hitter Ready"
                        G.preventJoinByTicket(G) 
                        cl.updateGroup(G)
                       
#======ALLJOINGROUP✔======#
            elif "Spada" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
			ki.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "warmest greeting from continental, Evrything have a price Sir ! Lets agree to disagree. Evrything its just for a good bussines.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
			ki2.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "No Bussines on continental Ground. DOG BOARDNING AVAILABLE.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
			ki3.sendText(msg.to,"[" + str(ginfo.name) + "]\n\n" + "Ashes to ashes, Perhaps Bourbon will make your good and Relax sir. For now ! .\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        print "hitter ready"
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
#===LEAVE GROUP & BYE BOT✔===#
	    elif "Hastalavista" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
 		        ki.sendText(msg.to,"See you again soon kid, we always watching at you. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n " + "*" + str(ginfo.name) + "*")
                        ki.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"I hope next time you have a lucky days like on this day sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n" + "*" + str(ginfo.name) + "*")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"Please Respect with the commite at Continental, or we will teach you How to hold the spoon sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n " + "*" + str(ginfo.name) + "*")
                        ki3.leaveGroup(msg.to)
                        cl.sendText(msg.to,"Thanks sir")
                    except:
                        pass

#===LEAVE GROUP✔===#
            elif "Good bye kid" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#===CHECK HITTER ON✔===#
            elif "Hitter help" in msg.text:
                ki.sendText(msg.to,"\n[ HITTER - MAIN COMMAND ]\n\n○㉿SBcreator\n○㉿Hello world\n○㉿TL:\n○㉿Gift\n○㉿Hitter id\n○㉿Update time\n\n[ COMMAND IN GROUP ]\n○㉿Gmade\n○㉿Gnc\n○㉿Banned tag\n○㉿Url\n○㉿Gdata\n○㉿Setpoint\n○㉿Recheck\n○㉿Hitter on\n○㉿Hitter id\n○㉿Hitter mid\n○㉿Group:lock\n○㉿List Banned\n○㉿Mentiones\n○㉿Good bye kid")
                ki2.sendText(msg.to,"\n[ HITTER - MISC COMMAND ]\n\n○㉿Gnc\n○㉿Hitter mid\n○㉿Comment check\n○㉿Comment set:\n○㉿Add message:\n○㉿Response name\n○㉿Changename + Text\n○㉿Kicn:\n○㉿Ki2cn:\n○㉿Ki3cn:\n○㉿Gmade\n○㉿Mid + @\n○㉿Mesaage add\n\n[ CHECK - STARTS ]\n○㉿Set check\n○㉿Qr on•off\n○㉿Protected:on•off\n○㉿Protectall:on•off\n○㉿Contact:on•off\n○㉿Auto share:on•off\n○㉿Auto add:on•off\n○㉿Comment:on•off\n○㉿Leave:on•off\n○㉿Join:on•off")
                ki3.sendText(msg.to,"\n[ HITTER - BUSSINES CMDR ]\n\n○㉿How fast\n○㉿Spada\n○㉿Hastalavista\n○㉿Continental lock\n○㉿Enjoy sir\n○㉿Ban/Banned + C\n○㉿Unban/Unbanned + C\n○㉿Banned + Contac\n○㉿Banned list\n○㉿Ban + @\n○㉿Unban + @\n○㉿Relax sir\n○㉿Denied + @\n○㉿Revoke + @ + @\n○㉿jointicket + link\n○㉿Time now\n○㉿Mkick + Mid\n○㉿Invite + Mid\n○㉿Sayonara\n\n\n○㉿ Continental - GST.BOT™")
#===PROTOCOL B===#
            elif "Protocol b" in msg.text:
                ki.sendText(msg.to,"The Protocol B ,Has been activited ,Excuise me sir, But we Still doing bussines here ! And You Have been REVOKE by, The Komite. And Your Arguments its will be PRICELESS. by the komite of Continental. As by Your Atitude. And Your Choice Will not agree With the Komite of continental. So lets Agree to disagree. Evrything its just For a good Bussines Sir. Because this is all the Reason Why we standing here. And this is WHO WE ARE !\n\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki2.sendText(msg.to,"We already explain sir About the rules and Code, Like Old Promisses, And we Standing here ,For the Komite Of Continental, Evrything have a price, and everything have a code, without Code We just spend a life Like animal. So please Respect with our people, Then They will respect to you to. Sir, Now you can having Fun, and enjoy For Spend Your last Time Together Sir. We have no apologize here. Because we will always fighting For the truth, We are the World Family. We do not Forgive and we do not Forget. EXPECT US!\n\n••••Regards\n─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                ki3.sendText(msg.to,"Relaxs sir")
#===CCTV SLIDER===#
            elif msg.text == "Setpoint":
                    cl.sendText(msg.to, "Still finding the slider sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki.sendText(msg.to, "Prepare to check Sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki2.sendText(msg.to, "Checking sir. the agent from continental stay in evrywhere ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    ki3.sendText(msg.to, "You can run but you cant hide kid ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
#===RECHECK✔===#
            elif msg.text == "Recheck":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[0] + "\n"

                        ki2.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal \n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        ki3.sendText(msg.to, "An already read point has not been set.\n「set」you can send,and read point will be created Sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===CHECKING SPEED✔===#
#===AND CREATOR BOT==#
            elif "How fast" in msg.text:
                start = time.time()
                ki.sendText(msg.to, "Writing server speed sir, perhaps it will be spend a few moment sir, enjoy and Relax, For Now ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
		ki.sendText(msg.to, "%s second" % (elapsed_time))
		ki2.sendText(msg.to, "%s second" % (elapsed_time))
		ki3.sendText(msg.to, "%s second" % (elapsed_time))
#===SB CREATOR✔===#
	    elif msg.text in ["SBcreator"]:
                if msg.toType == 2:
                      msg.contentType = 13
                      Creatorbot = "ua717cfcb0ff03ddfc3340974557c20da"
                      try:
                         msg.contentMetadata = {'mid': Creatorbot}
                      except:
                        Creatorbot = "ua717cfcb0ff03ddfc3340974557c20da"
                      cl.sendText(msg.to, "Author By : [B.HT™]•㉿Cnn \n●BLVCK SHADE\n●BLVCK SVVAIV\n●BLVCK FOX\n\nWarmest Greeting From Continental GS-T.BOT Team. Perhaps Bourbon will make your good, And Relax Sir. For Now ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                      cl.sendMessage(msg)
#===WELCOME MSG✔===#
	    elif msg.text in ["Hello world"]:
                ginfo = cl.getGroup(msg.to)
                ki.sendText(msg.to,"welcome back sir , enjoy, and relax. For Now ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n" + str(ginfo.name))
                ki2.sendText(msg.to,"Warmest Greeting From Continental Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n" + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                ki3.sendText(msg.to,"We will not agree if you doing bussines at continental Ground sir. DOG BOARDNING AVAILABLE. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n" + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#===GROUP MADE INFO✔===#
	    elif "Gmade" in msg.text:
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
		    ki3.sendText(msg.to,"This Owner From this Group Sir \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ \n " + str(group.name) + " :\n" + group.creator.displayName )
                    cl.sendMessage(M)
#===SEE MID WITH TAGGING PERSON✔===#
	    elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki2.sendText(msg.to, g.mid)
                        ki3.sendText(msg.to, "Processing done, Sir.\n「Mid」As you want sir ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===BANNED TAGGING✔===#
                    else:
                        pass
	    elif ("Banned tag " in msg.text):
               if op.param2 in Bots:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      ki.sendText(msg.to,"Succesfully Doing the bussines sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                      ki2.sendText(msg.to,"Next Protocol sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                   except:
                      pass
#===KICK BY TAGGING✔===#
	    elif ("Revoke " in msg.text):
               if op.param2 not in Bots:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      ki2.kickoutFromGroup(msg.to,[target])
                      ki.sendText(msg.to,"Evrything Its just for a good bussines sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                      ki3.sendText(msg.to,"So Please Respect With our people, Then they will respect to you to. without Code we just same like animal. DOG BOARDNING AVAILABLE SIR. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                   except:
                      pass
#===REJECT INVITE✔===#
	    elif msg.text in ["Group lock"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"No someone can doing bussines in Continental Ground, An so please respect till the negotiate end sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Without Eticade code, we just same like a animal sir, and evrythingbhave code Expect us. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Wait and see, silent in strike, Perhaps bourbon will make your Good for negotiate, And Relax sir. Enjoy, For now ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ.")
                        ki3.sendText(msg.to,"Dont ever thinking like you have choice, just Choose one and evrithing will be clear sir, Or You have been revoke by the commite as like your attitude. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki.sendText(msg.to,"Perhaps Bourbon will make your good and Relax Sir. For Now ! \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===ALLOW INVITE✔===#
	    elif msg.text in ["Group unlock"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.acceptGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"I hope is a beeter ways, and best choice from you Sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki.sendText(msg.to,"Its just like game hide and seek, you come i come, and if you will go, we will follow you like your shadow. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki2.sendText(msg.to,"Dont pick a wrong choice sir, or we will teach you how to hold the spoon \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                        ki3.sendText(msg.to,"The beeter solution is begins from your self. Continental agent always stay in everyplace you stay sir. \n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
                    else:
                        ki.sendText(msg.to,"Next time we hope you have a lucky day like on this day sir.\n ─অই͜⟦㉿ Континентальный ™ ⟧ ೋ")
#===GROUP BROADCAST✔===#
#	    elif "Broadcast group " in msg.text:
#     		bctxt = msg.text.replace("Broadcast group", "")
#     		n = cl.getGroupIdsJoined()
#     		for i  in n:
#          	    cl.sendText(msg.to, (bctxt))
#===CONTACT BROADCAST✔===#
#	    elif "Broadcast Cntc " in msg.text:
#     		bctxt = msg.text.replace("Broadcast Cntc ", "")
#     		t = cl.getAllContactIds()
#     		for o in t:
#          	    cl.sendText(msg.to, (bctxt))
#===========================OPERATIONALTYPE=#
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)
                        ki.sendText(msg.to,"I m Back Sir. Lets agree to disagree.")

                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        ki.sendText(msg.to,"I Already said to you sir. Dont Doing bussines at Continental ground. DOG BOARDNING AVAILABLE SIR.")
                       
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.sendText(msg.to,"Ashes to Ashes Sir. The Circle Of the life and death Continues.")

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)

                        wait["blacklist"][op.param2] = True
                        ki2.sendText(msg.to,"This we stay, Where the bullet say.")
#======#
#K2MID = KI2MID#
                elif op.param3 in ki2mid:
                    if op.param2 in ki3mid:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = ki3.getGroup(op.param1)
                        ki3.sendText(msg.to,"Evrything Have a Price sir. Without Code we just like animal sir.")

                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki3.sendText(msg.to,"Now We show to you How to hold the spoon.")

                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        ki3.sendText(msg.to,"Perhaps Bourbon will make your good and Relax sir. For now !")
#=====#
                elif op.param3 in ki3mid:
                    if op.param2 in mid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)
                        cl.sendText(msg.to,"Lets Finish this.")

                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.sendText(msg.to,"As My Situation Sir.")
#==#
                elif op.param3 in mid:
                    if op.param2 in ki2mid:
                        cl.kickoutFromGroup(op.param1,[op.param2])

                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        ki2.sendText(msg.to,"Now you know, Evrything its just for a good bussiness. sir")
                
            except:
                pass


#------------------------------------------------------------------------------------#
#END OF PHARSE SEGMEMT 01#
#------------------------------------------------------------------------------------#
#====TIME✔====#
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
