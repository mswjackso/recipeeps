@auth.requires_login()
def index():

  recipes = db(db.Recipe.user_ref==auth.user.id).select(orderby=db.Recipe.category)

  form = SQLFORM(db.Recipe)
  if form.process().accepted:
    session.flash = 'Recipe added'
    categoryExist = db(db.Category.name==form.vars.category).select().first()
    print categoryExist
    print form.vars
    if categoryExist == None:
      db.Category.insert(name=form.vars.category)
    redirect(URL('main','index'))

  return dict(recipes=recipes, form=form)

@auth.requires_login()
def recipe():

  recipe = db(db.Recipe.title==request.args(0).replace("_", " ")).select().first()
  pictures = db(db.Picture.recipe_ref==recipe.id).select()
  recipeForm = SQLFORM(db.Recipe, recipe, deletable=True, showid=False)
  pictureForm = SQLFORM(db.Picture, showid=False)

  if recipeForm.process().accepted:
    if recipeForm.vars.delete_this_record!=None:
      session.flash = "Recipe removed"
      redirect(URL('main','index'))
    else:
      session.flash = "Saved"
      redirect(URL('main','recipe', recipeForm.vars.title.replace(" ","_")))

  if pictureForm.process().accepted:
    session.flash = "Picture added"
    redirect(URL('main','recipe', recipe.title.replace(" ","_")))

  return dict(recipe=recipe, recipeForm=recipeForm, pictures=pictures, pictureForm=pictureForm)
