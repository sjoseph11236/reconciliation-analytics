DB=db/reconciliation.db
SCHEMA=db/schema.sql
SEED=db/seed.sql

install:
	python3 -m pip install -r requirements.txt

reset-db:
	@rm -f ${DB}
	@sqlite3 ${DB} < ${SCHEMA}
	@sqlite3 ${DB} < ${SEED}
	@echo "Database reset and seeded"

dev:
	@PYTHONPATH=. python3 src/poller.py
	
start: 
	@python3 -m uvicorn api.app:app --reload

mcp-dev:
	@mcp dev mcp_server/server.py