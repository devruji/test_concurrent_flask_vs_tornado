from flask import Flask
from time import sleep
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

def mock_api_request(num) -> int:
    sleep(1)
    return num


@app.route('/')
def hello_world() -> dict:
    results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for result in executor.map(mock_api_request, [i for i in range(5)]):
            results.append(result)

    return {'res': results}

if __name__ == '__main__':
    app.run(threaded=True, debug=True)