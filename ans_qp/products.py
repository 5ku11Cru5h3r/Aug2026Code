import subprocess

products = [
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10},
{"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50}
]

id_counter = 3

def menu():
    menu_txt = '''
    1.Add Product
    2.View Product
    3.Search Product
    4.Update Product
    5.Delete Product'''
    
    print("***********Product Inventory Management System************")
    print(menu_txt)
    try:
        choice = int(input("Enter the choice you want: "))
        if choice < 0 or choice > 5:
            print("Enter choise between 0 and 5")
        return choice
    except ValueError:
        print("choice must be a Number")
        
def add_product():
    global id_counter
    while True:
        print("Enter the details of the product: ")
        id_counter+=1
        name = input("Name:     ")
        while name == "":
            name = input("Name:     ")
            
        category = input("Category:     ")
        while category == "":
            category = input("Category:     ")
            
        while True:
            try:
                price = float(input("Price:     "))
                if price <= 0:
                    print("Price cannot be less than 0")
                    continue
                break
            except ValueError:
                print("Value must be a number")
                
        while True:
            try:
                quantity = int(input("Quantity      "))
                if quantity <= 0:
                    print("Quantity must be more than 0")
                    continue
                break
            except ValueError:
                print("Quantiy must be a number")
                
        prod_data = dict(id=id_counter, name=name, category=category, price=price, quantity=quantity)
        
        products.append(prod_data)
        print(f"\n product added with id: {id_counter}")
        choice = input("Enter more product [y/n]: ").strip().lower()
        if choice != 'y':
            return
      
def print_one_product():
        product = products[0]
        id, name, category, price, quantity = product.values()
        print(f"ID:       :{id}")
        print(f"Name         {name}")
        print(f"Category         {category}")
        print(f"Price         {price}")
        print(f"Quantity         {quantity}")
        
def print_products():
    print("-"*98)
    print(f"{'ID':<5} {"Name":<25} {"Category":<25} {"Price":<15} {"Quantity":<15}")
    print("-"*98)
    for p in products:
        pid, name, category, price, quantity = p.values()
        print(f"{pid:<5} {name:<25} {category:<25} {price:<15} {quantity:<15}")
    
    print("-"*98)
      
def view_product():
    if len(products) == 0:
        print("No Product found in products")
    elif len(products) == 1:
        print_one_product(products)
    else:
        print_products()
        
def search_product():
    result = []
    search_item = input("Enter the product item to search for: ")
    if search_item.isdigit():
        search_term = int(search_item)
        
        product = [p for p in products if p['id'] == search_term]
        
        if not product:
            print("Product Not found")
            
        result.append(product)
        
        print(result)
        
    else:
        search_term = search_item.strip().lower()
        # if search_term in products['name']:
        
        for product in products:
            if search_term in product['name'].lower():
                result.append(product) 
        print(result)
        return result         
        
def update_product():
    edit_id = int(input("Enter the id you want to update:  "))
    
    product = [p for p in products if p['id'] == edit_id]
    
    if not product:
        print("product not found")
        return
        
    product = product[0]
    
    
    _name = input("Name:   ")
    while _name == "":
        print("Name cannot be empty")
        _name = input("Name:   ")
        
    _category = input("category:   ")
    while _category == "":
        print("Category cannot be empty")
        _category = input("category:   ")
        
        
    while True:
        try:
            _price = float(input("Price:     "))
            if _price <= 0:
                print("Price must be grater than 0")
                continue
            break
        except ValueError:
            print("value must be a number")
            
    while True:
        try:
            _quantity = int(input("Quantity:     "))
            if _quantity <= 0:
                print("Quantity must be grater than 0")
                continue
            break
        except ValueError:
            print("Quantity must be an Number")    
    product['name'] = _name
    product['category'] = _category
    product['price'] = _price
    product['quantity'] = _quantity
    
    

    
    ...
    
def delete_product():
    id_del = int(input("Enter the Id:  "))
    
    product = [p for p in products if p['id'] == id_del]
    
    if not product:
        print("Id not found to delete")
        return
    
    product = product[0]
    
    ans = input("Are you sure you want to delete [y/n]: ")
    
    if ans.strip().lower() == 'y':
        products.remove(product)
        print("Product Deleted Succesfully")
    else:
        print("Not Deleted")
def main():
    subprocess.call(['cls'], shell=True)
    while True:
        choice = menu()
        match choice:
            case 6:
                break
            case 1:
                add_product()
            case 2:
                view_product()
            case 3:
                search_product()
            case 4:
                update_product()
            case 5:
                delete_product()
            case _:
                print("Enter a valid choise to process the action")
                
                
if __name__ == '__main__':
    main()
        
        
        