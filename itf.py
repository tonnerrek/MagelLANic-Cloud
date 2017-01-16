import yaml
from jinja2 import *


with open("itf.yaml", "r") as f:
 itf = yaml.load(f)

 
env = Environment(loader=FileSystemLoader("./junos/interfaces/"))
port = raw_input("Please enter port type:")
template = env.get_template('cPort' + port + '.j2')

print "\n\n\n"
print template.render(interface=itf)
print "\n\n\n"