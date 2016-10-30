"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from collections import defaultdict

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
db.session.query(Model).filter(Model.name=="Corvette", Model.brand_name=='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year<1960).all()

# Get all brands that were founded after 1920.
db.session.query(Brand).filter(Brand.founded >1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
db.session.query(Brand).filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued.isnot(None))|(Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
db.session.query(Model).filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_list = db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter_by(year=year).all()
    for model in model_list:
        print "Model: %s Brand_name: %s Brand_headquarter: %s" %(model[0], model[1], model[2])


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_model_list = db.session.query(Brand.name, Model.name).all()
    brand_dict = defaultdict(list)

    for brand, model in brand_model_list:
        brand_dict.append(model)

    for key in brand_dict:
        print key, brand_dict[key]

    

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
# It's a query object of Brand class where the brand name is Ford 

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

"""Association table is used to serve as a bridge in a "many to many" relationship.
The table itself has no meaningful field but holds the foreign keys of the two 
tables it connects.
"""
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """returns objects that are brands whose name contains or is equal to the input string"""
    return db.session.query(Brand).filter.like(Brand.name.like('% {} %').format(mystr)).all()


def get_models_between(start_year, end_year):
    """returns objects that are models with years that fall between the start year and end year"""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
