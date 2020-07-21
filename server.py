from bot import chad_bot
import requests
import json
 
dog_url='https://dog.ceo/api/breeds/image/random'

update_id= None
bot = chad_bot()
def make_reply(msg):
    if msg == '/hi':
        reply= "hi there, I am a Bot created by Aman Kumar(amanku070300 on gitHub) follow my creator on instragram @not.aman.kumar"
    elif msg == '/doggo':
        r = requests.get(dog_url)
        json_parse = json.loads(r.text)
        reply= json_parse["message"]
        return reply

    else:
        reply= None
    return reply

while True:
    print ("...")
    updates=bot.get_updates(offset=update_id)
    updates= updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message= item["message"]["text"]
            except:
                message = None
            from_=item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply,from_)


