from flask import FLask
app = flask(__name__)
@app.route("/")
def connection():
  return "void spector server loaded"
@app.route("/update")
def gameheartbeat():
  return "PULSE"

@app.route("/tempprofile") #yes its called temp profuile
def returnsession():
  return "shut to dumb as up"

@app.route("/version") # i made it return a custom version
def returnversion():
  return "voidspector local"


if __name__ == "__main__":
  app.run("0.0.0.0",port=5362,debug=False) # keep debug false if your streaming the code or showing it to someone
