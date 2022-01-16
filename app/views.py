# Imports
from flask import abort, flash, redirect, render_template, url_for
from forms import ItemForm
from . import db
from . import Item

def list_items():
    """
    List all items
    """

    items = Item.query.all()

    return render_template('items/items.html',
                          items = items, title="Items")

def add_item():
    """
    Add an Item to the database
    """

    add_item = True

    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name = form.name.data,
                    quantity = form.quantity.data,
                    description = form.description.data)
        
        try:
            # add item to the database
            db.session.add(item)
            db.session.commit()
            flash('You have added a new item.')
        except:
            # if the item already exists
            flash('Sorry: item name already exists.')
        
        # redirect to items page
        return redirect(url_for('list_items'))

    # load item template
    return render_template('items/item.html', action = "Add", add_item = add_item, form = form, title = "Add Item")

def edit_item(id):
    """
    Edit an Item
    """

    add_item = False

    item = Item.query.get_or_404(id)
    form = ItemForm(obj=item)
    if form.validate_on_submit:
        item.name = form.name.data
        item.quantity = form.quantity.data
        item.description = form.description.data
        db.session.commit()
        flash('You have edited the item.')

        # redirect to items page
        return redirect(url_for('list_items'))

    form.description.data = item.description
    form.quantity.data = item.quantity
    form.name.data = item.name
    # load item template
    return render_template('items/item.html', action ="Edit", add_item = add_item, form = form, item = item, title = "Edit Item")