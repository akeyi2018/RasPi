from flaskr.models import Entry, db

#Entry.query.all()

#entry = Entry(title='title', text='text')
#db.session.add(entry)
#db.session.commit()

#entry = Entry.query.get(2)
#entry.title = 'hello_world'
#db.session.add(entry)
#db.session.commit()

#print(Entry.query.all())

#entry = Entry.query.filter(Entry.title == 'hello_world').first()
#print(entry)

#db.session.delete(entry)
#db.session.commit()

print(Entry.query.all())


