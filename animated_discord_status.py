import requests
import json
import time
headers = {"Authorization":"discord_token"}
#Here you need to add your discord account token.
data = {
    "custom_status" : {
        "text":"test",
        "emoji_id":"768389828752179200",
        "animated":"true"
        #1. placeholder text.
        #2. id of your emoji. (open it in the browser and copy the id from the link. exmpl. https://cdn.discordapp.com/emojis/768389828752179200.gif?v=1, id would be 768389828752179200)
        #bool for if the emoji is an animated one.
    }
}
def send_response(tickspeed):
    response = requests.patch("https://discord.com/api/v8/users/@me/settings",json=data,headers=headers)
    print(response)
    time.sleep(tickspeed)
def parse_text(txt):
    for i in range(len(txt)):
        data["custom_status"]['text'] = txt[:i+1]
        if i+1 == len(txt):
            send_response(7)
            #this is the time that the status stays after it is written
        else:
            send_response(1.5)
            #this is the time it takes new letters to be added
if __name__ == "__main__":
    while True:
        #here you should add any text you want to be written on the status. if you add more than 1 they will switch after they are written.
        parse_text("lol funny!")
        parse_text("Xd!1!!")
        parse_text("ed ski")    