import models, time


async def get_all_activity  (app, client):
    '''
    getting data of all activity
    '''
    async with app.db.acquire() as conn:
        await select_all = select([Activity.__table__.c.id,
                                   Activity.__table__.c.name]).\
                           where(Activity.__table__.c.user_id == client)
        await result = conn.execute(select_all)


async def get_activity_using_id(app, client, id):
      '''
      data of some activity using its id
      '''
      with app.db.acquire() as conn:
          await select_one = select([Activity.__table__.c.id,
                               Activity.__table__.c.name]).\
                               where(
                               and_(Activity.__table__.c.id == id\
                                    Activity.__table__.c.id == client)
          await result = conn.execute(select_all)


async def create_activity(app, client_id, a_name ):
     '''
         adding activity in the database
     '''
     with app.db.acquire() as conn:
         await insert_one = Actity.__table__.insert().values(name = a_name,
                            data_created = time.time())

         await result = conn.execute(insert_one)


async def update_name(app, client_id, a_name,id ):
     '''
         update activity in the database
     '''
     with app.db.acquire() as conn:
         await update_one = Actity.__table__.update().\
                            values(name = a_name).\
                            where(Activity.__table__.c.id == id))
         await result = conn.execute(update_one)


 def delete(app, client_id, id ):
     '''
     deleting a specific activity using its id
     '''
    with app.db.acquire() as conn:
         await delete_one = Actity.__table__.delete().\
                            where(Activity.__table__.c.id == id))
         await result = conn.execute(delete_one)
