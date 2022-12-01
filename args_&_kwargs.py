def show_numbers(**kwargs):
    for i,j in enumerate(kwargs):
        print(i,j)


show_numbers(one=1,two=2,three=3)