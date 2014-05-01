@auth.requires_login()
def index():

  recipes = db(db.Recipe.user_ref==auth.user.id).select(orderby=db.Recipe.category)

  form = SQLFORM(db.Recipe)
  if form.process().accepted:
    session.flash = 'Hurray'
    redirect(URL('main','index'))

  return dict(recipes=recipes, form=form)

@auth.requires_login()
def recipe():
  
  recipe = db(db.Recipe.title==request.args(0).replace("_", " ")).select().first()
  pictures = db(db.Picture.recipe_ref==recipe.id).select()
  form = SQLFORM(db.Recipe, recipe)
  
  if form.process().accepted:
    session.flash = "Saved"
    redirect(URL('main','recipe', form.vars.title.replace(" ","_")))
  
  return dict(recipe=recipe, form=form, pictures=pictures)
