def get_db() -> Session:
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()