# Imports
import csv
from flask import abort, flash, redirect, render_template, url_for
from .forms import ItemForm
from .. import db
from ..model import Item
from . import items_blueprint
from io import StringIO

from werkzeug.wrappers import Response

@items_blueprint.route('/', methods=['GET', 'POST'])
def list_items():
    """
    List all items
    """
    
    items = Item.query.all()

    return render_template('items/items.html',
                          items=items, title="Items")

@items_blueprint.route('/add', methods=['GET', 'POST'])
def add_item():
    """
    Add an Item to the database
    """

    add_item = True

    form = ItemForm()
    if form.validate_on_submit():
        item = Item(name=form.name.data,
                    quantity=form.quantity.data,
                    description=form.description.data)
        
        try:
            # add item to the database
            db.session.add(item)
            db.session.commit()
            flash('You have added a new item.')
        except:
            # if the item already exists
            flash('Sorry: item name already exists.')
        
        # redirect to items page
        return redirect(url_for('items.list_items'))

    # load item template
    return render_template('items/item.html', action="Add", add_item=add_item, form=form, title="Add Item")

@items_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    """
    Edit an Item
    """

    add_item = False

    item = Item.query.get_or_404(id)
    form = ItemForm(obj=item)
    if form.validate_on_submit():
        item.name = form.name.data
        item.quantity = form.quantity.data
        item.description = form.description.data
        db.session.commit()
        flash('You have edited the item.')

        # redirect to items page
        return redirect(url_for('items.list_items'))

    form.description.data = item.description
    form.quantity.data = item.quantity
    form.name.data = item.name
    # load item template
    return render_template('items/item.html', action ="Edit", add_item=add_item, form=form, item=item, title="Edit Item")

@items_blueprint.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_item(id):
    """
    Delete a item from the database
    """

    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('You have deleted the item')

    # redirect to items page
    return redirect(url_for('items.list_items'))

    # return render_template(title = "Delete Item")

def generate_csv(items):
        """
        Generate a csv file
        """

        data = StringIO()
        write = csv.writer(data)
        
        # write the header
        write.writerow(['Name', 'Quantity', 'Description'])
        yield data.getvalue()
        data.seek(0)
        data.truncate(0)

        # write each item in items
        for item in items:
            write.writerow([item.name, item.quantity, item.description])
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

@items_blueprint.route('/export', methods=['GET', 'POST'])
def export():
    """
    Export Items as csv
    """
    items = Item.query.all()

    response = Response(generate_csv(items), mimetype='text/csv')

    # add a filename
    response.headers.set("Content-Disposition", "attachment", filename="items.csv")
    return response
    