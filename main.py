#  this pyscript is for integrating your python code to your webpage
from pyscript import display

r_name= 'Riverbend Brew' #restaurant name to be on display
o_name= 'Owner: Khloe Myles S. Espina' #Owner name to be on display
year= 'Since 2025' #Year of foundation
prod1='Jungle Grove Latté' #1st product 
price1='₱120' #{}
prod2='Mossy Matcha Cheescake'
price2='₱130'
prod3='Flowering Hibuscus Tea'
price3='₱90'
prod4='Rose Petal Tart'
price4='₱160'
prod5='Maple Syrup Waffles'
price5='₱140'
schedule='Open Daily | 7:00am - 9pm'

display(f'{r_name}', target="result")
display(f'{o_name}', target="result1")
display(f'{year}', target="result2")
display(f'{prod1}', target="prod1")
display(f'{prod2}', target="prod2")
display(f'{prod3}', target="prod3")
display(f'{prod4}', target="prod4")
display(f'{prod5}', target="prod5")
display(f'{price1}', target="price1")
display(f'{price2}', target="price2")
display(f'{price3}', target="price3")
display(f'{price4}', target="price4")
display(f'{price5}', target="price5")
display(f'{schedule}', target="Sched")


