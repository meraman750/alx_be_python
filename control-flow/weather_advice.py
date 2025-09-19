current_weather = str(input("What's the weather like today? (sunny/rain/cold):"))
match current_weather:
	case "sunny":
		print("Wear a t-shirt and sunglasses.")
	case "rain":
		print("Don't forget your umbrella and a raincoat!")
	case "cold":
		print("WMake sure to wear a warm coat and a scarf.")
	case _:
		print("Sorry, I don't have recommendations for this weather.")
    