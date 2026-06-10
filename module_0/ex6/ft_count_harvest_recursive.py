def	ft_counter(count, day):
	if(count > day):
		print("Harvest time!")
		return

	print(f"Day {count}")
	ft_counter(count + 1, day)

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	ft_counter(1, days)