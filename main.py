#  this pyscript is for integrating your python code to your webpage
from pyscript import display


r_name= 'Riverbend Brew' #restaurant name to be on display
o_name= 'Owner: Khloe Myles S. Espina' #Owner name to be on display
year= 'Since 2025' #Year of foundation
prod1='Jungle Grove Latté' #1st product 
price1='₱120' #1st price
prod2='Mossy Matcha Cheescake' #2nd product
price2='₱130' # 2nd price
prod3='Flowering Hibuscus Tea' #3rd product
price3='₱90' #3rd price
prod4='Rose Petal Tart' #4th product
price4='₱160' #4th price
prod5='Maple Syrup Waffles' #5th product
price5='₱140' #5th price
schedule='Open Daily | 7:00am - 9pm' #Opening hours

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



