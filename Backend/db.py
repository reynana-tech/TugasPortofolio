import pymysql
from config import Config

_conn = None


def _create_connection():
    ca_path = Config.TIDB_SSL_CA
    ssl_params = {'ca': ca_path} if ca_path else None

    if not Config.TIDB_HOST:
        raise Exception("TIDB_HOST environment variable is not set")

    conn = pymysql.connect(
        host=Config.TIDB_HOST,
        port=Config.TIDB_PORT,
        user=Config.TIDB_USER,
        password=Config.TIDB_PASSWORD,
        database=Config.TIDB_DB,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        ssl=ssl_params,
        autocommit=False,
        connect_timeout=10
    )
    return conn


def get_db():
    """Return a reusable DB connection. Caller should call commit/rollback as needed.
    Connection will be re-created if closed.
    """
    global _conn
    try:
        if _conn is None:
            _conn = _create_connection()
        else:
            try:
                # ping with reconnect to ensure connection is alive
                _conn.ping(reconnect=True)
            except Exception:
                _conn = _create_connection()
        return _conn
    except Exception as e:
        print(f"❌ Database connection error (Backend.db.get_db): {e}")
        raise


def close_db():
    global _conn
    try:
        if _conn:
            _conn.close()
    finally:
        _conn = None
