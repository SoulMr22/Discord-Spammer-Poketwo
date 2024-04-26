from webserver import keep_alive
import requests

channelID = 1233332944836231179
headers = {
    "authorization":
    "ODc5MjA3MjAwMDU1MjMwNTI1.GKjSzo.92yhGpUH1jt2YcrO1pguCpT1YJXgrOLz7nvuHE"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
