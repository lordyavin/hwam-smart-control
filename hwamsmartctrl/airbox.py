import aiohttp
import json

class Airbox:
    def __init__(self, host:str):
        self.host = host
        self.session = aiohttp.ClientSession(base_url="https://"+self.host)
    
    async def getStoveData(self) -> dict:
        async with self.session.get("/get_stove_data") as response:
            txt = await response.text()
            return json.loads(txt)
        
    async def startCombustion(self) -> bool:
        async with self.session.get("/start") as response:            
            data = await response.json()
            if data["response"] == "OK" : 
                return True
            else :
                return False
            
    async def setBurnLevel(self, level:int) -> bool:
        async with self.session.post("/set_burn_level", data={"level":level}) as response:
            data = await response.json()
            if data["response"] == "OK" : 
                return True
            else :
                return False