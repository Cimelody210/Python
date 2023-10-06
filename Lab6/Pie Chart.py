import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

y = np.array([21.9,17,7,10.8, 5.8, 8, 35.8])
mylabels = ["ToothPaste", "FaseWash","FaceCream" ,"Moisturixer", "Shampoo","Bathing Soap"]

plt.pie(y, mylabels)
plt.legend(title = "Four Fruits:")
plt.title('The charts show the sources of electricity produced in 4 countries between 2003 and 2008.')
plt.show()