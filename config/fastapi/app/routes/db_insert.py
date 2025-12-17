from fastapi import APIRouter
from sqlalchemy import create_engine, text

from app.settings import db_name, db_user, db_password

router_insert = APIRouter()

def connect_to_db(db_name:str, db_user:str, db_password:str):
    return create_engine(
        f"jdbc:postgresql://{db_name}:{db_user}@localhost:5432/{db_password}"
    )

@router_insert.post("/insert_user")
async def insert_user(request):

    try:
        db_connection = connect_to_db(db_user=db_user, db_password=db_password, db_name=db_name)

#TODO TO DO ZROBIENIA DYNAMICZNIE

        params = {
            "name": request.name,
            "posts": request.posts,
            "location": request.location
        }

        sql_query = """
                    insert into public.users (name, posts, location) 
                    values (:name, :posts, :location); \
                    """

        with db_connection.connect() as conn:
            result = conn.execute(sql_query)
            conn.commit()
            print(result)

    except Exception as e:
        print(e)
        raise e

    return {"status":1}

