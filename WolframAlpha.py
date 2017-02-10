import wolframalpha

print("@input",end="")
print(" #",end="")
print("server_host_addr:port_",end="")
input = input("")
app_id = "TA453W-E39H3LV76r"
client = wolframalpha.Client(app_id)

res = client.query(input)
output = next(res.results).text

print("@output", " #",end="")
print(output)

