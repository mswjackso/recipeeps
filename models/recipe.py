from datetime import datetime

db.define_table('Category',
  Field('name','string'),
  format = '%(name)s'
)

db.define_table('Recipe',
  Field('user_ref','reference auth_user', default=auth.user_id, readable=False, writable=False),
  Field('creationTime','datetime', default=datetime.utcnow(), readable=False, writable=False),
  Field('title','string', requires=IS_NOT_EMPTY()),
  Field('category','string', requires=IS_NOT_EMPTY()),
  Field('ingredients','list:string', requires=IS_NOT_EMPTY()),
  Field('directions','list:string', requires=IS_NOT_EMPTY()),
  Field('src','string'),
  Field('notes','text'),
  Field('pictures','list:reference Picture', readable=False, writable=False),
)

db.define_table('Picture',
  Field('picture','upload',requires=IS_IMAGE()),
  Field('recipe_ref', 'reference Recipe')
)
