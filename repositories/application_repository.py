import sqlite3

from queries.application_queries import GET_APPLICATION_ARTIFACTS

DB_PATH = "db/reconciliation.db"

def get_application_artifacts(application_id: int):
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    
    try:
        row = connection.execute(
            GET_APPLICATION_ARTIFACTS,
            (application_id,),
        ).fetchone()
        
        if row is None:
            return None
        
        return dict(row)
    finally:
        connection.close()