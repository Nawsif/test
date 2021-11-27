import asyncio
import roblox_py
from roblox_py import Client
import os

client = Client(cookies=open("cookie.txt", "r+").read())

gameid = input("Enter game id: ")
visitsreq = input("Enter number of visits: ")
os.system("cls")
print("How long does it take for your ROBLOX to load? This will be the time between visits")
print("1 - Default (12 seconds)")
print("2 - Slow (20 seconds)")
print("3 - custom (enter your own time between visits)")
choosetime = input()

if choosetime == "1":
    os.system("cls")
    timelimit = 12
elif choosetime == "2":
    os.system("cls")
    timelimit = 20
elif choosetime == "3":
    os.system("cls")
    timelimit = int(input("Enter custom time between visits: "))

async def main():
    global gameid
    global timelimit
    global visitsreq
    totalvisited = 0
    for x in range(int(visitsreq)):
        print(f"Visited {str(totalvisited)} times")
        auth_game = await client.join_game(int(gameid))
        await auth_game.join_game()
        await asyncio.sleep(int(timelimit))
        await auth_game.kill_game()
        os.system("cls")
        totalvisited += 1
    
loop = asyncio.get_event_loop()
loop.run_until_complete(main())