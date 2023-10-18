import psycopg2

def connect_to_database():
    """Connects to the PostgreSQL database.
    Returns:
        A psycopg2 connection object.
    """
    with psycopg2.connect(dbname='clients_db',
                                user='postgres',
                                password='postgres',
                                host='localhost',
                                port=5432) as conn:
        return conn

def get_client_total_prices_using_inner_join():
  """Gets the total price for each client using an INNER JOIN.
  Returns:
    A list of tuples, where each tuple contains the client name and total price.
  """
  conn = connect_to_database()
  with conn.cursor() as cur:
    sql = """
      SELECT clients.name, SUM(products.price) AS total_price
      FROM clients
      INNER JOIN products ON clients.id = products.id
      GROUP BY clients.name
      ORDER BY total_price DESC;
    """
    cur.execute(sql)
    results = cur.fetchall()

    return results

def get_client_total_prices_using_left_join():
  """Gets the total price for each client using a LEFT JOIN.
  Returns:
    A list of tuples, where each tuple contains the client name and total price.
  """
  conn = connect_to_database()
  cur = conn.cursor()

  sql = """
      SELECT clients.name, SUM(products.price) AS total_price
      FROM clients
      LEFT JOIN products ON clients.id = products.id
      GROUP BY clients.name
      ORDER BY total_price DESC;
    """

  cur.execute(sql)
  results = cur.fetchall()

  cur.close()
  conn.close()

  return results

def get_client_total_prices_using_full_outer_join():
  """Gets the total price for each client using a FULL OUTER JOIN.
  Returns:
    A list of tuples, where each tuple contains the client name and total price.
  """
  conn = connect_to_database()
  cur = conn.cursor()

  sql = """
      SELECT clients.name, SUM(products.price) AS total_price
      FROM clients
      FULL OUTER JOIN products ON clients.id = products.id
      GROUP BY clients.name
      ORDER BY total_price DESC;
    """
  cur.execute(sql)
  results = cur.fetchall()

  cur.close()
  conn.close()

  return results

def main():
  """Gets the total price for each client using different types of SQL joins."""

  client_total_prices_using_inner_join = get_client_total_prices_using_inner_join()
  client_total_prices_using_left_join = get_client_total_prices_using_left_join()
  client_total_prices_using_full_outer_join = get_client_total_prices_using_full_outer_join()

  print("Total prices using INNER JOIN:")
  print("\n".join([f"{client_name}: {total_price}" for client_name, total_price in client_total_prices_using_inner_join]))

  print("\nTotal prices using LEFT JOIN:")
  print("\n".join([f"{client_name}: {total_price}" for client_name, total_price in client_total_prices_using_left_join]))

  print("\nTotal prices using FULL OUTER JOIN:")
  print("\n".join([f"{client_name}: {total_price}" for client_name, total_price in client_total_prices_using_full_outer_join]))

if __name__ == "__main__":
  main()

# OUTPUT:
# Total prices using INNER JOIN:
# Carol: 300.00
# Bob: 200.00
# Alice: 100.00

# Total prices using LEFT JOIN:
# Carol: 300.00
# Bob: 200.00
# Alice: 100.00

# Total prices using FULL OUTER JOIN:
# Carol: 300.00
# Bob: 200.00
# Alice: 100.00
# dci-student  17-10-2023-python-databases-advanced-Lightmaker777  ➜ ( main)  ♥ 12:17 