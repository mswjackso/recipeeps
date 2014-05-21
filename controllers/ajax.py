def removeAllPictures():
  id = request.args[0]
  db(db.Picture.recipe_ref==id).delete()
  return "Complete"
