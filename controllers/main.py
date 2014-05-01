@auth.requires_login()
def index():

  recipes = db(db.Recipe.user_ref==auth.user.id).select(orderby=db.Recipe.category)

  form = SQLFORM(db.Recipe)
  if form.process().accepted:
    response.flash = 'Hurray'
    redirect()

  return dict(recipes=recipes, form=form)
