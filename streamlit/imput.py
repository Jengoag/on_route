    url="http://127.0.0.1:5000/store_addresses"
    initial_input = "alcala"

    info = {'initial': initial_input, }
    requests.post(url, data=info) 