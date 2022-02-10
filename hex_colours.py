colour = {"Bright Ube": "#d19fe8", "Brilliant Rose": "	#ff55a3","Bronze": "#cd7f32", "Brown1": "#ff4040","Buff": "#f0dc82", "Burgundy": "#800020","Burlywood3": "#cdaa7d", "Burnt Sienna": "#e97451","CadetBlue": "#5f9ea0", "Canary": "	#ffff99"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,colour.get(colour_name)))
    colour_name = input("Enter a colour name: ")