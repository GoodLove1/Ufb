import os
from flask import Flask

bapp = Flask(__name__)

@bapp.route('/')
def home():
    return """
<center> 
    <h1>FondnessForwardBot</h1> 
</center> 
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    bapp.run(host='0.0.0.0', port=port)
