#%%

class Chair:
    def __init__(self, color, number_of_legs):
        if int != type(number_of_legs):
            raise ValueError("legs has to be an int")
            # to specify that legs has to be an error
        
        self.color = color
        self.number_of_legs = number_of_legs



chair1 = Chair("red", 4)
chair2 = Chair ("black", 3)

print(chair1.color)
print(chair1.number_of_legs)



# %%
