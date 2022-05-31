import random,requests
def rand_port():
    ports=[i for i in range(1,6)]
    def inner():
        port_choice = random.choice(ports)
        ports.remove(port_choice)
        return int(port_choice)
    return inner



test=rand_port()

print(test())
print(test())
print(test())
print(test())
print(test())
test1=rand_port()
print(test1())
print(test1())

url='https://www.mydrivers.com'

rep=requests.get(url)
