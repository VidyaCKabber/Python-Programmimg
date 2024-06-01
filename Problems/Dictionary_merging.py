items = {
    "123": {"name": "Book", "price": "$10"}
}

item_data = {"price": "$12", "author": "Author Name"}

item_id = "123"
items[item_id] |= item_data

print(items)

#output
#{'123': {'name': 'Book', 'price': '$12', 'author': 'Author Name'}}


