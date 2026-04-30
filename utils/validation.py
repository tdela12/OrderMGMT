from enums import Status


def validate_field(value, cast_type, field_name):
    try:
        return cast_type(value)
    except (ValueError, TypeError):
        raise(f"{field_name} ({value!r}) is not valid")


def validate_order_details(_customer_id, _product_id, _quantity):
    validate_field(_customer_id, str, 'customer_id')
    validate_field(_product_id, str, 'product_id')
    validate_field(_quantity, int, 'quantity')

