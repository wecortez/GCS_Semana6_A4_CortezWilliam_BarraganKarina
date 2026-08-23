# tests/test_app.py
# Prueba inicial: Karina Barragán
# Prueba de filtro: William Cortez

from src.app import add_product, filter_products_by_date, list_products


def setup_function():
    list_products().clear()


def test_add_and_list():
    add_product("Oso de peluche", 3)

    assert {"name": "Oso de peluche", "qty": 3} in list_products()


def test_filter_products_by_date():
   add_product("Carro", 4, "2026-08-20")
   add_product("Muñeca", 2, "2026-08-21")
   add_product("Pelota", 3)

   result = filter_products_by_date("2026-08-20")
   names = [product["name"] for product in result]

   assert "Carro" in names
   assert "Muñeca" not in names
   assert "Pelota" not in names