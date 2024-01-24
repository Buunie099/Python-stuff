import datetime

y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().time().hour
n = datetime.datetime.now().time().minute
t = "am"
if h > 12:
    h -= 12
    t = "pm"
print("The day is",y,"-",m,"-",d,"and it is",h,":",n,t)


# for html
# <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
# <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>