import stripe

stripe.api_key = 'sk_test_WpiP6ZHMMmXneBSord0so6ma00DxUHSaGk'

def lambda_handler(event, context):
  stripe.InvoiceItem.create(
      customer="cus_HALwlLyAqv6WtK",
      amount=20,
      currency="usd",
      description="Advertisement cost",
  )
  return ("Invoice Item added")
