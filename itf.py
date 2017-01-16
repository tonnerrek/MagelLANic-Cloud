import yaml
from jinja2 import *


with open("itf.yaml", "r") as f:
 itf = yaml.load(f)

 
env = Environment(loader=FileSystemLoader("./junos/interfaces/"))
template = env.get_template('cPortOFC.j2')

print "\n\n\n"
print template.render(interface=itf)
print "\n\n\n"