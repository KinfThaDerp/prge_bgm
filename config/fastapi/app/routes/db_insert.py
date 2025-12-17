from fastapi import APIRouter
from sqlalchemy import create_engine, text

router_insert = APIRouter()

def connect_to_db():
    return create_engine(
        f"postgresql://postgres:postgres@localhost:5432/postgres"
    )

@router_insert.get("/insert_user")
async def insert_user():

    try:
        db_connection = connect_to_db()

        sql_query = text("""
                    INSERT INTO public.users (name, posts, location) 
                    VALUES ('Janek', 10, 'Gdańsk')
                    """)

        with db_connection.connect() as conn:
            result = await conn.execute(sql_query)
            conn.commit()
            print(result)

    except Exception as e:
        print(e)
        raise e

    return {"status":1}

